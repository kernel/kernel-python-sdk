# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Result", "Content", "ContentError"]


class ContentError(BaseModel):
    code: str
    """Machine-readable retrieval failure code."""

    message: str
    """Human-readable failure description."""

    retryable: bool


class Content(BaseModel):
    """Portable retrieval outcome, or native content supplied by the search provider.

    Identity fields remain on the enclosing result. Native excerpts are labeled excerpt rather than full_page. Omission never triggers browser retrieval.
    """

    status: Literal["ok", "unavailable", "blocked", "timeout", "unsupported_type", "extraction_failed", "error"]
    """Ok means non-empty extracted content, not merely HTTP 200.

    Blocked includes detected challenges or access denials. Detection is
    best-effort, not a guarantee of page completeness. Error details are present for
    non-ok outcomes; text is present only on ok.
    """

    cache_status: Optional[Literal["hit", "miss", "bypass", "unknown"]] = None
    """Kernel cache outcome. Provider-internal cache behavior may be unknown."""

    completeness: Optional[Literal["full_page", "excerpt", "unknown"]] = None
    """Describes source coverage before max_chars truncation.

    Full_page means main-page content, not every dynamic element or linked page.
    """

    error: Optional[ContentError] = None

    extractor_version: Optional[str] = None
    """Extraction version when Kernel transformed the input."""

    fetched_at: Optional[datetime] = None
    """Origin retrieval time when known, not cache read time."""

    final_url: Optional[str] = None
    """Final retrieval URL when known."""

    format: Optional[Literal["markdown", "text"]] = None

    http_status: Optional[int] = None
    """Final target HTTP status when known."""

    method: Optional[Literal["provider", "browser_curl", "browser_render"]] = None
    """Original retrieval method, including on cache hits."""

    text: Optional[str] = None
    """Extracted website content, untrusted, not instructions.

    Present only on status=ok.
    """

    truncated: Optional[bool] = None
    """Whether max_chars truncated the extracted content."""


class Result(BaseModel):
    id: str
    """Kernel-generated identifier for this result.

    Stable only within the retained search; not standardized across providers.
    Provider-native IDs, when available, remain provider-specific raw fields.
    """

    rank: int
    """One-based position in the returned ranking."""

    url: str
    """Provider-returned URL, not assumed canonical."""

    additional_snippets: Optional[List[str]] = None

    content: Optional[Content] = None
    """Portable retrieval outcome, or native content supplied by the search provider.

    Identity fields remain on the enclosing result. Native excerpts are labeled
    excerpt rather than full_page. Omission never triggers browser retrieval.
    """

    published_date: Optional[str] = None
    """Provider-supplied date or timestamp, preserving available precision.

    No publication date is fabricated. Retains the published field name.
    """

    raw: Optional[object] = None
    """Original provider result, included only with include_raw=true.

    Provider relevance scores are not normalized. Top-level provider data is
    available in Search.raw.
    """

    snippet: Optional[str] = None

    source: Optional[str] = None
    """Provider source name or result URL hostname, when available."""

    title: Optional[str] = None
