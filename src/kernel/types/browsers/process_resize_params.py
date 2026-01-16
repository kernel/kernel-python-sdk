# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProcessResizeParams"]


class ProcessResizeParams(TypedDict, total=False):
    id: Required[str]

    cols: Required[int]
    """New terminal columns."""

    rows: Required[int]
    """New terminal rows."""
