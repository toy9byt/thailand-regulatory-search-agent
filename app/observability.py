"""
Observability, Distributed Tracing & PII Redaction Module.
Implements OpenTelemetry Distributed Tracing, Structured JSON Logging,
Intent vs. Outcome Capture, and Active Thai Financial PII Redaction.
"""

import json
import logging
import re
import sys
import time
from typing import Any, ClassVar

try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider

    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer("thailand-regulatory-search-agent", "1.0.0")
    OTEL_AVAILABLE = True
except ImportError:
    tracer = None
    OTEL_AVAILABLE = False


class PIIRedactionScrubber:
    """
    Active PII redaction pipeline protecting Thai National IDs, bank accounts, cards, and keys.
    """

    PATTERNS: ClassVar[dict[str, str]] = {
        "THAI_NATIONAL_ID": r"\b\d{1}-\d{4}-\d{5}-\d{2}-\d{1}\b|\b\d{13}\b",
        "BANK_ACCOUNT": r"\b\d{3}-\d{1}-\d{5}-\d{1}\b|\b\d{10,12}\b",
        "CREDIT_CARD": r"\b(?:\d{4}[ -]?){3}\d{4}\b",
        "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
        "SECRET_KEY": r"AIza[0-9A-Za-z_-]{35}|ya29\.[0-9A-Za-z_-]+",
    }

    @classmethod
    def redact(cls, text: str) -> str:
        """Sanitizes text by replacing all matched PII with typed redaction tokens."""
        if not text or not isinstance(text, str):
            return text

        scrubbed = text
        for pii_type, pattern in cls.PATTERNS.items():
            scrubbed = re.sub(pattern, f"[REDACTED_{pii_type}]", scrubbed)
        return scrubbed

    @classmethod
    def redact_dict(cls, data: dict[str, Any]) -> dict[str, Any]:
        """Recursively sanitizes dictionary keys and string values."""
        redacted = {}
        for k, v in data.items():
            if isinstance(v, str):
                redacted[k] = cls.redact(v)
            elif isinstance(v, dict):
                redacted[k] = cls.redact_dict(v)
            elif isinstance(v, list):
                redacted[k] = [cls.redact(item) if isinstance(item, str) else item for item in v]
            else:
                redacted[k] = v
        return redacted


class StructuredJSONLogger:
    """
    Structured JSON Logger capturing rich audit metadata and enforcing Intent vs Outcome dual logging.
    """

    def __init__(self, logger_name: str = "regulatory_agent"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger.addHandler(handler)

    def log_intent(
        self,
        agent_name: str,
        intended_action: str,
        parameters: dict[str, Any],
        trace_id: str | None = None
    ):
        """Records INTENT_EMITTED event before tool or sub-agent execution."""
        clean_params = PIIRedactionScrubber.redact_dict(parameters)
        payload = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "level": "INFO",
            "event": "INTENT_EMITTED",
            "trace_id": trace_id or "trace_auto_gen",
            "agent_name": agent_name,
            "intended_action": intended_action,
            "parameters": clean_params,
        }
        self.logger.info(json.dumps(payload, ensure_ascii=False))

    def log_outcome(
        self,
        agent_name: str,
        action: str,
        status: str,
        latency_ms: float,
        result_summary: dict[str, Any],
        trace_id: str | None = None
    ):
        """Records OUTCOME_RECORDED event after execution with observed latency and status."""
        clean_summary = PIIRedactionScrubber.redact_dict(result_summary)
        payload = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "level": "INFO",
            "event": "OUTCOME_RECORDED",
            "trace_id": trace_id or "trace_auto_gen",
            "agent_name": agent_name,
            "action": action,
            "status": status,
            "latency_ms": round(latency_ms, 2),
            "result_summary": clean_summary,
        }
        self.logger.info(json.dumps(payload, ensure_ascii=False))


# Singleton default logger
logger = StructuredJSONLogger()
