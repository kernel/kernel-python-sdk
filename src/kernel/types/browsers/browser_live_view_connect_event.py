# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserLiveViewConnectEvent", "Data"]


class Data(BaseModel):
    session_id: str
    """Live view session identifier.

    Stable across reconnects, so a transient network blip can emit two events with
    the same session_id.
    """


class BrowserLiveViewConnectEvent(BaseModel):
    """A live view client connected to the headful browser's WebRTC server.

    Headful only; not emitted for headless images.
    """

    category: Literal["connection"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["live_view_connect"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
