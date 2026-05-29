# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserMonitorScreenshotEvent", "Data"]


class Data(BaseModel):
    png: Optional[str] = None
    """Base64-encoded PNG screenshot of the browser viewport."""


class BrowserMonitorScreenshotEvent(BaseModel):
    """A periodic screenshot of the browser viewport."""

    category: Literal["system"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["monitor_screenshot"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
