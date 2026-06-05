# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserCdpConnectEvent"]


class BrowserCdpConnectEvent(BaseModel):
    """An external client (e.g.

    customer SDK, Playwright, Puppeteer) connected to the CDP WebSocket proxy on this VM.
    """

    category: Literal["connection"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["cdp_connect"]

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
