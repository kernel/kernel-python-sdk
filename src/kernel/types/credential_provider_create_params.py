# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CredentialProviderCreateParams"]


class CredentialProviderCreateParams(TypedDict, total=False):
    token: Required[str]
    """Service account token for the provider (e.g., 1Password service account token)"""

    provider_type: Required[Literal["onepassword"]]
    """Type of credential provider"""

    cache_ttl_seconds: int
    """How long to cache credential lists (default 300 seconds)"""
