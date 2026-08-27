"""
Guided Error Handling module.
Converts exceptions and invalid arguments into structured, self-healing recovery instructions for LLMs.
"""

from typing import Any

from .schemas import ToolErrorResponse


def build_guided_error_response(
    error_code: str,
    message: str,
    recovery_suggestion: str,
    invalid_input_echo: dict[str, Any] | None = None
) -> dict[str, Any]:
    """
    Constructs a structured ToolErrorResponse dictionary guiding the LLM to self-correct.

    Args:
        error_code: Machine-readable uppercase token indicating failure classification.
        message: Plain-language diagnostic explanation of the issue.
        recovery_suggestion: Step-by-step guidance enabling the LLM to repair its tool call.
        invalid_input_echo: Optional capture of the inputs that triggered the failure.

    Returns:
        Dictionary adhering strictly to ToolErrorResponse schema.
    """
    error_payload = ToolErrorResponse(
        status="ERROR",
        error_code=error_code,
        message=message,
        recovery_suggestion=recovery_suggestion,
        invalid_input_echo=invalid_input_echo or {}
    )
    return error_payload.model_dump()


def handle_circular_lookup_error(circular_code: str, regulator: str) -> dict[str, Any]:
    """Handles malformed or missing circular code lookups."""
    return build_guided_error_response(
        error_code="CIRCULAR_NOT_FOUND",
        message=f"Circular identifier '{circular_code}' was not found under regulator '{regulator}'.",
        recovery_suggestion=(
            "Please verify the circular notation. For Bank of Thailand (BOT), valid formats include 'สนส. 12/2563' or 'SorNorSor. 12/2563'. "
            "If uncertain, query without 'circular_code' and provide a topic keyword (e.g. topic='Cloud Outsourcing') to search by semantic intent."
        ),
        invalid_input_echo={"circular_code": circular_code, "regulator": regulator}
    )


def handle_sfi_exclusion_error(statute_or_topic: str) -> dict[str, Any]:
    """Handles queries inadvertently requesting state-owned enterprise bank / SFI rules."""
    return build_guided_error_response(
        error_code="SFI_REGULATION_EXCLUDED",
        message=f"The requested topic or statute '{statute_or_topic}' pertains to State-Owned Enterprise Banks (SFIs) or Government Procurement.",
        recovery_suggestion=(
            "This agent strictly enforces Private Commercial Banking scope under the Financial Institutions Businesses Act B.E. 2551. "
            "Please reformulate your inquiry focusing on private commercial banking mandates under BOT (e.g. สนส. 12/2563 for private cloud outsourcing), "
            "SEC cyber resilience, OIC InsurTech, or PDPA data privacy."
        ),
        invalid_input_echo={"query": statute_or_topic}
    )


def handle_regulator_mismatch_error(regulator: str, topic: str) -> dict[str, Any]:
    """Handles querying a regulator for a jurisdiction they do not govern."""
    return build_guided_error_response(
        error_code="REGULATORY_JURISDICTION_MISMATCH",
        message=f"The requested regulator '{regulator}' does not have statutory jurisdiction over '{topic}'.",
        recovery_suggestion=(
            "Verify the regulatory mapping: Use 'BOT' for Banking IT Risk & Payments; 'SEC' for Capital Markets, Trading & Digital Assets; "
            "'OIC' for Insurance & Bancassurance; and 'PDPC' for Personal Data Protection Act compliance across all sectors."
        ),
        invalid_input_echo={"regulator": regulator, "topic": topic}
    )
