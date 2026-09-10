# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource
from .browser_event_context import BrowserEventContext

__all__ = ["BrowserProxyErrorEvent", "Data"]


class Data(BrowserEventContext):
    """Browser event context stamped by the browser monitor onto all CDP-sourced events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    code: Literal[
        "destination_blocked",
        "provider_blacklisted",
        "provider_unreachable",
        "provider_rejected",
        "origin_tls_timeout",
        "proxy_unavailable",
        "upstream_timeout",
        "upstream_dns_failure",
        "upstream_connect_failed",
    ]
    """
    Proxy-layer error code: the X-Kernel-Proxy-Error response header value from a
    branded 5xx error page served by the metro egress host-proxy. Values mirror what
    the proxy emits: destination_blocked, provider_blacklisted,
    provider_unreachable, provider_rejected, origin_tls_timeout, proxy_unavailable,
    upstream_timeout, upstream_dns_failure, upstream_connect_failed. Unknown header
    values are dropped.
    """

    request_id: str
    """CDP request identifier matching the originating request."""

    status: int
    """HTTP response status of the branded error page (502)."""

    method: Optional[str] = None
    """HTTP method of the failed request, when known."""

    resource_type: Optional[str] = None
    """CDP Network.ResourceType for the request, when known."""


class BrowserProxyErrorEvent(BaseModel):
    """A branded proxy-layer failure observed by the browser.

    Emitted when the metro egress host-proxy serves a branded 5xx error page whose response carries the X-Kernel-Proxy-Error header. Low-volume and carries a typed code. Its value is per-session and per-URL attribution for sessions that already capture the network stream: proxy failures are only observable while the CDP network collector is running, so this is an opt-in refinement of the raw network events rather than a default-on alerting signal.
    """

    category: Literal["network"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["proxy_error"]

    data: Optional[Data] = None
    """Browser event context stamped by the browser monitor onto all CDP-sourced
    events.

    Identifies the target, frame, and navigation epoch in which the event occurred.
    """

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
