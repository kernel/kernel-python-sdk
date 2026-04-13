# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrowserCurlParams"]


class BrowserCurlParams(TypedDict, total=False):
    url: Required[str]
    """Target URL (must be http or https)."""

    body: str
    """Request body (for POST/PUT/PATCH)."""

    headers: Dict[str, str]
    """Custom headers merged with browser defaults."""

    method: Literal["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    """HTTP method."""

    response_encoding: Literal["utf8", "base64"]
    """Encoding for the response body. Use base64 for binary content."""

    timeout_ms: int
    """Request timeout in milliseconds."""
