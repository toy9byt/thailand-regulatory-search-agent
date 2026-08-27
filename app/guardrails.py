"""
Guardrails and Human-in-the-Loop (HITL) Policy Enforcement Module.
Implements pre-execution input filters, post-execution statutory grounding verifiers,
and explicit code stops for high-stakes actions (Category 3.3 & Category 3.4).
"""

import re
from typing import Any, ClassVar


class InputGuardrail:
    """Pre-execution security and scope policy guardrail."""

    SFI_KEYWORDS: ClassVar[list[str]] = [
        "จัดซื้อจัดจ้าง", "พัสดุภาครัฐ", "ebidding", "e-bidding",
        "สคร", "สตง", "ออมสิน", "ธกส", "ธอส", "sme bank", "exim bank",
        "state-owned bank", "sfi"
    ]

    INJECTION_PATTERNS: ClassVar[list[str]] = [
        r"ignore (all )?previous instructions",
        r"system prompt override",
        r"you are now in developer mode",
        r"disregard (the )?constitution",
    ]

    @classmethod
    def validate_input(cls, user_prompt: str) -> tuple[bool, str | None, str | None]:
        """
        Validates prompt against prompt injection and ensures strict private commercial banking scope.

        Returns:
            Tuple of (is_valid, error_code, rejection_reason).
        """
        prompt_lower = user_prompt.lower()

        # 1. Prompt Injection Defense
        for pattern in cls.INJECTION_PATTERNS:
            if re.search(pattern, prompt_lower):
                return (
                    False,
                    "SECURITY_INJECTION_DETECTED",
                    "Input rejected: Prompt contains unauthorized instructions attempting to alter system guardrails."
                )

        # 2. SFI / Government Procurement Exclusion Gate
        for kw in cls.SFI_KEYWORDS:
            if kw in prompt_lower:
                return (
                    False,
                    "SFI_SCOPE_EXCLUDED",
                    (
                        f"Input rejected: Topic pertains to State-Owned Enterprise Banks (SFIs) or Government Procurement ('{kw}'). "
                        "This system strictly enforces Private Commercial Banking scope under the Financial Institutions Businesses Act B.E. 2551."
                    )
                )

        return (True, None, None)


class OutputGuardrail:
    """Post-execution statutory grounding and compliance verifier."""

    GROUNDING_PATTERN = r"\[Grounded:\s*[^\]]+\]"

    @classmethod
    def verify_grounding(cls, output_text: str) -> tuple[bool, str | None]:
        """
        Verifies that every generated compliance claim contains at least one statutory grounding anchor.
        """
        matches = re.findall(cls.GROUNDING_PATTERN, output_text)
        if not matches:
            return (
                False,
                "UNGROUNDED_OUTPUT: Generated report fails 100% Grounding Mandate. Missing official statutory citations."
            )
        return (True, None)


class HumanInTheLoopHook:
    """
    Explicit confirmation stop requiring human supervisor approval before executing high-stakes actions.
    """

    HIGH_STAKES_TRIGGERS: ClassVar[list[str]] = [
        "SUBMIT_INCIDENT_NOTIFICATION_BOT",
        "REPORT_DATA_BREACH_PDPC",
        "COMMIT_POLICY_AMENDMENT_BOARD",
        "REVOKE_CLOUD_SERVICE_PROVIDER_CONTRACT",
    ]

    @classmethod
    def evaluate_action(
        cls,
        action_name: str,
        parameters: dict[str, Any],
        confirmed_by_user: bool = False
    ) -> dict[str, Any]:
        """
        Intercepts high-stakes actions and mandates human digital confirmation before proceeding.

        Args:
            action_name: Machine-readable identifier for the action.
            parameters: Action payload and blast radius details.
            confirmed_by_user: Boolean flag indicating if human user has provided explicit sign-off.

        Returns:
            Dict indicating whether execution is approved or paused for confirmation.
        """
        if action_name in cls.HIGH_STAKES_TRIGGERS and not confirmed_by_user:
            return {
                "status": "AWAITING_HUMAN_CONFIRMATION",
                "action": action_name,
                "severity": "CRITICAL",
                "blast_radius": f"Executing '{action_name}' triggers legally binding regulatory disclosures or material contractual impacts.",
                "required_action": "Senior Executive / Compliance Officer explicit confirmation is legally mandated before dispatch.",
                "payload_preview": parameters,
            }

        return {
            "status": "APPROVED_FOR_EXECUTION",
            "action": action_name,
            "confirmed_by_user": True,
        }
