# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserConsoleErrorEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    text: str
    """Human-readable error text, as the browser console would display it.

    For console.error() calls, the first argument coerced to a string. For uncaught
    exceptions, the prefix and error message, e.g. "Uncaught Error: boom" or
    "Uncaught (in promise) TypeError: x is not a function".
    """

    args: Optional[List[str]] = None
    """All console arguments coerced to strings.

    Present only when sourced from Runtime.consoleAPICalled.
    """

    column: Optional[int] = None
    """Column number in the script where the exception was thrown.

    Present only when sourced from Runtime.exceptionThrown.
    """

    level: Optional[str] = None
    """CDP console type value, always "error".

    Present only when sourced from Runtime.consoleAPICalled.
    """

    line: Optional[int] = None
    """Line number in the script where the exception was thrown.

    Present only when sourced from Runtime.exceptionThrown.
    """

    source_url: Optional[str] = None
    """URL of the script file that threw the exception.

    Present only when sourced from Runtime.exceptionThrown.
    """

    stack_trace: Optional["BrowserCallStack"] = None
    """
    CDP Runtime.StackTrace representing the JavaScript call stack at the time of an
    event. Fields use CDP naming conventions rather than snake_case to match the
    Chrome DevTools Protocol wire format.
    """


class BrowserConsoleErrorEvent(BaseModel):
    """A browser console error or uncaught JavaScript exception event.

    Emitted from two distinct CDP sources with different data shapes. Runtime.consoleAPICalled (console.error calls) produces level, text, args, and stack_trace. Runtime.exceptionThrown (uncaught exceptions) produces text, line, column, source_url, and stack_trace. Fields not applicable to the source are absent.
    """

    category: Literal["console"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["console_error"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""


from .browser_call_stack import BrowserCallStack
