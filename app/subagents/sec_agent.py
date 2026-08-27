"""
SecMarketAgent: Securities and Exchange Commission (SEC) Regulatory Sub-Agent.
Specialized in Capital Market IT Standards, Cyber Resilience, and Digital Asset Decrees.
"""

from typing import Any

from ..tools.schemas import FSIRegulatoryQueryInput
from ..tools.sec_tools import (
    audit_trading_cloud_cyber_resilience,
    search_sec_capital_market_regulations,
)


class SecMarketAgent:
    """Specialist sub-agent for SEC Thailand capital market compliance."""

    def __init__(self, name: str = "SecMarketAgent"):
        self.name = name
        self.regulator = "SEC"
        self.role_description = (
            "Specialist Counsel for Securities and Exchange Commission (SEC) regulations, "
            "focusing on capital market cyber resilience and digital asset custody standards."
        )

    def process_query(self, topic: str) -> dict[str, Any]:
        """Queries SEC statutory guidelines and circulars."""
        query_input = FSIRegulatoryQueryInput(
            regulator="SEC",
            topic=topic,
            entity_scope="FINANCIAL_CONGLOMERATE"
        )
        return search_sec_capital_market_regulations(query_input)

    def audit_trading_platform(self, tier: str = "Mission_Critical") -> dict[str, Any]:
        """Audits cloud algorithmic trading infrastructure against SEC requirements."""
        return audit_trading_cloud_cyber_resilience(tier)
