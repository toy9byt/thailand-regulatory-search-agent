"""
RegulatoryCoordinatorAgent: Root Coordinator Agent for Thailand FSI Regulatory Search & Compliance.
Orchestrates domain sub-agents (BOT, SEC, OIC, PDPA, AI Governance), strategic model routing,
guardrails, human-in-the-loop checks, and enterprise GRC synthesis.
"""

from typing import Any

from .constitution import SYSTEM_CONSTITUTION
from .guardrails import HumanInTheLoopHook, InputGuardrail, OutputGuardrail
from .router import ModelRouter
from .subagents.ai_agent import AiGovernanceAgent
from .subagents.bot_agent import BotBankingAgent
from .subagents.grc_agent import GrcSynthesizerAgent
from .subagents.ncsa_agent import NcsaCyberAgent
from .subagents.oic_agent import OicInsuranceAgent
from .subagents.pdpa_agent import PdpaComplianceAgent
from .subagents.sec_agent import SecMarketAgent


class RegulatoryCoordinatorAgent:
    """
    Root Multi-Agent Coordinator implementing proven Coordinator-Worker architecture in Google ADK.
    """

    def __init__(self, name: str = "RegulatoryCoordinatorAgent"):
        self.name = name
        self.constitution = SYSTEM_CONSTITUTION
        self.router = ModelRouter()

        # Domain Specialist Sub-Agents
        self.bot_agent = BotBankingAgent()
        self.sec_agent = SecMarketAgent()
        self.oic_agent = OicInsuranceAgent()
        self.pdpa_agent = PdpaComplianceAgent()
        self.ai_agent = AiGovernanceAgent()
        self.ncsa_agent = NcsaCyberAgent()
        self.grc_agent = GrcSynthesizerAgent()

    def handle_compliance_inquiry(
        self,
        user_prompt: str,
        session_id: str = "default_session",
        confirmed_by_user: bool = False
    ) -> dict[str, Any]:
        """
        Main entrypoint processing enterprise private banking compliance inquiries.

        Args:
            user_prompt: Compliance question or architectural proposal.
            session_id: Client session identifier.
            confirmed_by_user: Boolean flag for high-stakes human approval.

        Returns:
            Dictionary containing compliance verdict, synthesized GRC matrix, and audit trace.
        """
        # 1. Ingress PII Sanitization (Zero-Trust Inbound Scrubber)
        from .observability import PIIRedactionScrubber
        clean_prompt = PIIRedactionScrubber.redact(user_prompt)

        # 2. Pre-execution Security & SFI Scope Guardrail
        is_valid, error_code, rejection_reason = InputGuardrail.validate_input(clean_prompt)
        if not is_valid:
            return {
                "status": "REJECTED_BY_GUARDRAIL",
                "error_code": error_code,
                "reason": rejection_reason,
                "session_id": session_id,
            }

        # 2. Strategic Model Routing: Resolve tier configuration
        triage_config = self.router.resolve_model_config("FAST_TRIAGE")
        synthesis_config = self.router.resolve_model_config("DEEP_REASONING_SYNTHESIS")

        # 3. Parallel/Sequential Sub-Agent Inquiries
        collected_obligations: list[dict[str, Any]] = []

        prompt_lower = clean_prompt.lower()

        # Route to BOT Agent
        if any(w in prompt_lower for w in ["bank", "cloud", "it risk", "outsourcing", "payment", "ธปท", "สนส"]):
            bot_res = self.bot_agent.process_query(topic=user_prompt)
            if bot_res.get("status") == "SUCCESS":
                collected_obligations.extend(bot_res.get("matched_obligations", []))

        # Route to SEC Agent
        if any(w in prompt_lower for w in ["trading", "securities", "digital asset", "wealth", "ก.ล.ต", "sec"]):
            sec_res = self.sec_agent.process_query(topic=user_prompt)
            if sec_res.get("status") == "SUCCESS":
                collected_obligations.extend(sec_res.get("matched_obligations", []))

        # Route to OIC Agent
        if any(w in prompt_lower for w in ["insurance", "bancassurance", "policy", "ประกัน", "คปภ", "oic"]):
            oic_res = self.oic_agent.process_query(topic=user_prompt)
            if oic_res.get("status") == "SUCCESS":
                collected_obligations.extend(oic_res.get("matched_obligations", []))

        # Route to PDPA Agent
        if any(w in prompt_lower for w in ["privacy", "pii", "personal data", "cross-border", "transfer", "pdpa", "สคส"]):
            pdpa_res = self.pdpa_agent.process_query(topic=user_prompt)
            if pdpa_res.get("status") == "SUCCESS":
                collected_obligations.extend(pdpa_res.get("matched_obligations", []))

        # Route to AI Governance Agent
        if any(w in prompt_lower for w in [
            "ai", "machine learning", "genai", "llm", "credit scoring", "algorithm",
            "ปัญญาประดิษฐ์", "model risk", "drift", "explainability", "etda", "aigc"
        ]):
            ai_res = self.ai_agent.process_query(topic=clean_prompt)
            if ai_res.get("status") == "SUCCESS":
                collected_obligations.extend(ai_res.get("matched_obligations", []))

        # Route to NCSA Cybersecurity Act Agent (CII & Data Centers)
        if any(w in prompt_lower for w in [
            "cyber", "ไซเบอร์", "ncsa", "สกมช", "cii", "data center",
            "ศูนย์ข้อมูล", "ดาต้าเซ็นเตอร์", "colocation", "t-b cert", "incident notification"
        ]):
            ncsa_res = self.ncsa_agent.process_query(topic=clean_prompt)
            if ncsa_res.get("status") == "SUCCESS":
                collected_obligations.extend(ncsa_res.get("matched_obligations", []))

        # Default fallback to BOT + PDPA if broad cloud inquiry
        if not collected_obligations:
            bot_res = self.bot_agent.process_query(topic="Cloud IT Risk Outsourcing")
            pdpa_res = self.pdpa_agent.process_query(topic="Cross-Border Data Transfer")
            collected_obligations.extend(bot_res.get("matched_obligations", []))
            collected_obligations.extend(pdpa_res.get("matched_obligations", []))

        # 4. GRC Synthesis using Deep Reasoning Tier
        grc_synthesis = self.grc_agent.synthesize(
            collected_obligations=collected_obligations,
            workload=clean_prompt[:100]
        )

        # 5. Check Human-in-the-Loop Gate
        if any(o.get("severity") == "CRITICAL" for o in collected_obligations if isinstance(o, dict)):
            hitl_eval = HumanInTheLoopHook.evaluate_action(
                action_name="COMMIT_POLICY_AMENDMENT_BOARD",
                parameters={"workload": clean_prompt, "obligations_count": len(collected_obligations)},
                confirmed_by_user=confirmed_by_user
            )
            if hitl_eval["status"] == "AWAITING_HUMAN_CONFIRMATION":
                grc_synthesis["requires_hitl_approval"] = True
                grc_synthesis["hitl_action_details"] = hitl_eval
                grc_synthesis["status"] = "AWAITING_HUMAN_CONFIRMATION"

        # 6. Post-execution Grounding Validation
        grounding_valid, _ = OutputGuardrail.verify_grounding(str(grc_synthesis))

        return {
            "status": grc_synthesis.get("status", "SUCCESS"),
            "session_id": session_id,
            "routing_metadata": {
                "triage_tier": triage_config,
                "synthesis_tier": synthesis_config,
            },
            "grc_synthesis": grc_synthesis,
            "statutory_grounding_verified": grounding_valid,
            "obligations_evaluated": len(collected_obligations),
        }
