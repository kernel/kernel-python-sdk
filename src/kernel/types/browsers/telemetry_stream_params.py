# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TelemetryStreamParams"]


class TelemetryStreamParams(TypedDict, total=False):
    replay: str
    """
    Pass `all` to start from the oldest retained event instead of only new events;
    any other value is treated as from-now. The buffer is bounded, so the first
    event id may be greater than 1 if older events were evicted.
    """

    type: SequenceNotStr[str]
    """
    Deliver only these event types, such as captcha_solve_started or
    captcha_challenge_result. Repeat the parameter or pass comma-separated values
    for multiple types. Keepalive frames are always delivered. Filtered-out events
    are not sent. An id-only frame carrying the latest skipped id is sent about
    every 15 seconds while skipped events keep arriving, and otherwise with the next
    keepalive or when the stream ends, so the connection stays active and
    Last-Event-ID moves past them; a reconnect resumes after the skipped events.
    """

    last_event_id: Annotated[str, PropertyInfo(alias="Last-Event-ID")]
