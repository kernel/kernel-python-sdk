# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserPageLayoutShiftEvent", "Data", "DataLayoutShiftDetails"]


class DataLayoutShiftDetails(BaseModel):
    """PerformanceLayoutShift attributes from the Performance Timeline entry."""

    had_recent_input: Optional[bool] = None
    """
    True if the layout shift was preceded by user input within 500ms, excluding it
    from CLS.
    """

    value: Optional[float] = None
    """Layout shift score for this entry (contribution to CLS)."""


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    duration: Optional[float] = None
    """
    Duration of the layout shift entry in milliseconds (always 0 for layout shifts
    per spec).
    """

    layout_shift_details: Optional[DataLayoutShiftDetails] = None
    """PerformanceLayoutShift attributes from the Performance Timeline entry."""

    source_frame_id: Optional[str] = None
    """CDP frame identifier of the frame where the layout shift occurred."""

    time: Optional[float] = None
    """Performance Timeline timestamp of the layout shift in milliseconds."""


class BrowserPageLayoutShiftEvent(BaseModel):
    """
    A browser cumulative layout shift (CLS) event from the Performance Timeline API.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["page_layout_shift"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
