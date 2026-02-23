# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    limit: int
    """Limit the number of profiles to return."""

    offset: int
    """Offset the number of profiles to return."""

    query: str
    """Search profiles by name or ID."""
