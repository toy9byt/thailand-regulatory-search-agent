"""
Thailand Financial Services Industry (FSI) AI Governance & Ethical AI Tools.
Covers Bank of Thailand (BOT) AI/ML Financial Guidelines, ETDA Thailand AI Governance Clinic (AIGC),
and PDPA Automated Decision-Making (ADM) statutory mandates.
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

# Canonical Registry for Thai FSI AI Governance Mandates
AI_GOVERNANCE_MANDATES_REGISTRY: list[RegulatoryObligation] = [
    RegulatoryObligation(
        obligation_id="OBL-BOT-AI-01",
        title="BOT AI/ML Explainability & Transparency Mandate (Non-Black Box)",
        mandate_description=(
            "Financial institutions utilizing Artificial Intelligence and Machine Learning (AI/ML) models "
            "for retail credit underwriting, risk assessment, or customer advisory must ensure algorithmic explainability. "
            "Pure black-box models without interpretable decision logic (e.g., SHAP, LIME, or feature attribution) "
            "are prohibited for critical financial determinations; institutions must be capable of providing clear reasons for adverse decisions."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="แนวทางการประยุกต์ใช้ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง (AI/ML) ในภาคการเงิน ธนาคารแห่งประเทศไทย และ ประกาศ สนส. 12/2563",
            statute_name_en="Bank of Thailand Guidelines on the Use of Artificial Intelligence and Machine Learning (AI/ML) in Financial Services",
            section_or_clause="หมวด 3 ความโปร่งใสและความสามารถในการอธิบาย (Transparency & Explainability)",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2022-09-15",
            gazette_reference="BOT Consultation Paper & IT Risk Supervisory Letter",
            official_source_url="https://www.bot.or.th/en/our-roles/financial-markets/fintech-and-innovation/ai-ml-in-financial-sector.html",
        ),
        severity="HIGH",
        enforcement_sanction="Order to halt automated credit model operations, mandatory model re-calibration, and supervisory audit under Financial Institutions Businesses Act.",
        remediation_actions=[
            "Implement model explainability layers (SHAP / Integrated Gradients) generating customer-readable decision summaries.",
            "Establish adverse action notice templates citing dominant explanatory features for loan denials.",
            "Prohibit opaque black-box neural networks for automated lending without verifiable feature attribution."
        ],
        audit_evidence_requirements=[
            "Model Explainability Architecture Specification and validation methodology.",
            "Sample adverse credit determination audit records demonstrating interpretable rationales.",
            "Board Risk Committee approval of explainability standards."
        ],
    ),
    RegulatoryObligation(
        obligation_id="OBL-BOT-AI-02",
        title="BOT Fairness & Anti-Bias Mandate in Algorithmic Credit Underwriting",
        mandate_description=(
            "Commercial banks using Alternative Data and automated AI algorithms must conduct rigorous statistical bias audits. "
            "Algorithms must not discriminate against applicants on the basis of gender, race, religion, disability, "
            "or socioeconomic geographic proxy attributes, adhering to BOT Market Conduct standards."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="เกณฑ์การบริหารจัดการด้านการให้บริการแก่ลูกค้าอย่างเป็นธรรม (Market Conduct) และหลักการ AI/ML ธนาคารแห่งประเทศไทย",
            statute_name_en="Bank of Thailand Market Conduct Regulations & AI/ML Fairness Principles",
            section_or_clause="หมวด 2 ความเป็นธรรมและการไม่เลือกปฏิบัติ (Fairness & Non-Discrimination)",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2022-09-15",
            gazette_reference="BOT Directional Guidelines on Fair Digital Lending",
            official_source_url="https://www.bot.or.th/en/rules-and-regulations/market-conduct.html",
        ),
        severity="CRITICAL",
        enforcement_sanction="Regulatory sanctions, mandatory compensation for affected customer classes, and suspension of digital personal loan licenses.",
        remediation_actions=[
            "Conduct disparate impact and demographic parity audits across model training datasets.",
            "Remove proxy attributes correlated with protected personal characteristics.",
            "Establish automated bias alert thresholds triggering manual human underwriter review."
        ],
        audit_evidence_requirements=[
            "Disparate impact statistical analysis reports signed by Chief Risk Officer.",
            "Feature importance correlation matrix excluding protected demographic proxies.",
            "Annual algorithmic fairness audit reports."
        ],
    ),
    RegulatoryObligation(
        obligation_id="OBL-BOT-AI-03",
        title="Model Risk Management (MRM), Validation & Concept Drift Control",
        mandate_description=(
            "Commercial banks must establish independent Model Risk Management (MRM) frameworks governing the entire AI lifecycle. "
            "Pre-deployment stress testing, continuous monitoring of data/concept drift, and automated triggers "
            "for model retraining are mandatory to ensure stability and resilience under stressed market conditions."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2563 เรื่อง การบริหารความเสี่ยงด้าน IT และแนวปฏิบัติ Model Risk Management",
            statute_name_en="Bank of Thailand Notification SorNorSor. 12/2563 IT Risk Governance & Model Risk Management Standards",
            section_or_clause="ข้อ 4.3 (การบริหารความเสี่ยงด้านแบบจำลองทางการเงินและ AI)",
            issuing_authority="Bank of Thailand (ธนาคารแห่งประเทศไทย)",
            enactment_date="2020-07-31",
            gazette_reference="เล่ม 137 ตอนพิเศษ 188 ง หน้า 14",
            official_source_url="https://www.bot.or.th/content/dam/bot/documents/laws-and-regulations/fipm/SorNorSor12-2563.pdf",
        ),
        severity="HIGH",
        enforcement_sanction="Capital charge add-on for model risk, mandatory parallel legacy run, and supervisory notice.",
        remediation_actions=[
            "Establish dedicated Independent Model Validation (IMV) unit separate from model developers.",
            "Implement real-time monitoring of model drift (Population Stability Index / PSI > 0.25 triggers recalibration).",
            "Perform semi-annual adversarial stress testing and backtesting against historical downturn data."
        ],
        audit_evidence_requirements=[
            "Independent Model Validation (IMV) Sign-off Document prior to production deployment.",
            "Automated Model Drift dashboards with automated alert logs.",
            "Documented model rollback and failover contingency procedures."
        ],
    ),
    RegulatoryObligation(
        obligation_id="OBL-ETDA-AIGC-01",
        title="National AI Governance Framework (ETDA AIGC Executive Guidelines)",
        mandate_description=(
            "Enterprise organizations deploying Artificial Intelligence in Thailand should align with the National AI Governance Framework "
            "established by the Electronic Transactions Development Agency (ETDA Thailand AI Governance Clinic). "
            "Mandates risk-tiering assessment, transparent AI identity disclosure to consumers, robust data provenance tracking, "
            "and Human-in-the-Loop (HITL) oversight for high-impact automated operations."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="แนวทางการประยุกต์ใช้ปัญญาประดิษฐ์อย่างมีธรรมาภิบาลสำหรับผู้บริหารองค์กร (AI Governance Guidelines for Executives) โดย สพธอ. (ETDA)",
            statute_name_en="ETDA Thailand AI Governance Clinic (AIGC) Framework & Executive Guidelines",
            section_or_clause="เสาหลักที่ 1-4 (Strategy, Governance, Risk Management & Operations)",
            issuing_authority="Electronic Transactions Development Agency (สำนักงานพัฒนาธุรกรรมทางอิเล็กทรอนิกส์ - ETDA)",
            enactment_date="2023-11-20",
            gazette_reference="ETDA AIGC Publication No. 1/2566",
            official_source_url="https://www.etda.or.th/th/aigc.aspx",
        ),
        severity="HIGH",
        enforcement_sanction="Public enterprise audit scrutiny, loss of National Trustmark certification, and referral to sectoral regulators for non-compliance.",
        remediation_actions=[
            "Conduct AI system risk tiering (categorizing high-impact customer-facing systems).",
            "Implement clear disclosure informing consumers whenever interacting with conversational AI or synthetic media.",
            "Establish Human-in-the-Loop (HITL) approval gates for actions with significant financial or legal impact."
        ],
        audit_evidence_requirements=[
            "Enterprise AI Governance Policy ratified by Executive Committee.",
            "AI System Inventory & Risk Categorization Register.",
            "Consumer AI Interaction Disclosure logs and consent records."
        ],
    ),
    RegulatoryObligation(
        obligation_id="OBL-PDPC-AI-01",
        title="PDPA Automated Decision-Making (ADM) & Right to Human Intervention",
        mandate_description=(
            "Under PDPA B.E. 2562, data subjects have the right to receive meaningful information regarding the logic involved "
            "in automated profiling or algorithmic decision-making that significantly affects them. Data subjects retain the right "
            "to object to automated processing and demand human review of automated credit, insurance, or profiling verdicts."
        ),
        statutory_citation=StatutoryCitation(
            statute_name_th="พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA) มาตรา 30 และ มาตรา 37",
            statute_name_en="Personal Data Protection Act B.E. 2562 (PDPA) Sections 30 & 37 (Automated Profiling)",
            section_or_clause="มาตรา 30 (สิทธิในการคัดค้านและการขอให้ทบทวนการตัดสินใจโดยระบบอัตโนมัติ)",
            issuing_authority="Personal Data Protection Commission (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล - สคส.)",
            enactment_date="2019-05-27",
            gazette_reference="เล่ม 136 ตอนที่ 69 ก หน้า 33",
            official_source_url="https://www.pdpc.or.th/wp-content/uploads/2021/04/PDPA-2562.pdf",
        ),
        severity="HIGH",
        enforcement_sanction="Administrative fines up to 5,000,000 THB, punitive damages under civil law, and corrective remediation orders.",
        remediation_actions=[
            "Embed clear mechanism enabling data subjects to request manual human review of automated decisions.",
            "Update Privacy Notices to explicitly disclose AI profiling parameters and logic.",
            "Maintain operational runbooks for DPO to process automated decision objection requests within statutory timelines."
        ],
        audit_evidence_requirements=[
            "Customer-facing Automated Profiling Disclosure and Privacy Policy.",
            "DPO Workflow for processing Automated Decision-Making objection tickets.",
            "Log of human review overrides and manual underwriting verifications."
        ],
    ),
]


def search_thai_fsi_ai_governance_mandates(
    query_input: FSIRegulatoryQueryInput
) -> dict[str, Any]:
    """
    Searches statutory and regulatory mandates governing AI/ML in Thailand FSI,
    including Bank of Thailand AI/ML Principles, ETDA National AI Governance, and PDPA Automated Decision-Making.
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

    for obligation in AI_GOVERNANCE_MANDATES_REGISTRY:
        text_corpus = (
            f"{obligation.title} {obligation.mandate_description} "
            f"{obligation.statutory_citation.statute_name_th} {obligation.statutory_citation.statute_name_en}"
        ).lower()

        if any(kw in text_corpus for kw in keywords) or not keywords or query_input.topic == "ALL":
            results.append(obligation)

    if not results:
        return handle_circular_lookup_error(
            circular_code="AI_GOVERNANCE",
            available_circulars=["OBL-BOT-AI-01", "OBL-BOT-AI-02", "OBL-BOT-AI-03", "OBL-ETDA-AIGC-01", "OBL-PDPC-AI-01"]
        )

    search_result = FSIRegulatorySearchResult(
        status="SUCCESS",
        regulator="AI_GOVERNANCE",
        topic=query_input.topic,
        matched_obligations=results,
        total_found=len(results),
    )

    return {
        "status": "SUCCESS",
        "regulator": "BOT_ETDA_PDPC_AI_GOVERNANCE",
        "matched_obligations": [o.model_dump() for o in search_result.matched_obligations],
        "grounded_citation_summary": [
            f"[Grounded: {o.statutory_citation.statute_name_en}, {o.statutory_citation.section_or_clause}, {o.statutory_citation.issuing_authority}]"
            for o in search_result.matched_obligations
        ],
    }
