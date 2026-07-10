# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CredentialListParams"]


class CredentialListParams(TypedDict, total=False):
    domain: str
    """Filter by domain"""

    limit: int
    """Maximum number of results to return"""

    offset: int
    """Number of results to skip"""

    query: str
    """Case-insensitive substring match against credential name or domain.

    IDs match by exact value.
    """
