# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserConsoleLogEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    args: Optional[List[str]] = None
    """All console arguments coerced to strings."""

    level: Optional[str] = None
    """CDP Runtime.consoleAPICalled type, passed through unfiltered from Chrome.

    error is routed to console_error events instead; all other CDP console types
    appear here. See CDP spec for the full enum.
    """

    stack_trace: Optional["BrowserCallStack"] = None
    """
    CDP Runtime.StackTrace representing the JavaScript call stack at the time of an
    event. Fields use CDP naming conventions rather than snake_case to match the
    Chrome DevTools Protocol wire format.
    """

    text: Optional[str] = None
    """First console argument coerced to string."""


class BrowserConsoleLogEvent(BaseModel):
    """A browser console log event (console.log, console.info, console.warn, etc.)."""

    category: Literal["console"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["console_log"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""


from .browser_call_stack import BrowserCallStack
