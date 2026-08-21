# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserPlatformAPICallEvent", "Data"]


class Data(BaseModel):
    duration_ms: float
    """Wall-clock duration of the handler in milliseconds."""

    operation_id: str
    """Matched route's operation, named as the in-VM API names its handler (e.g.

    ProcessExec, StartRecording).
    """

    request_id: str
    """Per-request identifier from the in-VM API request middleware."""

    status: int
    """HTTP response status code."""


class BrowserPlatformAPICallEvent(BaseModel):
    """
    An HTTP call that manages the browser VM rather than driving the browser, handled by the in-VM API server — recording lifecycle, filesystem and process management, telemetry and browser configuration. Mostly platform-induced (e.g. profile save, replay capture) rather than agent actions.
    """

    category: Literal["platform"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["platform_api_call"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
