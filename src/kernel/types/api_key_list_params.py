# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    include_deleted: bool
    """Deprecated: use status=all instead.

    When true, include deleted (soft-deleted) API keys in the results for audit
    purposes.
    """

    limit: int
    """Maximum number of results to return"""

    name: str
    """Exact-match filter on API key name using the database collation.

    In production, matching is case- and accent-insensitive. Names are not required
    to be unique, so multiple keys may match. When status=all or
    include_deleted=true is set, soft-deleted keys with the same name may also
    match.
    """

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

    status: Literal["active", "deleted", "all"]
    """Filter API keys by status.

    "active" returns keys that are not deleted (default; expired-but-not-deleted
    keys are still included), "deleted" returns only soft-deleted keys, "all"
    returns both.
    """
