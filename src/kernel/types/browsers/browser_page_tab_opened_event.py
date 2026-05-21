# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserPageTabOpenedEvent", "Data"]


class Data(BaseModel):
    opener_id: Optional[str] = None
    """Target identifier of the tab that opened this one, if any."""

    target_id: Optional[str] = None
    """CDP target identifier for the newly opened tab."""

    target_type: Optional[Literal["page", "background_page", "service_worker", "shared_worker", "other"]] = None
    """CDP target type of the page that produced the event."""

    title: Optional[str] = None
    """Initial page title of the new tab."""

    url: Optional[str] = None
    """Initial URL of the new tab."""


class BrowserPageTabOpenedEvent(BaseModel):
    """
    A new browser tab or target was opened (CDP Target.attachedToTarget for page targets). Fires before a CDP session is attached to the new target, so session_id, frame_id, loader_id, and nav_seq are absent; this event does not compose BrowserEventContext. Consumers reading context fields generically should treat it as a special case.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["page_tab_opened"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
