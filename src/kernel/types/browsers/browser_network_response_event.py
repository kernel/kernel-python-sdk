# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_http_headers import BrowserHTTPHeaders
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserNetworkResponseEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    body: Optional[str] = None
    """Truncated response body, present only for text MIME types."""

    headers: Optional[BrowserHTTPHeaders] = None
    """Response headers."""

    method: Optional[str] = None
    """HTTP method of the original request."""

    mime_type: Optional[str] = None
    """MIME type of the response (e.g. text/html, application/json)."""

    request_id: Optional[str] = None
    """CDP request identifier matching the originating network_request event."""

    resource_type: Optional[str] = None
    """CDP Network.ResourceType for the request, passed through as-is from Chrome.

    Known values include Document, Fetch, XHR, Script, Stylesheet, Image, Media,
    Font, TextTrack, EventSource, WebSocket, Manifest, Prefetch, Other, and more.
    """

    status: Optional[int] = None
    """HTTP response status code."""

    status_text: Optional[str] = None
    """HTTP response status text (e.g. OK, Not Found)."""


class BrowserNetworkResponseEvent(BaseModel):
    """A browser network response received event.

    Fired after the response body is fully received, not when headers arrive.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["network_response"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
