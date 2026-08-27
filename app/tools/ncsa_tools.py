"""
National Cyber Security Agency (NCSA / สกมช.) Statutory Compliance Tools.
Specialized in Cybersecurity Act B.E. 2562 (พ.ร.บ. การรักษาความมั่นคงปลอดภัยไซเบอร์ พ.ศ. 2562),
Critical Information Infrastructure (CII) Data Center Standards, and Incident Notification.
"""

from typing import Any

from .error_handler import (
    handle_circular_lookup_error,
    handle_sfi_exclusion_error,
)
from .schemas import (
    FSIRegulatoryQueryInput,
    FSIRegulatorySearchResult,
    RegulatoryObligation,
    StatutoryCitation,
)

# Canonical In-Memory Knowledge Store for NCSA Cybersecurity Act Mandates
NCSA_CYBER_MANDATES_REGISTRY: list[RegulatoryObligation] = [
    RegulatoryObligation(
        obligation_id="OBL-NCSA-CII-01",
        title="Data Center Critical Information Infrastructure (CII) Cybersecurity Baseline Standards",
        mandate_description=(
            "Data Centers and cloud facilities hosting mission-critical financial systems are legally designated as "
            "Critical Information Infrastructure (CII) under the Financial and Banking sector and IT/Telecom sector. "
            "Must maintain strict physical and digital cybersecurity controls: biometric physical access, dual-power redundancy, "
            "environmental protection, and continuous CCTV surveillance with minimum 90-day retention."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติการรักษาความมั่นคงปลอดภัยไซเบอร์ พ.ศ. 2562 มาตรา 49 และ มาตรา 50 ร่วมกับ ประกาศ กมช. เรื่อง ประมวลแนวทางปฏิบัติและกรอบมาตรฐานด้านการรักษาความมั่นคงปลอดภัยไซเบอร์สำหรับหน่วยงาน CII พ.ศ. 2564",
            statute_name_en="Cybersecurity Act B.E. 2562 Sections 49 & 50 and NCSA Notification on CII Baseline Cybersecurity Framework B.E. 2564",
            section_or_clause="มาตรา 49 และ มาตรา 50 (การกำหนดมาตรฐานความมั่นคงปลอดภัยไซเบอร์ของหน่วยงาน CII)",
            issuing_authority="National Cyber Security Agency (สำนักงานคณะกรรมการการรักษาความมั่นคงปลอดภัยไซเบอร์แห่งชาติ - สกมช.)",
            enactment_date="2019-05-27",
            gazette_reference="เล่ม 136 ตอนที่ 69 ก หน้า 20",
            official_source_url="https://www.ncsa.or.th/law-regulation/cybersecurity-act-2562/",
        ),
        severity="CRITICAL",
        enforcement_sanction="Administrative orders, public supervisory disclosure, operational suspension, and criminal penalties under Chapter 7 of Cybersecurity Act.",
        remediation_actions=[
            "Designate Data Centers and Cloud hosting facilities under the official CII Registry with NCSA.",
            "Enforce Tier III / Tier IV power and cooling redundancy and 24/7 biometric physical access control.",
            "Establish unified Security Operations Center (SOC) monitoring network telemetry and server logs."
        ],
        audit_evidence_requirements=[
            "Official NCSA CII Registration Certificate.",
            "Data Center physical access logs and biometric verification records (retained >= 90 days).",
            "ISO/IEC 27001, ISO 22301, and SOC 2 Type II compliance certificates."
        ],
    ),
    RegulatoryObligation(
        obligation_id="OBL-NCSA-CII-02",
        title="Critical Cyber Threat Incident Notification within 24 Hours (NCSA & T-B CERT)",
        mandate_description=(
            "When a Critical or Serious Cyber Threat impacts a financial Data Center, core banking switch, or cloud workload "
            "(e.g., ransomware outage, core network DDoS, or mass credential breach), the regulated entity must notify "
            "the National Cyber Security Agency (NCSA) and the Sectoral CERT (Thailand Banking Sector CERT / T-B CERT) "
            "immediately and without delay, and not later than 24 hours from incident detection."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติการรักษาความมั่นคงปลอดภัยไซเบอร์ พ.ศ. 2562 มาตรา 53 และ มาตรา 73 ร่วมกับ ประกาศ สกมช. เรื่อง หลักเกณฑ์ วิธีการ และเงื่อนไขในการแจ้งเหตุภัยคุกคามทางไซเบอร์ พ.ศ. 2564",
            statute_name_en="Cybersecurity Act B.E. 2562 Sections 53 & 73: Mandatory Incident Notification Protocols",
            section_or_clause="มาตรา 53 (การแจ้งเหตุภัยคุกคามทางไซเบอร์)",
            issuing_authority="National Cyber Security Agency (สกมช.) & T-B CERT",
            enactment_date="2021-12-14",
            gazette_reference="เล่ม 138 ตอนพิเศษ 304 ง หน้า 18",
            official_source_url="https://www.ncsa.or.th/incident-reporting-criteria/",
        ),
        severity="CRITICAL",
        enforcement_sanction="Administrative fine up to 200,000 THB plus 10,000 THB per day of ongoing delay under Section 73 of Cybersecurity Act.",
        remediation_actions=[
            "Configure automated P1/Sev-1 incident escalation playbooks notifying NCSA and T-B CERT within 24 hours.",
            "Establish direct hotlines and encrypted communication channels with NCSA Incident Response Team.",
            "Conduct post-incident root-cause analysis (RCA) within 30 calendar days."
        ],
        audit_evidence_requirements=[
            "Incident Response Plan (IRP) detailing statutory 24-hour notification protocol.",
            "Sample incident notification dispatch receipts and timestamps.",
            "T-B CERT coordination and liaison records."
        ],
    ),
    RegulatoryObligation(
        obligation_id="OBL-NCSA-CII-03",
        title="Annual Independent Cybersecurity Audit & Data Center Risk Assessment",
        mandate_description=(
            "Financial institutions and their critical Data Center facilities must undergo an annual cybersecurity "
            "risk assessment and independent audit conducted by a certified external auditor (e.g., CISA, CISSP, ISO Lead Auditor). "
            "The completed audit report and management remediation response must be submitted to NCSA within 30 days of completion."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติการรักษาความมั่นคงปลอดภัยไซเบอร์ พ.ศ. 2562 มาตรา 50(2) และ มาตรา 54",
            statute_name_en="Cybersecurity Act B.E. 2562 Section 50(2) & 54: Independent Cybersecurity Audit",
            section_or_clause="มาตรา 50(2) (การประเมินความเสี่ยงและการตรวจสอบด้านความมั่นคงปลอดภัยไซเบอร์โดยผู้ตรวจสอบอิสระ)",
            issuing_authority="National Cyber Security Agency (สำนักงานคณะกรรมการการรักษาความมั่นคงปลอดภัยไซเบอร์แห่งชาติ - สกมช.)",
            enactment_date="2019-05-27",
            gazette_reference="เล่ม 136 ตอนที่ 69 ก หน้า 21",
            official_source_url="https://www.ncsa.or.th/law-regulation/cybersecurity-act-2562/",
        ),
        severity="HIGH",
        enforcement_sanction="Administrative penalty up to 300,000 THB and formal supervisory audit notice under Section 74.",
        remediation_actions=[
            "Commission annual third-party independent cybersecurity audit across on-premise and colocation Data Centers.",
            "Track all high and critical audit vulnerabilities in an automated JIRA/ServiceNow remediation workflow.",
            "Submit the annual audit report to NCSA and Bank of Thailand within the statutory 30-day window."
        ],
        audit_evidence_requirements=[
            "Independent Cybersecurity Audit Report signed by a certified Lead Auditor.",
            "Official NCSA transmittal letter confirming submission within 30 days.",
            "Executive Management Remediation Plan for identified vulnerabilities."
        ],
    ),
]


