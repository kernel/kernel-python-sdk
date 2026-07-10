# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    limit: int
    """Limit the number of profiles to return."""

    name: str
    """Exact-match filter on profile name using the database collation.

    In production, matching is case- and accent-insensitive. During the
    default-project migration, unscoped requests prefer a concrete default-project
    profile over a legacy unscoped profile with the same name.
    """

    offset: int
    """Offset the number of profiles to return."""

    query: str
    """Case-insensitive substring match against profile name or ID."""
