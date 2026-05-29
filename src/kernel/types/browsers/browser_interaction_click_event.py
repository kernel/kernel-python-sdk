# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserInteractionClickEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    selector: Optional[str] = None
    """CSS selector path to the clicked element."""

    tag: Optional[str] = None
    """HTML tag name of the clicked element in uppercase (e.g. BUTTON, A, DIV)."""

    text: Optional[str] = None
    """Visible text content of the clicked element, trimmed."""

    x: Optional[int] = None
    """Viewport x-coordinate of the click in CSS pixels."""

    y: Optional[int] = None
    """Viewport y-coordinate of the click in CSS pixels."""


class BrowserInteractionClickEvent(BaseModel):
    """A browser user click event captured via injected page script."""

    category: Literal["interaction"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["interaction_click"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
