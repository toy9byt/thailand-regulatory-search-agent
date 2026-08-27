"""
PdpaComplianceAgent: Personal Data Protection Commission (PDPC / สคส.) Regulatory Sub-Agent.
Specialized in Personal Data Protection Act B.E. 2562, Section 28-29 Cross-Border Cloud Transfers,
and Sensitive Financial PII Governance.
"""

from typing import Any

from ..tools.pdpa_tools import (
    search_pdpa_financial_data_regulations,
    validate_cross_border_cloud_transfer,
)
from ..tools.schemas import FSIRegulatoryQueryInput


class PdpaComplianceAgent:
    """Specialist sub-agent for Thai PDPA data privacy and cross-border data transfers."""

    def __init__(self, name: str = "PdpaComplianceAgent"):
        self.name = name
        self.regulator = "PDPC"
        self.role_description = (
            "Specialist Counsel for Personal Data Protection Act (PDPA B.E. 2562) compliance, "
            "focusing on cross-border cloud transfers (Sections 28-29), DPO mandates, and 72-hour breach notifications."
        )

    def process_query(self, topic: str) -> dict[str, Any]:
        """Queries PDPA statutory guidelines and cross-border transfer rules."""
        query_input = FSIRegulatoryQueryInput(
            regulator="PDPC",
            topic=topic,
            entity_scope="PRIVATE_COMMERCIAL_BANK"
        )
        return search_pdpa_financial_data_regulations(query_input)

    def validate_cloud_transfer(self, destination: str, classification: str = "Confidential_Banking_PII") -> dict[str, Any]:
        """Validates cross-border cloud architecture against PDPA transfer criteria."""
        return validate_cross_border_cloud_transfer(destination, classification)
