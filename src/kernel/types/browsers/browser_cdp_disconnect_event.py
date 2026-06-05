# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserCdpDisconnectEvent", "Data"]


class Data(BaseModel):
    duration_ms: float
    """Wall-clock duration of the connection in milliseconds."""

    message_count: int
    """Number of CDP messages relayed across the connection in either direction."""

    reason: Literal["client_close", "upstream_changed", "upstream_error", "context_cancelled"]
    """Why the connection ended.

    client_close: the client initiated the close. upstream_changed: Chromium
    restarted mid-session and the proxy tore down so the client could reconnect
    against the new upstream. upstream_error: upstream dial or message pump errored.
    context_cancelled: the request context was cancelled (typically server
    shutdown).
    """


class BrowserCdpDisconnectEvent(BaseModel):
    """An external client disconnected from the CDP WebSocket proxy on this VM.

    Pair with the immediately preceding cdp_connect on the same stream.
    """

    category: Literal["connection"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["cdp_disconnect"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
