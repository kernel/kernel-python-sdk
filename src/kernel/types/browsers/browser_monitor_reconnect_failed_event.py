# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserMonitorReconnectFailedEvent", "Data"]


class Data(BaseModel):
    reason: Optional[Literal["reconnect_exhausted"]] = None
    """Reason for the reconnection failure.

    reconnect_exhausted: all retry attempts were used up without successfully
    restoring the CDP connection.
    """


class BrowserMonitorReconnectFailedEvent(BaseModel):
    """
    The CDP connection to Chrome could not be re-established after exhausting all reconnection attempts. No further telemetry events will arrive on this session.
    """

    category: Literal["system"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["monitor_reconnect_failed"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
