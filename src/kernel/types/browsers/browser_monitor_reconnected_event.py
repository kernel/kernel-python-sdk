# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserMonitorReconnectedEvent", "Data"]


class Data(BaseModel):
    reconnect_duration_ms: Optional[int] = None
    """Wall-clock time in milliseconds taken to reconnect after the disconnection."""


class BrowserMonitorReconnectedEvent(BaseModel):
    """
    The CDP connection to Chrome was successfully re-established after a disconnection. Events emitted during the gap are lost. Computed state is reset, so navigation and network tracking restart fresh from this point.
    """

    category: Literal["system"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["monitor_reconnected"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
