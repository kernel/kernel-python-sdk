# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebmcpListToolsParams"]


class WebmcpListToolsParams(TypedDict, total=False):
    exclude_custom: bool
    """Exclude custom tools when true."""
