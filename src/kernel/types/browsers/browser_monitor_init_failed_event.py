# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserMonitorInitFailedEvent", "Data"]


class Data(BaseModel):
    step: Optional[str] = None
    """The CDP method or initialization step that failed (e.g. Target.setAutoAttach)."""


class BrowserMonitorInitFailedEvent(BaseModel):
    """The CDP session could not be initialized."""

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["monitor_init_failed"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
