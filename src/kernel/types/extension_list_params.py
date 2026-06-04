# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtensionListParams"]


class ExtensionListParams(TypedDict, total=False):
    limit: int
    """Limit the number of extensions to return."""

    offset: int
    """Offset the number of extensions to return."""
