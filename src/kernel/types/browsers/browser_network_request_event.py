# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_http_headers import BrowserHTTPHeaders
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserNetworkRequestEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    document_url: Optional[str] = None
    """URL of the document that initiated the request."""

    headers: Optional[BrowserHTTPHeaders] = None
    """Request headers."""

    initiator_type: Optional[str] = None
    """
    CDP Initiator.type indicating what caused the request, passed through as-is from
    Chrome. Known values include script, parser, preload, and other.
    """

    is_redirect: Optional[bool] = None
    """True if this request is the result of a redirect."""

    method: Optional[str] = None
    """HTTP method as sent on the wire (e.g. GET, POST)."""

    post_data: Optional[str] = None
    """Request body for POST/PUT requests, if available."""

    redirect_url: Optional[str] = None
    """Original URL before the redirect, present when is_redirect is true."""

    request_id: Optional[str] = None
    """CDP request identifier, unique within the session."""

    resource_type: Optional[str] = None
    """CDP Network.ResourceType for the request, passed through as-is from Chrome.

    Known values include Document, Fetch, XHR, Script, Stylesheet, Image, Media,
    Font, TextTrack, EventSource, WebSocket, Manifest, Prefetch, Other, and more.
    """


class BrowserNetworkRequestEvent(BaseModel):
    """A browser network request sent event."""

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["network_request"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
