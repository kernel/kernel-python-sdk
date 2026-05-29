# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserInteractionScrollSettledEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    from_x: Optional[int] = None
    """Scroll x-position at the start of the scroll gesture in CSS pixels."""

    from_y: Optional[int] = None
    """Scroll y-position at the start of the scroll gesture in CSS pixels."""

    target_selector: Optional[str] = None
    """CSS selector path to the scrolled element."""

    to_x: Optional[int] = None
    """Final scroll x-position after the gesture settled in CSS pixels."""

    to_y: Optional[int] = None
    """Final scroll y-position after the gesture settled in CSS pixels."""


class BrowserInteractionScrollSettledEvent(BaseModel):
    """
    A browser scroll settled event emitted after scroll position stops changing, captured via injected page script.
    """

    category: Literal["interaction"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["interaction_scroll_settled"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