def search_thai_fsi_cybersecurity_act_mandates(
    query_input: FSIRegulatoryQueryInput
) -> dict[str, Any]:
    """
    Searches statutory obligations under the Thailand Cybersecurity Act B.E. 2562 (พ.ร.บ. ไซเบอร์),
    specifically addressing Data Centers, Critical Information Infrastructure (CII), and 24-hour threat notification.
    """
    topic_lower = query_input.topic.lower()

    # Pre-execution SFI rejection filter
    sfi_keywords = ["จัดซื้อจัดจ้าง", "พัสดุภาครัฐ", "ebidding", "สคร", "สตง", "ออมสิน", "ธกส", "ธอส"]
    for kw in sfi_keywords:
        if kw in topic_lower:
            return handle_sfi_exclusion_error(
                entity_name="Inquired State-Owned Entity",
                prohibited_keyword=kw
            )

    results: list[RegulatoryObligation] = []
    keywords = topic_lower.split()

    for obligation in NCSA_CYBER_MANDATES_REGISTRY:
        text_corpus = (
            f"{obligation.title} {obligation.mandate_description} "
            f"{obligation.statutory_citation.statute_name_th} {obligation.statutory_citation.statute_name_en}"
        ).lower()

        if any(kw in text_corpus for kw in keywords) or not keywords or query_input.topic == "ALL":
            results.append(obligation)

    if not results:
        return handle_circular_lookup_error(
            circular_code="CYBERSECURITY_ACT_CII",
            available_circulars=["OBL-NCSA-CII-01", "OBL-NCSA-CII-02", "OBL-NCSA-CII-03"]
        )

    search_result = FSIRegulatorySearchResult(
        status="SUCCESS",
        regulator="NCSA",
        topic=query_input.topic,
        matched_obligations=results,
        total_found=len(results),
    )

    return {
        "status": "SUCCESS",
        "regulator": "NCSA_CYBERSECURITY_ACT",
        "matched_obligations": [o.model_dump() for o in search_result.matched_obligations],
        "grounded_citation_summary": [
            f"[Grounded: {o.statutory_citation.statute_name_en}, {o.statutory_citation.section_or_clause}, {o.statutory_citation.issuing_authority}]"
            for o in search_result.matched_obligations
        ],
    }
