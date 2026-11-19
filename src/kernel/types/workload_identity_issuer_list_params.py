# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WorkloadIdentityIssuerListParams"]


class WorkloadIdentityIssuerListParams(TypedDict, total=False):
    enabled: bool

    limit: int

    offset: int

    query: str
    """Case-insensitive substring match against name or description; exact ID match."""

    status: Literal["active", "archived", "all"]
