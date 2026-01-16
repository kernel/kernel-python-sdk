# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrowserUpdateParams"]


class BrowserUpdateParams(TypedDict, total=False):
    proxy_id: Optional[str]
    """ID of the proxy to use.

    Omit to leave unchanged, set to empty string to remove proxy.
    """
