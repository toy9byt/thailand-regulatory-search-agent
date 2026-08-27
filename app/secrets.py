"""
Secure Secret Management Module.
Integrates with Google Cloud Secret Manager for dynamic credential injection
with strict zero-hardcoded-secret enforcement (Category 5.3).
"""

import logging
import os


class SecretManagerClient:
    """
    Secure Secret Manager client wrapping Google Cloud Secret Manager API
    with local environment variable fallback for development environments.
    """

    def __init__(self, project_id: str | None = None):
        self.project_id = project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
        self.logger = logging.getLogger("SecretManagerClient")

    def get_secret(self, secret_id: str, default_value: str | None = None) -> str | None:
        """
        Retrieves secret payload from Secret Manager or environment variable.

        Args:
            secret_id: Identifier of the secret (e.g., 'GEMINI_API_KEY').
            default_value: Optional fallback if secret is not set.

        Returns:
            Resolved secret string.
        """
        # 1. First priority: Direct Environment Variable (standard 12-factor pattern)
        env_val = os.getenv(secret_id)
        if env_val:
            return env_val

        # 2. Second priority: Google Cloud Secret Manager if client library available
        if self.project_id:
            try:
                from google.cloud import secretmanager
                client = secretmanager.SecretManagerServiceClient()
                name = f"projects/{self.project_id}/secrets/{secret_id}/versions/latest"
                response = client.access_secret_version(request={"name": name})
                return response.payload.data.decode("UTF-8")
            except (ImportError, OSError, RuntimeError, ValueError) as exc:
                self.logger.debug("Falling back from Secret Manager: %s", exc)

        return default_value
