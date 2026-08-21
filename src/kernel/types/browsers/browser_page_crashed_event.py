# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserPageCrashedEvent", "Data"]


class Data(BaseModel):
    target_id: str
    """CDP target identifier of the crashed page."""

    target_type: Literal["page", "background_page", "service_worker", "shared_worker", "other"]
    """CDP target type of the page that produced the event."""

    url: str
    """URL the page was on when its renderer process crashed."""


class BrowserPageCrashedEvent(BaseModel):
    """
    A page's renderer process crashed (an "Aw, Snap!" failure) while the browser process itself stayed alive. Reported on the crashed page's session, with the session and target ids on `source.metadata`. Captured only while the `page` category is enabled.
    """

    category: Literal["page"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["page_crashed"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
