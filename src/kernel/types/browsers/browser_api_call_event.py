# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserAPICallEvent", "Data"]


class Data(BaseModel):
    duration_ms: float
    """Wall-clock duration of the handler in milliseconds."""

    operation_id: str
    """OpenAPI operationId of the matched route (e.g. processExec, takeScreenshot)."""

    request_id: str
    """Per-request identifier from the in-VM API request middleware."""

    status: int
    """HTTP response status code."""


class BrowserAPICallEvent(BaseModel):
    """An agent-driven HTTP call handled by the in-VM API server."""

    category: Literal["control"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["api_call"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
