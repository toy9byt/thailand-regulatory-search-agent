"""
Securities and Exchange Commission (SEC / สำนักงาน ก.ล.ต.) Statutory Compliance Tools.
Specialized in Cyber Resilience Guidelines, Capital Market IT Systems Standards,
and Digital Asset Business Emergency Decree B.E. 2561.
"""

from typing import Any

from .error_handler import build_guided_error_response, handle_sfi_exclusion_error
from .schemas import (
    FSIRegulatoryQueryInput,
    FSIRegulatorySearchResult,
    RegulatoryObligation,
    StatutoryCitation,
)

SEC_MANDATES_REGISTRY: list[RegulatoryObligation] = [
    RegulatoryObligation(
        obligation_id="OBL-SEC-CYBER-01",
        title="Capital Market Cyber Resilience & Threat Intelligence Sharing",
        mandate_description=(
            "Securities brokers, private banking wealth managers, and asset managers must implement "
            "NIST-aligned cyber defense frameworks. Mandatory participation in Thai Capital Market CERT (TCM-CERT) "
            "and immediate threat indicator sharing for active Distributed Denial of Service (DDoS) or ransomware."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศสำนักงานคณะกรรมการกำกับหลักทรัพย์และตลาดหลักทรัพย์ เรื่อง แนวทางการบริหารจัดการความเสี่ยงด้านไซเบอร์ (Cyber Resilience Guidelines)",
            statute_name_en="Securities and Exchange Commission Cyber Resilience Guidelines for Capital Market Intermediaries",
            section_or_clause="หมวด 3 ข้อ 12 (การประเมินภัยคุกคามและการแลกเปลี่ยนข้อมูลภัยไซเบอร์)",
            issuing_authority="Securities and Exchange Commission (สำนักงาน ก.ล.ต.)",
            enactment_date="2021-04-20",
            gazette_reference="คู่มือแนวทางปฏิบัติ ก.ล.ต. ฉบับที่ 2/2564",
            official_source_url="https://www.sec.or.th/TH/Pages/LawandRegulations/CyberResilience.aspx",
        ),
        severity="HIGH",
        enforcement_sanction="Administrative fine under Section 282 of the Securities and Exchange Act B.E. 2535 (up to ฿500,000 plus ฿10,000/day).",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-SEC-DIGITALASSET-01",
        title="Cold Storage Segregation & Multi-Signature Custody",
        mandate_description=(
            "Commercial banks operating digital asset custodian or brokerage subsidiaries must maintain >= 90% of client digital assets "
            "in air-gapped Cold Storage with multi-signature or Multi-Party Computation (MPC) quorum approval."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชกำหนดการประกอบธุรกิจสินทรัพย์ดิจิทัล พ.ศ. 2561 และประกาศ ก.ล.ต. ที่เกี่ยวข้อง",
            statute_name_en="Emergency Decree on Digital Asset Businesses B.E. 2561 (2018): Custody Standards",
            section_or_clause="มาตรา 30 และประกาศคณะกรรมการ ก.ล.ต. ที่ กธ. 19/2561",
            issuing_authority="Securities and Exchange Commission (สำนักงาน ก.ล.ต.)",
            enactment_date="2018-05-13",
            gazette_reference="เล่ม 135 ตอนที่ 33 ก หน้า 1",
            official_source_url="https://www.sec.or.th/TH/Pages/LawandRegulations/DigitalAsset.aspx",
        ),
        severity="CRITICAL",
        enforcement_sanction="Revocation of digital asset custodian license and criminal proceedings under Section 67.",
        is_state_owned_bank_only=False,
    ),
]


def search_sec_capital_market_regulations(
    query_input: FSIRegulatoryQueryInput
) -> dict[str, Any]:
    """
    Searches Securities and Exchange Commission (SEC) cyber resilience and digital asset standards.

    Exclusively targets private commercial banks and capital market affiliates.

    Args:
        query_input: Structured FSIRegulatoryQueryInput containing regulator and topic.

    Returns:
        Structured dictionary adhering to FSIRegulatorySearchResult schema or ToolErrorResponse schema.
    """
    if "จัดซื้อจัดจ้าง" in query_input.topic or "sfi" in query_input.topic.lower():
        return handle_sfi_exclusion_error(query_input.topic)

    if query_input.regulator != "SEC":
        return build_guided_error_response(
            error_code="REGULATOR_MISMATCH",
            message=f"sec_tools only handles SEC queries, but received '{query_input.regulator}'.",
            recovery_suggestion="Verify target regulator. Use 'SEC' for securities and capital market topics.",
            invalid_input_echo=query_input.model_dump()
        )

    results: list[RegulatoryObligation] = []
    keywords = query_input.topic.lower().split()
    for obligation in SEC_MANDATES_REGISTRY:
        if any(kw in obligation.title.lower() or kw in obligation.mandate_description.lower() for kw in keywords):
            results.append(obligation)

    if not results:
        results = SEC_MANDATES_REGISTRY

    return FSIRegulatorySearchResult(
        status="SUCCESS",
        regulator="SEC",
        topic=query_input.topic,
        matched_obligations=results,
        total_found=len(results)
    ).model_dump()


def audit_trading_cloud_cyber_resilience(
    trading_system_tier: str = "Mission_Critical"
) -> dict[str, Any]:
    """
    Audits algorithmic trading and wealth management cloud infrastructure against SEC cyber benchmarks.

    Args:
        trading_system_tier: Criticality classification of the trading platform.

    Returns:
        Dict outlining mandatory SEC controls and TCM-CERT reporting channels.
    """
    return {
        "regulator": "SEC",
        "system_tier": trading_system_tier,
        "mandatory_controls": [
            "TCM-CERT mandatory real-time incident escalation within 1 hour of DDoS detection.",
            "Independent penetration testing performed semi-annually by CREST-certified testers.",
            "Immutable WORM logging for all electronic trade execution orders with SHA-256 integrity.",
        ],
        "compliance_status": "COMPLIANT_SPEC",
    }
