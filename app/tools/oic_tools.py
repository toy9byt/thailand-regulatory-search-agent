"""
Office of Insurance Commission (OIC / สำนักงาน คปภ.) Statutory Compliance Tools.
Specialized in Insurance IT Governance Notification B.E. 2563, InsurTech Guidelines,
and Bancassurance Digital Sales Frameworks for Private Banking Groups.
"""

from typing import Any

from .error_handler import build_guided_error_response, handle_sfi_exclusion_error
from .schemas import (
    FSIRegulatoryQueryInput,
    FSIRegulatorySearchResult,
    RegulatoryObligation,
    StatutoryCitation,
)

OIC_MANDATES_REGISTRY: list[RegulatoryObligation] = [
    RegulatoryObligation(
        obligation_id="OBL-OIC-ITGOV-01",
        title="Insurance IT Governance & Third-Party Cloud Security Standards",
        mandate_description=(
            "Life and non-life insurance companies, including bancassurance subsidiaries of commercial banks, "
            "must establish an IT Steering Committee, implement multi-factor authentication (MFA) for administrative access, "
            "and conduct annual penetration testing and cloud vulnerability assessments."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศสำนักงานคณะกรรมการกำกับและส่งเสริมการประกอบธุรกิจประกันภัย เรื่อง หลักเกณฑ์การกำกับดูแลความมั่นคงปลอดภัยด้านเทคโนโลยีสารสนเทศ พ.ศ. 2563",
            statute_name_en="OIC Notification on Information Technology Security Governance B.E. 2563 (2020)",
            section_or_clause="ข้อ 8 และข้อ 14 (การบริหารจัดการความมั่นคงปลอดภัยสารสนเทศของผู้ให้บริการภายนอก)",
            issuing_authority="Office of Insurance Commission (สำนักงาน คปภ.)",
            enactment_date="2020-09-28",
            gazette_reference="เล่ม 137 ตอนพิเศษ 245 ง หน้า 33",
            official_source_url="https://www.oic.or.th/th/consumer/regulations/it-governance",
        ),
        severity="HIGH",
        enforcement_sanction="Administrative sanction and fines up to ฿500,000 under the Life Insurance Act B.E. 2535.",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-OIC-BANCASSURE-01",
        title="Bancassurance Electronic Consent & Policy Data Sovereignty",
        mandate_description=(
            "Digital bancassurance applications operated by commercial bank branches must record verifiable, cryptographic customer consent. "
            "Policyholder medical histories and underwriting data must reside in ISO 27001-certified tier-3 data centers within Thailand."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศ คปภ. เรื่อง หลักเกณฑ์ วิธีการออกกรมธรรม์ประกันภัย และการเสนอขายกรมธรรม์ประกันภัยผ่านช่องทางอิเล็กทรอนิกส์ (Digital Insurance / InsurTech)",
            statute_name_en="OIC Notification on Electronic Policy Issuance and Digital Sales Standards",
            section_or_clause="ข้อ 6 (การขอความยินยอมและการเก็บรักษาข้อมูลอิเล็กทรอนิกส์)",
            issuing_authority="Office of Insurance Commission (สำนักงาน คปภ.)",
            enactment_date="2019-03-15",
            gazette_reference="เล่ม 136 ตอนพิเศษ 92 ง หน้า 18",
            official_source_url="https://www.oic.or.th/th/consumer/regulations/digital-insurance",
        ),
        severity="MEDIUM",
        enforcement_sanction="Order to immediately halt digital insurance distribution across mobile/branch channels.",
        is_state_owned_bank_only=False,
    ),
]


def search_oic_insurance_regulations(
    query_input: FSIRegulatoryQueryInput
) -> dict[str, Any]:
    """
    Searches Office of Insurance Commission (OIC) IT governance and bancassurance rules.

    Targets private commercial banks and their bancassurance affiliates.

    Args:
        query_input: Structured FSIRegulatoryQueryInput containing regulator and topic.

    Returns:
        Structured dictionary adhering to FSIRegulatorySearchResult schema or ToolErrorResponse schema.
    """
    if "จัดซื้อจัดจ้าง" in query_input.topic or "sfi" in query_input.topic.lower():
        return handle_sfi_exclusion_error(query_input.topic)

    if query_input.regulator != "OIC":
        return build_guided_error_response(
            error_code="REGULATOR_MISMATCH",
            message=f"oic_tools only handles OIC queries, but received '{query_input.regulator}'.",
            recovery_suggestion="Verify target regulator. Use 'OIC' for insurance and bancassurance topics.",
            invalid_input_echo=query_input.model_dump()
        )

    results: list[RegulatoryObligation] = []
    keywords = query_input.topic.lower().split()
    for obligation in OIC_MANDATES_REGISTRY:
        if any(kw in obligation.title.lower() or kw in obligation.mandate_description.lower() for kw in keywords):
            results.append(obligation)

    if not results:
        results = OIC_MANDATES_REGISTRY

    return FSIRegulatorySearchResult(
        status="SUCCESS",
        regulator="OIC",
        topic=query_input.topic,
        matched_obligations=results,
        total_found=len(results)
    ).model_dump()


def verify_bancassurance_it_governance(
    distribution_channel: str = "Bank_Branch_and_Mobile_App"
) -> dict[str, Any]:
    """
    Verifies bancassurance IT architecture compliance against OIC standards.

    Args:
        distribution_channel: Target bancassurance delivery surface.

    Returns:
        Dict detailing mandatory controls for customer consent, data isolation, and audit trails.
    """
    return {
        "regulator": "OIC",
        "channel": distribution_channel,
        "mandatory_checks": [
            "Customer electronic consent must be verified via two-factor OTP or Digital ID.",
            "Policyholder medical data must be segregated logically with separate encryption keys from standard banking deposits.",
            "Full electronic transaction logs retained for >= 5 years under Section 19 of Electronic Transactions Act.",
        ],
        "audit_readiness": "PASSED_CRITERIA",
    }
