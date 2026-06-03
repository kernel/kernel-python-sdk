# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserPoolListParams"]


class BrowserPoolListParams(TypedDict, total=False):
    limit: int
    """Limit the number of browser pools to return."""

    offset: int
    """Offset the number of browser pools to return."""
