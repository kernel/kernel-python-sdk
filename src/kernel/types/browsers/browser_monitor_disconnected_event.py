# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserMonitorDisconnectedEvent", "Data"]


class Data(BaseModel):
    reason: Optional[Literal["chrome_restarted"]] = None
    """Reason for the disconnection. chrome_restarted: Chrome process restarted."""


class BrowserMonitorDisconnectedEvent(BaseModel):
    """The CDP connection to Chrome was lost.

    Telemetry events may be dropped until monitor_reconnected arrives. In-progress computed state is discarded rather than paused, so computed events still pending for the current navigation (network_idle, page_layout_settled, page_navigation_settled) never fire. monitor_reconnected does not restore them. After reattachment a fresh state machine starts, so computed events can resume before the next navigation and carry empty navigation context until one occurs.
    """

    category: Literal["monitor"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["monitor_disconnected"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
