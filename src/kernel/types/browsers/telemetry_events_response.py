# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["TelemetryEventsResponse"]


class TelemetryEventsResponse(BaseModel):
    """Envelope wrapping a browser telemetry event with its monotonic sequence number.

    Each SSE data: frame carries one envelope as JSON. The seq value is also emitted as the SSE id: field so clients can pass it as Last-Event-ID on reconnect.
    """

    event: "BrowserTelemetryEvent"
    """Union type representing any browser telemetry event.

    Discriminated on `type`. Each event's `category` determines when it is captured.
    The CDP collector-health events (monitor_disconnected, monitor_reconnected,
    monitor_reconnect_failed, monitor_init_failed) use the `monitor` category, which
    is not user-configurable: it flows automatically whenever any CDP category
    (console, network, page, interaction) is captured, and is silent otherwise.
    monitor_screenshot uses the opt-in `screenshot` category. All other event types
    are controlled by their per-category enable/disable flags.
    """

    seq: int
    """Process-monotonic sequence number assigned by the browser VM.

    Pass as Last-Event-ID on reconnect to resume without gaps. Gaps in received seq
    values indicate dropped events.
    """


from .browser_telemetry_event import BrowserTelemetryEvent
