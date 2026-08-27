"""
Personal Data Protection Commission (PDPC / สำนักงาน สคส.) Statutory Compliance Tools.
Specialized in Personal Data Protection Act B.E. 2562 (PDPA), Section 28-29 Cross-Border Cloud Transfers,
DPO Governance, and Sensitive Financial PII Safeguards.
"""

from typing import Any

from .error_handler import build_guided_error_response, handle_sfi_exclusion_error
from .schemas import (
    FSIRegulatoryQueryInput,
    FSIRegulatorySearchResult,
    RegulatoryObligation,
    StatutoryCitation,
)

PDPA_MANDATES_REGISTRY: list[RegulatoryObligation] = [
    RegulatoryObligation(
        obligation_id="OBL-PDPA-CROSSBORDER-01",
        title="Cross-Border Data Transfer Adequacy & Standard Contractual Clauses (SCCs)",
        mandate_description=(
            "Personal financial data sent to foreign Cloud Service Provider (CSP) data regions outside Thailand "
            "must comply with Section 28 (adequate protection destination) or execute Section 29 Standard Contractual Clauses (SCCs) "
            "or certified Binding Corporate Rules (BCRs) guaranteeing enforceable data subject rights."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA) และประกาศคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล เรื่อง หลักเกณฑ์การให้ความคุ้มครองข้อมูลส่วนบุคคลที่ส่งหรือโอนไปยังต่างประเทศ พ.ศ. 2566",
            statute_name_en="Personal Data Protection Act B.E. 2562 (2019): Cross-Border Data Transfer Criteria B.E. 2566",
            section_or_clause="มาตรา 28 และมาตรา 29",
            issuing_authority="Personal Data Protection Commission (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล)",
            enactment_date="2023-12-25",
            gazette_reference="เล่ม 140 ตอนพิเศษ 321 ง หน้า 1",
            official_source_url="https://www.pdpc.or.th/regulations/cross-border-transfers",
        ),
        severity="CRITICAL",
        enforcement_sanction="Administrative fines up to ฿5,000,000 and punitive damages up to 2x under Section 83 and Section 77.",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-PDPA-BREACH-01",
        title="72-Hour Data Breach Notification & DPO Appointment",
        mandate_description=(
            "Commercial banks acting as Data Controllers must designate a Data Protection Officer (DPO) and notify "
            "the PDPC Office within 72 hours of becoming aware of any personal data breach posing risk to customer rights. "
            "High-risk breaches require immediate notification to affected customers without undue delay."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA) มาตรา 37 และมาตรา 41",
            statute_name_en="Personal Data Protection Act B.E. 2562: Data Breach Notification & DPO Mandate",
            section_or_clause="มาตรา 37(4) และมาตรา 41",
            issuing_authority="Personal Data Protection Commission (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล)",
            enactment_date="2019-05-27",
            gazette_reference="เล่ม 136 ตอนที่ 69 ก หน้า 52",
            official_source_url="https://www.pdpc.or.th/regulations/data-breach-notification",
        ),
        severity="CRITICAL",
        enforcement_sanction="Administrative fines up to ฿3,000,000 and criminal liability under Section 79.",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-PDPA-SENSITIVE-01",
        title="Sensitive PII & Biometric Explicit Consent for Financial Services",
        mandate_description=(
            "Collection of biometric data (facial recognition, fingerprint scans) for e-KYC or mobile banking "
            "strictly requires explicit, granular, unbundled consent under Section 26. Cannot be bundled into generic T&Cs."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA) มาตรา 26",
            statute_name_en="Personal Data Protection Act B.E. 2562: Sensitive Personal Data Criteria",
            section_or_clause="มาตรา 26 (ข้อมูลอ่อนไหวและข้อมูลชีวภาพ)",
            issuing_authority="Personal Data Protection Commission (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล)",
            enactment_date="2019-05-27",
            gazette_reference="เล่ม 136 ตอนที่ 69 ก หน้า 45",
            official_source_url="https://www.pdpc.or.th/regulations/sensitive-data",
        ),
        severity="HIGH",
        enforcement_sanction="Fines up to ฿5,000,000 and criminal imprisonment up to 1 year under Section 79.",
        is_state_owned_bank_only=False,
    ),
]


def search_pdpa_financial_data_regulations(
    query_input: FSIRegulatoryQueryInput
) -> dict[str, Any]:
    """
    Searches Personal Data Protection Act (PDPA) statutory provisions and subordinate rules for banking.

    Args:
        query_input: Structured FSIRegulatoryQueryInput containing regulator and topic.

    Returns:
        Structured dictionary adhering to FSIRegulatorySearchResult schema or ToolErrorResponse schema.
    """
    if "จัดซื้อจัดจ้าง" in query_input.topic or "sfi" in query_input.topic.lower():
        return handle_sfi_exclusion_error(query_input.topic)

    if query_input.regulator != "PDPC":
        return build_guided_error_response(
            error_code="REGULATOR_MISMATCH",
            message=f"pdpa_tools only handles PDPC queries, but received '{query_input.regulator}'.",
            recovery_suggestion="Verify target regulator. Use 'PDPC' for data privacy, cross-border transfers, and PII protection.",
            invalid_input_echo=query_input.model_dump()
        )

    results: list[RegulatoryObligation] = []
    keywords = query_input.topic.lower().split()
    for obligation in PDPA_MANDATES_REGISTRY:
        if any(kw in obligation.title.lower() or kw in obligation.mandate_description.lower() for kw in keywords):
            results.append(obligation)

    if not results:
        results = PDPA_MANDATES_REGISTRY

    return FSIRegulatorySearchResult(
        status="SUCCESS",
        regulator="PDPC",
        topic=query_input.topic,
        matched_obligations=results,
        total_found=len(results)
    ).model_dump()


def validate_cross_border_cloud_transfer(
    destination_region: str,
    data_classification: str = "Confidential_Banking_PII"
) -> dict[str, Any]:
    """
    Validates cross-border cloud architecture against PDPA Section 28 and 29 requirements.

    Args:
        destination_region: Cloud region name (e.g. 'asia-southeast1', 'us-central1').
        data_classification: Security classification of banking data transferred.

    Returns:
        Dict outlining mandatory transfer mechanisms, required SCC clauses, and DPO approvals.
    """
    is_local_thailand = "thailand" in destination_region.lower() or "bkk" in destination_region.lower() or "asia-southeast3" in destination_region.lower()
    return {
        "regulator": "PDPC",
        "destination_region": destination_region,
        "is_cross_border": not is_local_thailand,
        "mandatory_transfer_mechanism": (
            "Domestic data transfer; standard Section 37 security measures apply."
            if is_local_thailand
            else "Cross-border data transfer under Section 29; mandatory execution of Standard Contractual Clauses (SCCs) and Data Processing Agreement (DPA) with CSP."
        ),
        "encryption_requirement": "Customer-Managed Encryption Keys (CMEK) with keys stored within Thailand sovereignty perimeter.",
        "dpo_signoff_required": True,
    }
