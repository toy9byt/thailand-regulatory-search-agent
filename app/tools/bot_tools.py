"""
Bank of Thailand (BOT / ธปท.) Statutory Compliance Tools.
Specialized in Notification No. SorNorSor. 12/2563 (IT Risk & Cloud Outsourcing),
Payment Systems Act B.E. 2560, and Financial Institutions Businesses Act B.E. 2551.
"""

from typing import Any

from .error_handler import (
    build_guided_error_response,
    handle_circular_lookup_error,
    handle_sfi_exclusion_error,
)
from .schemas import (
    FSIRegulatoryQueryInput,
    FSIRegulatorySearchResult,
    RegulatoryObligation,
    StatutoryCitation,
)

# Canonical In-Memory Knowledge Store for Bank of Thailand Mandates
BOT_MANDATES_REGISTRY: list[RegulatoryObligation] = [
    RegulatoryObligation(
        obligation_id="OBL-BOT-122563-01",
        title="Material Cloud Outsourcing Governance & Prior Risk Assessment",
        mandate_description=(
            "Commercial banks must conduct comprehensive third-party risk assessment prior to procuring material IT/Cloud services. "
            "Must establish board-approved outsourcing policies, business continuity plans (BCP), and disaster recovery (DR) testing >= 1 time/year."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2563 เรื่อง การบริหารจัดการความเสี่ยงด้านเทคโนโลยีสารสนเทศ (IT Risk)",
            statute_name_en="Bank of Thailand Notification No. SorNorSor. 12/2563: Information Technology Risk Governance",
            section_or_clause="ข้อ 5.2.1 (การจ้างบุคคลภายนอกด้านระบบงานสารสนเทศ)",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2020-07-31",
            gazette_reference="เล่ม 137 ตอนพิเศษ 188 ง หน้า 12",
            official_source_url="https://www.bot.or.th/content/dam/bot/documents/laws-and-regulations/fipm/SorNorSor12-2563.pdf",
        ),
        severity="HIGH",
        enforcement_sanction="Administrative penalty, formal regulatory warning, and order to suspend cloud operations under Section 120 of Financial Institutions Businesses Act.",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-BOT-122563-02",
        title="Unrestricted Right to Audit for Bank and BOT Examiners",
        mandate_description=(
            "Contracts with Cloud Service Providers (CSPs) must explicitly guarantee unrestricted access and right-to-audit "
            "for internal auditors, external auditors, and Bank of Thailand statutory examiners across all data centers, logs, and systems storing bank data."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2563 เรื่อง การบริหารจัดการความเสี่ยงด้านเทคโนโลยีสารสนเทศ (IT Risk)",
            statute_name_en="Bank of Thailand Notification No. SorNorSor. 12/2563: Information Technology Risk Governance",
            section_or_clause="ข้อ 5.2.2 (สิทธิการตรวจสอบและการเข้าถึงข้อมูล - Right to Audit)",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2020-07-31",
            gazette_reference="เล่ม 137 ตอนพิเศษ 188 ง หน้า 14",
            official_source_url="https://www.bot.or.th/content/dam/bot/documents/laws-and-regulations/fipm/SorNorSor12-2563.pdf",
        ),
        severity="CRITICAL",
        enforcement_sanction="Nullification of CSP engagement approval and immediate supervisory order to retrieve bank data from cloud premises.",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-BOT-122563-03",
        title="Fourth-Party Subcontractor Control & Cloud Exit Strategy",
        mandate_description=(
            "Commercial banks must mandate that CSPs obtain written consent before subcontracting core processing (fourth parties). "
            "Banks must formulate and maintain an operational, stress-tested Exit Strategy detailing data repatriation within 90 days without data loss."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2563 เรื่อง การบริหารจัดการความเสี่ยงด้านเทคโนโลยีสารสนเทศ (IT Risk)",
            statute_name_en="Bank of Thailand Notification No. SorNorSor. 12/2563: Information Technology Risk Governance",
            section_or_clause="ข้อ 5.2.3 (การจ้างช่วงและการจัดทำแผนรองรับการยกเลิกสัญญา - Exit Strategy)",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2020-07-31",
            gazette_reference="เล่ม 137 ตอนพิเศษ 188 ง หน้า 16",
            official_source_url="https://www.bot.or.th/content/dam/bot/documents/laws-and-regulations/fipm/SorNorSor12-2563.pdf",
        ),
        severity="HIGH",
        enforcement_sanction="Regulatory direction under Section 89 of Financial Institutions Businesses Act requiring capital charge increase for operational risk.",
        is_state_owned_bank_only=False,
    ),
    RegulatoryObligation(
        obligation_id="OBL-BOT-PSA-01",
        title="High-Availability Payment System Resiliency & 24h Incident Notification",
        mandate_description=(
            "Critical payment gateway systems must maintain >= 99.9% uptime SLA with Maximum Tolerable Downtime (MTD) <= 2 hours. "
            "Any Sev-1 cybersecurity disruption or transaction outage must be formally reported to the BOT Financial Surveillance Department within 24 hours."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติระบบการชำระเงิน พ.ศ. 2560 และประกาศ ธปท. ที่เกี่ยวข้อง",
            statute_name_en="Payment Systems Act B.E. 2560 (2017) & BOT Incident Notification Directives",
            section_or_clause="มาตรา 16 และมาตรา 34",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2017-10-18",
            gazette_reference="เล่ม 134 ตอนที่ 108 ก หน้า 1",
            official_source_url="https://www.bot.or.th/th/our-roles/payment-systems/regulations.html",
        ),
        severity="CRITICAL",
        enforcement_sanction="Fines up to ฿2,000,000 and daily fines up to ฿50,000 under Section 41 of the Payment Systems Act.",
        is_state_owned_bank_only=False,
    ),
]


