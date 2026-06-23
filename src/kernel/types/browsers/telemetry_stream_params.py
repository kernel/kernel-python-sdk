# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TelemetryStreamParams"]


class TelemetryStreamParams(TypedDict, total=False):
    replay: str
    """
    Pass `all` to start from the oldest retained event instead of only new events;
    any other value is treated as from-now. The buffer is bounded, so the first
    event id may be greater than 1 if older events were evicted.
    """

    last_event_id: Annotated[str, PropertyInfo(alias="Last-Event-ID")]
