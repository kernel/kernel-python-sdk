# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .api_key import APIKey

__all__ = ["CreatedAPIKey"]


class CreatedAPIKey(APIKey):
    """API key returned immediately after creation. Includes the plaintext key once."""

    key: str
    """Plaintext API key. Only returned once when the key is created."""
