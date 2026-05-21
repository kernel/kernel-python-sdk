# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserEventContext"]


class BrowserEventContext(BaseModel):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    frame_id: Optional[str] = None
    """CDP frame identifier within the target."""

    loader_id: Optional[str] = None
    """CDP document loader identifier, reset on each navigation."""

    nav_seq: Optional[int] = None
    """
    Monotonically increasing navigation sequence number, incremented on each
    top-level navigation within the target.
    """

    session_id: Optional[str] = None
    """CDP session identifier for the target connection."""

    target_id: Optional[str] = None
    """Browser target identifier (stable across navigations within a tab)."""

    target_type: Optional[Literal["page", "background_page", "service_worker", "shared_worker", "other"]] = None
    """CDP target type of the page that produced the event."""

    url: Optional[str] = None
    """
    URL relevant to this event — page URL for navigation and page events, request
    URL for network events.
    """
