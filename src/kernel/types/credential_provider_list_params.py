# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CredentialProviderListParams"]


class CredentialProviderListParams(TypedDict, total=False):
    limit: int
    """Limit the number of credential providers to return."""

    offset: int
    """Offset the number of credential providers to return."""

    query: str
    """Search credential providers by name or ID."""
