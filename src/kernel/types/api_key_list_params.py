# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    created_by: str
    """Return only keys created by this user ID.

    This is the same person the key's created_by field describes.
    """

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

    principal_type: Literal["user", "service_account"]
    """
    Return only keys that act as a user, or only keys that act as a service account.
    """

    project_id: str
    """Return only keys scoped to this project ID.

    The value "org" returns keys that are not scoped to a project.
    """

    query: str
    """Case-insensitive substring match against API key name, creator, and project.

    API key identifiers and masked keys match by exact value or prefix.
    """

    service_account_id: str
    """Return only keys that belong to this service account."""

    sort_by: Literal["created_at", "name", "expires_at", "last_used_at"]
    """Field to sort API keys by.

    Keys with no expiry or no recorded use sort last for expires_at and last_used_at
    in either direction.
    """

    sort_direction: Literal["asc", "desc"]
    """Sort direction for API keys."""

    status: Literal["active", "expired", "deleted", "all"]
    """Filter API keys by status.

    "active" returns keys that are neither deleted nor expired (default), "expired"
    returns keys that are not deleted and whose expiry has passed, "deleted" returns
    only soft-deleted keys, "all" returns every key.
    """
