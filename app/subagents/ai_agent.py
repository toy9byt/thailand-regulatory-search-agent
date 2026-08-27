"""
AiGovernanceAgent: Specialized Sub-Agent for Thailand FSI AI Governance.
Focuses on Bank of Thailand (BOT) AI/ML Principles, ETDA National AI Governance (AIGC),
and PDPA Automated Decision-Making (ADM) statutory compliance.
"""

from typing import Any

from ..tools.ai_governance_tools import search_thai_fsi_ai_governance_mandates
from ..tools.schemas import FSIRegulatoryQueryInput


class AiGovernanceAgent:
    """
    Domain Specialist Sub-Agent evaluating Artificial Intelligence & Machine Learning
    governance compliance across the Thai Financial Services Industry.
    """

    def __init__(self, name: str = "AiGovernanceAgent"):
        self.name = name
        self.regulatory_body = "BOT_ETDA_PDPC_AI"

    def process_query(self, topic: str) -> dict[str, Any]:
        """
        Executes statutory search and analysis for AI/ML Governance in financial workflows.

        Args:
            topic: Natural language topic (e.g., 'Explainability in credit scoring AI', 'Model validation').

        Returns:
            Dictionary containing matched obligations, citations, and compliance guidelines.
        """
        query_input = FSIRegulatoryQueryInput(
            topic=topic,
            entity_scope="PRIVATE_COMMERCIAL_BANK",
            regulator="BOT",
        )
        return search_thai_fsi_ai_governance_mandates(query_input)
