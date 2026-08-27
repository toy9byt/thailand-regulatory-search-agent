"""
BotBankingAgent: Specialized Bank of Thailand (BOT) Regulatory Compliance Sub-Agent.
Enforces Financial Institutions Businesses Act B.E. 2551 and Notification No. SorNorSor. 12/2563.
"""

from typing import Any

from ..tools.bot_tools import (
    extract_fsi_cloud_outsourcing_mandates,
    search_thai_fsi_regulatory_circulars,
)
from ..tools.schemas import FSIRegulatoryQueryInput


class BotBankingAgent:
    """Specialist sub-agent for Bank of Thailand commercial banking and IT risk regulations."""

    def __init__(self, name: str = "BotBankingAgent"):
        self.name = name
        self.regulator = "BOT"
        self.role_description = (
            "Specialist Counsel for Bank of Thailand banking regulations, including Notification "
            "No. SorNorSor. 12/2563 (IT Risk & Cloud Outsourcing) and the Payment Systems Act B.E. 2560."
        )

    def process_query(self, topic: str, circular_code: str | None = None) -> dict[str, Any]:
        """
        Executes statutory search and analysis for Bank of Thailand matters.

        Args:
            topic: Banking regulatory topic (e.g. 'Cloud Outsourcing', 'IT Risk').
            circular_code: Optional specific circular code (e.g. 'สนส. 12/2563').

        Returns:
            Dictionary matching FSIRegulatorySearchResult schema.
        """
        query_input = FSIRegulatoryQueryInput(
            regulator="BOT",
            topic=topic,
            circular_code=circular_code,
            entity_scope="PRIVATE_COMMERCIAL_BANK"
        )
        return search_thai_fsi_regulatory_circulars(query_input)

    def get_cloud_clauses(self, cloud_tier: str = "PaaS_or_SaaS") -> dict[str, Any]:
        """Extracts mandatory contractual clauses for third-party cloud outsourcing."""
        return extract_fsi_cloud_outsourcing_mandates(cloud_tier)
