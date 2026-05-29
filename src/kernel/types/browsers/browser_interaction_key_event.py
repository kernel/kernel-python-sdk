# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserInteractionKeyEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    key: Optional[str] = None
    """Key value from the KeyboardEvent (e.g. Enter, Backspace, a)."""

    selector: Optional[str] = None
    """CSS selector path to the element that had focus when the key was pressed."""

    tag: Optional[str] = None
    """HTML tag name of the focused element in uppercase (e.g. INPUT, TEXTAREA, DIV)."""


class BrowserInteractionKeyEvent(BaseModel):
    """A browser keyboard event captured via injected page script."""

    category: Literal["interaction"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["interaction_key"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
