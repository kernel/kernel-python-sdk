# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WebmcpInvokeToolParams"]


class WebmcpInvokeToolParams(TypedDict, total=False):
    input: Required[Dict[str, object]]
    """Tool input, limited to 4 MiB after JSON serialization."""

    tool_ref: Required[str]

    timeout_sec: int
