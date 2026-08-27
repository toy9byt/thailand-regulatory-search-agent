"""
NcsaCyberAgent: Specialized Sub-Agent for Thailand Cybersecurity Act B.E. 2562 (NCSA / สกมช.).
Focuses on Critical Information Infrastructure (CII) Data Center Standards, Physical & Environmental
Controls, Incident Escalation to NCSA/T-B CERT, and Annual Independent Cyber Audits.
"""

from typing import Any

from ..tools.ncsa_tools import search_thai_fsi_cybersecurity_act_mandates
from ..tools.schemas import FSIRegulatoryQueryInput


class NcsaCyberAgent:
    """
    Domain Specialist Sub-Agent evaluating Critical Information Infrastructure (CII)
    and Data Center compliance under the Thailand Cybersecurity Act B.E. 2562.
    """

    def __init__(self, name: str = "NcsaCyberAgent"):
        self.name = name
        self.regulatory_body = "NCSA_CYBERSECURITY_ACT"

    def process_query(self, topic: str) -> dict[str, Any]:
        """
        Executes statutory search and analysis for Cybersecurity Act B.E. 2562 mandates,
        focusing on Data Centers and critical financial infrastructure.

        Args:
            topic: Natural language topic (e.g., 'Data center CII compliance', '24h incident notification').

        Returns:
            Dictionary containing matched obligations, citations, and compliance guidelines.
        """
        query_input = FSIRegulatoryQueryInput(
            regulator="NCSA",
            topic=topic,
            entity_scope="PRIVATE_COMMERCIAL_BANK",
        )
        return search_thai_fsi_cybersecurity_act_mandates(query_input)