def search_thai_fsi_regulatory_circulars(
    query_input: FSIRegulatoryQueryInput
) -> dict[str, Any]:
    """
    Searches Bank of Thailand statutory notifications, circulars, and primary banking laws.

    Exclusively targets Private Commercial Banks. Automatically detects and excludes
    state-owned bank (SFI) procurement queries.

    Args:
        query_input: Structured FSIRegulatoryQueryInput containing regulator, topic, and optional circular_code.

    Returns:
        Structured dictionary adhering to FSIRegulatorySearchResult schema or ToolErrorResponse schema.

    Raises:
        ValueError: If input payload fails fundamental Pydantic validation.
    """
    # 1. State-Owned Bank / Government Procurement Exclusion Gate
    sfi_keywords = ["จัดซื้อจัดจ้าง", "พัสดุภาครัฐ", "ebidding", "e-bidding", "สคร", "สตง", "ออมสิน", "ธกส", "ธอส", "sfi"]
    topic_lower = query_input.topic.lower()
    for kw in sfi_keywords:
        if kw in topic_lower:
            return handle_sfi_exclusion_error(query_input.topic)

    # 2. Regulator Mismatch Gate
    if query_input.regulator != "BOT":
        return build_guided_error_response(
            error_code="REGULATOR_MISMATCH",
            message=f"bot_tools only handles Bank of Thailand queries, but received '{query_input.regulator}'.",
            recovery_suggestion="Route SEC queries to sec_tools, OIC queries to oic_tools, and PDPA queries to pdpa_tools.",
            invalid_input_echo=query_input.model_dump()
        )

    # 3. Circular Code Direct Lookup
    if query_input.circular_code:
        normalized_code = query_input.circular_code.replace(" ", "").lower()
        matched = [
            m for m in BOT_MANDATES_REGISTRY
            if "12/2563" in normalized_code or "122563" in normalized_code
        ]
        if not matched:
            return handle_circular_lookup_error(query_input.circular_code, "BOT")
        return FSIRegulatorySearchResult(
            status="SUCCESS",
            regulator="BOT",
            topic=query_input.topic,
            matched_obligations=matched,
            total_found=len(matched)
        ).model_dump()

    # 4. Semantic Topic Filter
    results: list[RegulatoryObligation] = []
    keywords = query_input.topic.lower().split()
    for obligation in BOT_MANDATES_REGISTRY:
        match_score = sum(
            1 for kw in keywords
            if kw in obligation.title.lower() or kw in obligation.mandate_description.lower()
        )
        if match_score > 0 or any(k in query_input.topic.lower() for k in ["cloud", "it risk", "outsourcing", "payment", "ชำระเงิน"]):
            results.append(obligation)

    if not results:
        results = BOT_MANDATES_REGISTRY  # Default comprehensive return for broad FSI queries

    return FSIRegulatorySearchResult(
        status="SUCCESS",
        regulator="BOT",
        topic=query_input.topic,
        matched_obligations=results,
        total_found=len(results)
    ).model_dump()


def extract_fsi_cloud_outsourcing_mandates(
    cloud_service_type: str = "PaaS_or_SaaS"
) -> dict[str, Any]:
    """
    Extracts explicit contractual and operational clauses mandated by Bank of Thailand Notification SorNorSor. 12/2563.

    Args:
        cloud_service_type: Architecture tier ('IaaS', 'PaaS', 'SaaS', 'Generative_AI').

    Returns:
        Structured dictionary containing extracted contractual clauses and audit guidelines.
    """
    return {
        "regulator": "BOT",
        "notification": "สนส. 12/2563",
        "target_cloud_tier": cloud_service_type,
        "mandatory_contract_clauses": [
            {
                "clause_name": "Unrestricted Right to Audit (สิทธิการตรวจสอบ)",
                "statutory_ref": "สนส. 12/2563 ข้อ 5.2.2",
                "contract_language_requirement": (
                    "The Cloud Service Provider agrees to grant Bank internal audit, external audit, and Bank of Thailand examiners "
                    "full physical and logical access to inspect servers, configurations, logs, and cryptographic keys relevant to Bank data."
                ),
            },
            {
                "clause_name": "Chain-of-Custody & Fourth-Party Subcontracting (การจ้างช่วง)",
                "statutory_ref": "สนส. 12/2563 ข้อ 5.2.3",
                "contract_language_requirement": (
                    "The CSP shall not delegate, assign, or subcontract any primary processing of Bank data without prior written authorization from the Bank."
                ),
            },
            {
                "clause_name": "Data Sovereignty & Encryption at Rest (การคุ้มครองความปลอดภัย)",
                "statutory_ref": "สนส. 12/2563 ข้อ 4.3",
                "contract_language_requirement": (
                    "All Bank customer and transaction data must be encrypted in transit (TLS 1.3) and at rest with Customer-Managed Encryption Keys (CMEK)."
                ),
            },
        ],
        "exit_plan_criteria": "Minimum 90-day transition window, zero data lock-in, daily immutable data backup repatriation.",
    }
