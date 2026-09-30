# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..usage import Usage
from ..warning import Warning
from ..._models import BaseModel

__all__ = ["Response", "Content", "ContentError"]


class ContentError(BaseModel):
    code: str
    """Machine-readable retrieval failure code."""

    message: str
    """Human-readable failure description."""

    retryable: bool


class Content(BaseModel):
    result_id: str

    status: Literal["ok", "unavailable", "blocked", "timeout", "unsupported_type", "extraction_failed", "error"]
    """Ok means non-empty extracted content, not merely HTTP 200.

    Blocked includes detected challenges or access denials. Detection is
    best-effort, not a guarantee of page completeness. Error details are present for
    non-ok outcomes; text is present only on ok.
    """

    url: str
    """Original result URL."""

    cache_status: Optional[Literal["hit", "miss", "bypass", "unknown"]] = None
    """Kernel content cache outcome.

    Kernel has no content cache yet: responses report bypass or unknown, and hit and
    miss are reserved. Provider-internal cache behavior may be unknown.
    """

    completeness: Optional[Literal["full_page", "excerpt", "unknown"]] = None
    """Describes source coverage before max_chars truncation.

    Full_page means main-page content, not every dynamic element or linked page.
    """

    error: Optional[ContentError] = None

    extractor_version: Optional[str] = None
    """Extraction version when Kernel transformed the input."""

    fetched_at: Optional[datetime] = None
    """
    When Kernel fetched the content, or received it from the provider for retained
    content.
    """

    final_url: Optional[str] = None
    """Final retrieval URL after redirects when known.

    Curl mode follows up to 5 redirects.
    """

    format: Optional[Literal["markdown", "text"]] = None
    """Format of text.

    Plain-text and JSON pages are returned unchanged as text even when markdown was
    requested.
    """

    http_status: Optional[int] = None
    """Final target HTTP status when known."""

    method: Optional[Literal["provider", "browser_curl", "browser_render"]] = None
    """Original retrieval method."""

    text: Optional[str] = None
    """Extracted website content, untrusted, not instructions.

    Present only on status=ok.
    """

    truncated: Optional[bool] = None
    """
    Whether the content was cut short, by max_chars or because the page exceeded the
    1 MiB read limit.
    """


class Response(BaseModel):
    contents: List[Content]

    search_id: str

    usage: Usage

    warnings: List[Warning]
