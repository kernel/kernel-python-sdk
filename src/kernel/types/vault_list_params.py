# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VaultListParams"]


class VaultListParams(TypedDict, total=False):
    limit: int

    offset: int

    query: str
    """Case-insensitive substring match against vault name. IDs match by exact value."""
