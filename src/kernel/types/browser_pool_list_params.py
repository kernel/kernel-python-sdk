# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserPoolListParams"]


class BrowserPoolListParams(TypedDict, total=False):
    limit: int
    """Limit the number of browser pools to return."""

    name: str
    """Exact-match filter on browser pool name using the database collation.

    In production, matching is case- and accent-insensitive. During the
    default-project migration, unscoped requests prefer a concrete default-project
    browser pool over a legacy unscoped browser pool with the same name.
    """

    offset: int
    """Offset the number of browser pools to return."""

    query: str
    """Case-insensitive substring match against browser pool name.

    IDs match by exact value.
    """
