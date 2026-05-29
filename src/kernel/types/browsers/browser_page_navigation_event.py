# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserPageNavigationEvent", "Data"]


class Data(BaseModel):
    frame_id: Optional[str] = None
    """CDP frame identifier of the navigated frame."""

    loader_id: Optional[str] = None
    """New CDP document loader identifier assigned for this navigation."""

    parent_frame_id: Optional[str] = None
    """
    Parent frame identifier for subframe navigations; absent for top-level
    navigations.
    """

    session_id: Optional[str] = None
    """CDP session identifier."""

    target_id: Optional[str] = None
    """Browser target identifier."""

    target_type: Optional[Literal["page", "background_page", "service_worker", "shared_worker", "other"]] = None
    """CDP target type of the page that produced the event."""

    url: Optional[str] = None
    """URL navigated to."""


class BrowserPageNavigationEvent(BaseModel):
    """A browser page navigation started event (CDP Page.frameNavigated).

    Carries nav context fields inline but not nav_seq, as this event resets the navigation epoch.
    """

    category: Literal["page"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["page_navigation"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
