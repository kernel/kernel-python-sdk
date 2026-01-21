# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CredentialProviderUpdateParams"]


class CredentialProviderUpdateParams(TypedDict, total=False):
    token: str
    """New service account token (to rotate credentials)"""

    cache_ttl_seconds: int
    """How long to cache credential lists"""

    enabled: bool
    """Whether the provider is enabled for credential lookups"""

    priority: int
    """Priority order for credential lookups (lower numbers are checked first)"""
