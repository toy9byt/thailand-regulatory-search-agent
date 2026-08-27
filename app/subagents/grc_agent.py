"""
GrcSynthesizerAgent: Enterprise GRC Matrix and Policy Redline Sub-Agent.
Harmonizes cross-regulatory mandates from BOT, SEC, OIC, and PDPA into enterprise control objectives.
"""

from typing import Any

from ..tools.grc_tools import synthesize_enterprise_grc_controls


class GrcSynthesizerAgent:
    """Sub-agent responsible for cross-regulator synthesis and GRC control mapping."""

    def __init__(self, name: str = "GrcSynthesizerAgent"):
        self.name = name
        self.role_description = (
            "Lead Enterprise GRC Architect synthesizing statutory obligations across Thai regulators "
            "into actionable enterprise controls (CO-REG-TH-FSI-*) with audit evidence requirements."
        )

    def synthesize(self, collected_obligations: list[dict[str, Any]], workload: str) -> dict[str, Any]:
        """Harmonizes collected obligations into an executive GRC compliance matrix."""
        return synthesize_enterprise_grc_controls(collected_obligations, workload)
