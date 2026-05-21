# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserPageNavigationSettledEvent"]


class BrowserPageNavigationSettledEvent(BaseModel):
    """
    Emitted when page_dom_content_loaded and page_layout_settled have both fired for the same navigation, indicating the page is loaded and visually stable. Independent of network_idle; a single pending request does not block it.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["page_navigation_settled"]

    data: Optional[BrowserEventContext] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
