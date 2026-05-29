# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserPageLcpEvent", "Data", "DataLcpDetails"]


class DataLcpDetails(BaseModel):
    """LargestContentfulPaint attributes from the Performance Timeline entry."""

    element_id: Optional[str] = None
    """id attribute of the LCP element, if present."""

    load_time: Optional[float] = None
    """Load time of the LCP element in milliseconds."""

    node_id: Optional[int] = None
    """CDP DOM node identifier of the LCP element."""

    render_time: Optional[float] = None
    """
    Render time of the LCP element in milliseconds; 0 for cross-origin images
    without Timing-Allow-Origin.
    """

    size: Optional[float] = None
    """Visible area of the LCP element in pixels squared."""

    url: Optional[str] = None
    """URL of the LCP element for image or video elements."""


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    lcp_details: Optional[DataLcpDetails] = None
    """LargestContentfulPaint attributes from the Performance Timeline entry."""

    source_frame_id: Optional[str] = None
    """CDP frame identifier of the frame where the LCP element was rendered."""

    time: Optional[float] = None
    """Performance Timeline timestamp of the LCP entry in milliseconds."""


class BrowserPageLcpEvent(BaseModel):
    """
    A browser Largest Contentful Paint (LCP) event from the Performance Timeline API.
    """

    category: Literal["page"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["page_lcp"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
