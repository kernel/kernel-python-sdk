# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    limit: int
    """Maximum number of results to return"""

    offset: int
    """Number of results to skip"""

    query: str
    """Case-insensitive substring match against API key name, creator, and project.

    API key identifiers and masked keys match by exact value or prefix.
    """

    sort_by: Literal["created_at", "name", "expires_at"]
    """Field to sort API keys by."""

    sort_direction: Literal["asc", "desc"]
    """Sort direction for API keys."""
