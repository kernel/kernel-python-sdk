# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserLiveViewDisconnectEvent", "Data"]


class Data(BaseModel):
    duration_ms: float
    """Wall-clock duration of the connection in milliseconds."""

    session_id: str
    """
    Live view session identifier; matches the corresponding live_view_connect event.
    """


class BrowserLiveViewDisconnectEvent(BaseModel):
    """A live view client disconnected from the headful browser's WebRTC server.

    Pair with live_view_connect by session_id.
    """

    category: Literal["connection"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["live_view_disconnect"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
