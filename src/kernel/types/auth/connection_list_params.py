# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionListParams"]


class ConnectionListParams(TypedDict, total=False):
    domain: str
    """Filter by domain"""

    limit: int
    """Maximum number of results to return"""

    offset: int
    """Number of results to skip"""

    profile_name: str
    """Filter by profile name"""
