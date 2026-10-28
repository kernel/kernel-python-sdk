# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserSaveProfileParams"]


class BrowserSaveProfileParams(TypedDict, total=False):
    id: str
    """Existing profile ID to overwrite."""

    name: str
    """Profile name to overwrite or create."""
