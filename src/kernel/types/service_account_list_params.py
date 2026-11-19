# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ServiceAccountListParams"]


class ServiceAccountListParams(TypedDict, total=False):
    limit: int

    offset: int

    query: str
    """Case-insensitive substring match against name or description; exact ID match."""

    status: Literal["active", "archived", "all"]
