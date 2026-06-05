# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserServiceCrashedEvent", "Data"]


class Data(BaseModel):
    phase: Literal["startup", "running", "gave_up"]
    """Lifecycle phase the crash occurred in.

    startup: the process died before reaching a healthy running state. running: a
    previously healthy process died unexpectedly. gave_up: the process manager
    exhausted its restart attempts and stopped trying.
    """

    service_name: str
    """Program name of the crashed service (e.g. chromium, mutter, kernel-images-api)."""

    pid: Optional[int] = None
    """PID of the crashed process.

    Absent when the process manager gave up after exhausting restart attempts.
    """


class BrowserServiceCrashedEvent(BaseModel):
    """A managed service exited unexpectedly.

    Intentional stops do not produce this event; only unexpected exits and terminal restart-give-up transitions do.
    """

    category: Literal["system"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["service_crashed"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
