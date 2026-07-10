# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtensionListParams"]


class ExtensionListParams(TypedDict, total=False):
    limit: int
    """Limit the number of extensions to return."""

    name: str
    """Exact-match filter on extension name using the database collation.

    In production, matching is case- and accent-insensitive. During the
    default-project migration, unscoped requests prefer a concrete default-project
    extension over a legacy unscoped extension with the same name.
    """

    offset: int
    """Offset the number of extensions to return."""

    query: str
    """Case-insensitive substring match against extension name.

    IDs match by exact value.
    """
