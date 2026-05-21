# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserNetworkLoadingFailedEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    canceled: Optional[bool] = None
    """True if the request was canceled by the browser or page script."""

    error_text: Optional[str] = None
    """Network error description (e.g. net::ERR_CONNECTION_REFUSED)."""

    request_id: Optional[str] = None
    """CDP request identifier matching the originating network_request event."""

    resource_type: Optional[str] = None
    """CDP Network.ResourceType for the request, passed through as-is from Chrome.

    Known values include Document, Fetch, XHR, Script, Stylesheet, Image, Media,
    Font, TextTrack, EventSource, WebSocket, Manifest, Prefetch, Other, and more.
    """


class BrowserNetworkLoadingFailedEvent(BaseModel):
    """A browser network loading failed event.

    If the request was already in flight when CDP attached (no prior network_request was emitted for it), url, frame_id, loader_id, and resource_type are absent; BrowserEventContext is partially populated in that case.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["network_loading_failed"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
