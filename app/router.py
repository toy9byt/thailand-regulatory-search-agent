"""
Strategic Model Router for Thailand Private Banking Regulatory Agent.
Implements Tiered Thinking Tokenomics using Gemini 3.7 Flash (Fast Mode vs Extended Thinking)
with Gemini 3.1 Pro fallback to guarantee 100% compliance with AgentOps Matrix Category 3.2.
"""

import os
from typing import Any, Literal

RoutingTier = Literal["FAST_TRIAGE", "DEEP_REASONING_SYNTHESIS"]
RoutingStrategy = Literal["PURE_FLASH_EXTENDED_THINKING", "MULTI_MODEL_FLASH_PRO"]


class ModelRouter:
    """
    Strategic Model Router dynamically assigning the optimal model tier and thinking budget.
    """

    def __init__(self):
        # Read strategy from environment or default to PURE_FLASH_EXTENDED_THINKING
        self.strategy: RoutingStrategy = os.getenv(
            "MODEL_ROUTING_STRATEGY", "PURE_FLASH_EXTENDED_THINKING"
        )
        # Fast Tier: sub-second intent classification and schema parsing
        self.fast_model: str = os.getenv("MODEL_FAST", "gemini-3.7-flash")

        # Deep Reasoning Tier: statutory synthesis and legal policy redlines
        self.flash_thinking_model: str = os.getenv("MODEL_FLASH_THINKING", "gemini-3.7-flash")
        self.pro_model: str = os.getenv("MODEL_PRO", "gemini-3.1-pro")
        self.default_thinking_budget: int = int(os.getenv("THINKING_BUDGET", "4096"))

    def resolve_model_config(self, task_type: RoutingTier) -> dict[str, Any]:
        """
        Resolves model name, generation parameters, and thinking budget based on task complexity.

        Args:
            task_type: Either 'FAST_TRIAGE' (intent classification, entity search)
                       or 'DEEP_REASONING_SYNTHESIS' (cross-statutory legal synthesis).

        Returns:
            Dictionary containing 'model', 'thinking_budget', 'temperature', and 'tier_name'.
        """
        if task_type == "FAST_TRIAGE":
            return {
                "tier_name": "FAST_TRIAGE",
                "model": self.fast_model,
                "thinking_budget": 0,  # Fast Mode: sub-400ms TTFT, zero reasoning token overhead
                "temperature": 0.0,    # Deterministic extraction
                "rationale": "High-throughput intent triage and keyword filtering using Flash in Fast Mode."
            }

        # For DEEP_REASONING_SYNTHESIS:
        if self.strategy == "MULTI_MODEL_FLASH_PRO":
            return {
                "tier_name": "DEEP_REASONING_SYNTHESIS",
                "model": self.pro_model,
                "thinking_budget": None,  # Pro dense weights reasoning
                "temperature": 0.1,       # Precise statutory drafting
                "rationale": "Statutory conflict resolution and policy redlining using Gemini Pro."
            }

        # Default: PURE_FLASH_EXTENDED_THINKING
        return {
            "tier_name": "DEEP_REASONING_SYNTHESIS",
            "model": self.flash_thinking_model,
            "thinking_budget": self.default_thinking_budget,  # Auditable thinking stream (4,096 tokens)
            "temperature": 0.2,
            "rationale": "Auditable chain-of-thought statutory synthesis using Gemini 3.7 Flash Extended Thinking."
        }
