"""
Strict Pydantic v2 schemas for tool inputs and outputs.
Enforces explicit validation, type safety, and constrained LLM generation.
"""

from typing import Any, Literal

from pydantic import BaseModel, Field

RegulatorType = Literal["BOT", "SEC", "OIC", "PDPC", "NCSA", "AI_GOVERNANCE", "ALL"]
EntityType = Literal["PRIVATE_COMMERCIAL_BANK", "FINANCIAL_CONGLOMERATE"]
LegalCategory = Literal["ACT", "ROYAL_DECREE", "MINISTERIAL_REGULATION", "NOTIFICATION", "CIRCULAR"]
SeverityLevel = Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]


class FSIRegulatoryQueryInput(BaseModel):
    """Input schema for querying Thai financial regulatory frameworks."""

    regulator: RegulatorType = Field(
        ...,
        description="Target Thai financial regulator: 'BOT' (Bank of Thailand), 'SEC' (Securities and Exchange Commission), 'OIC' (Office of Insurance Commission), or 'PDPC' (Personal Data Protection Commission)."
    )
    topic: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Specific regulatory topic or technical domain (e.g., 'Cloud Outsourcing', 'IT Risk Management', 'Cross-Border PII Transfer', 'Bancassurance Cyber Resilience')."
    )
    circular_code: str | None = Field(
        None,
        description="Optional official circular or notification code (e.g., 'สนส. 12/2563', 'กธว. 1/2565')."
    )
    entity_scope: EntityType = Field(
        default="PRIVATE_COMMERCIAL_BANK",
        description="Target regulated entity tier. Strictly defaults to 'PRIVATE_COMMERCIAL_BANK'."
    )


class StatutoryCitation(BaseModel):
    """Schema representing an official statutory citation in Thailand."""

    statute_name_th: str = Field(..., description="Official statute title in Thai script.")
    statute_name_en: str = Field(..., description="Official statute title in English.")
    section_or_clause: str = Field(..., description="Specific Section (มาตรา), Clause (ข้อ), or Annex (ภาคผนวก).")
    issuing_authority: str = Field(..., description="Issuing regulatory body (e.g., Bank of Thailand).")
    enactment_date: str = Field(..., description="Date enacted or published in Royal Thai Government Gazette.")
    gazette_reference: str | None = Field(None, description="Official Gazette reference (Volume, Part, Page).")
    official_source_url: str = Field(..., description="Verified direct URL on official .go.th or .or.th domain.")


class RegulatoryObligation(BaseModel):
    """Schema detailing an enforceable operational or technical compliance mandate."""

    obligation_id: str = Field(..., description="Unique obligation identifier (e.g., 'OBL-BOT-122563-01').")
    title: str = Field(..., description="Summary title of the statutory mandate.")
    mandate_description: str = Field(..., description="Exact technical or operational obligation required.")
    statutory_citation: StatutoryCitation = Field(..., description="Primary legal citation anchoring this mandate.")
    severity: SeverityLevel = Field(..., description="Statutory non-compliance severity tier.")
    enforcement_sanction: str = Field(..., description="Statutory penalty or sanction for non-compliance.")
    is_state_owned_bank_only: bool = Field(
        default=False,
        description="Flag indicating if the regulation applies exclusively to State-Owned Banks (SFIs). Must be False for private bank scope."
    )


class FSIRegulatorySearchResult(BaseModel):
    """Schema representing structured results from regulatory search tools."""

    status: Literal["SUCCESS", "EXCLUDED", "NOT_FOUND"] = Field(..., description="Execution status.")
    regulator: RegulatorType = Field(..., description="Target regulator queried.")
    topic: str = Field(..., description="Queried regulatory domain.")
    matched_obligations: list[RegulatoryObligation] = Field(default_factory=list, description="List of matched statutory obligations.")
    total_found: int = Field(default=0, description="Total matching obligations identified.")
    exclusion_reason: str | None = Field(None, description="Detailed explanation if query was excluded (e.g. SFI/Government procurement exclusion).")


class GRCControlMapping(BaseModel):
    """Schema mapping a statutory mandate into an actionable enterprise GRC control."""

    control_id: str = Field(..., description="Enterprise control ID format 'CO-REG-TH-FSI-###'.")
    control_objective: str = Field(..., description="High-level policy control objective.")
    implementation_spec: str = Field(..., description="Concrete architectural or technical control specification.")
    evidence_artifact: str = Field(..., description="Mandatory audit evidence required for regulatory examination.")
    statutory_anchor: str = Field(..., description="Direct citation string format '[Grounded: ...]'.")


class GRCSynthesisResult(BaseModel):
    """Output schema for the final cross-regulatory compliance synthesis."""

    status: Literal["SUCCESS", "AWAITING_HUMAN_CONFIRMATION"] = Field(..., description="Synthesis execution status.")
    bank_scope: str = Field(default="Private Commercial Bank & Consolidated Financial Group", description="Regulated entity scope.")
    harmonized_controls: list[GRCControlMapping] = Field(default_factory=list, description="Synthesized enterprise controls.")
    statutory_conflicts: list[str] = Field(default_factory=list, description="Any identified cross-regulatory tensions or overlaps.")
    executive_summary: str = Field(..., description="Bilingual high-level compliance verdict for Chief Risk Officer / Board.")
    requires_hitl_approval: bool = Field(default=False, description="Flag indicating if a high-stakes confirmation gate is triggered.")
    hitl_action_details: dict[str, Any] | None = Field(None, description="Details of the high-stakes action awaiting confirmation.")


class ToolErrorResponse(BaseModel):
    """Structured error payload providing guided recovery instructions to LLMs."""

    status: Literal["ERROR"] = "ERROR"
    error_code: str = Field(..., description="Standardized error code (e.g. 'REGULATOR_API_TIMEOUT', 'INVALID_CIRCULAR_CODE').")
    message: str = Field(..., description="Human-readable description of what failed.")
    recovery_suggestion: str = Field(..., description="Actionable instruction guiding the LLM on how to recover without crashing.")
    invalid_input_echo: dict[str, Any] | None = Field(None, description="Echo of the input arguments that triggered the error.")
