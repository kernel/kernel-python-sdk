# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["BrowserCurlResponse"]


class BrowserCurlResponse(BaseModel):
    """Structured response from the browser curl request."""

    body: str
    """Response body (UTF-8 string or base64 depending on request)."""

    duration_ms: int
    """Total request duration in milliseconds."""

    headers: Dict[str, List[str]]
    """Response headers (multi-value)."""

    status: int
    """HTTP status code from target."""
