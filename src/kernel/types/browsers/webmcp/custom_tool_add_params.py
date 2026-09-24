# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomToolAddParams"]


class CustomToolAddParams(TypedDict, total=False):
    namespace: Required[str]

    source: Required[str]
    """
    JavaScript expression that evaluates to a non-empty array of custom tool
    definitions. Limited to 8,000,000 bytes when UTF-8 encoded, so multi-byte
    characters reduce the allowed character count.
    """

    force_overwrite_namespace: bool
    """
    Atomically replace all existing tools in this namespace with this batch when
    true.
    """
