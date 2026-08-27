"""
OicInsuranceAgent: Office of Insurance Commission (OIC) Regulatory Sub-Agent.
Specialized in Insurance IT Governance B.E. 2563 and Bancassurance Compliance.
"""

from typing import Any

from ..tools.oic_tools import search_oic_insurance_regulations, verify_bancassurance_it_governance
from ..tools.schemas import FSIRegulatoryQueryInput


class OicInsuranceAgent:
    """Specialist sub-agent for OIC Thailand bancassurance and insurance IT governance."""

    def __init__(self, name: str = "OicInsuranceAgent"):
        self.name = name
        self.regulator = "OIC"
        self.role_description = (
            "Specialist Counsel for Office of Insurance Commission (OIC) directives, "
            "focusing on insurance IT governance, customer consent, and digital bancassurance."
        )

    def process_query(self, topic: str) -> dict[str, Any]:
        """Queries OIC statutory guidelines and circulars."""
        query_input = FSIRegulatoryQueryInput(
            regulator="OIC",
            topic=topic,
            entity_scope="FINANCIAL_CONGLOMERATE"
        )
        return search_oic_insurance_regulations(query_input)

    def verify_bancassurance(self, channel: str = "Bank_Branch_and_Mobile_App") -> dict[str, Any]:
        """Verifies digital bancassurance channel architecture."""
        return verify_bancassurance_it_governance(channel)
