# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    limit: int
    """Maximum number of results to return"""

    name: str
    """Exact-match filter on project name using the database collation.

    In production, matching is case- and accent-insensitive.
    """

    offset: int
    """Number of results to skip"""

    query: str
    """Case-insensitive substring match against project name"""
