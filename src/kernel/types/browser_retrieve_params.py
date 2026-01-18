# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserRetrieveParams"]


class BrowserRetrieveParams(TypedDict, total=False):
    include_deleted: bool
    """When true, includes soft-deleted browser sessions in the lookup."""
