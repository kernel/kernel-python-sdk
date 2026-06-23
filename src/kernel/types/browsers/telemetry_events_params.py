# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["TelemetryEventsParams"]


class TelemetryEventsParams(TypedDict, total=False):
    category: List[
        Literal[
            "console",
            "network",
            "page",
            "interaction",
            "control",
            "connection",
            "system",
            "screenshot",
            "captcha",
            "monitor",
        ]
    ]
    """Restrict results to these event categories.

    Repeat the parameter for multiple values.
    """

    limit: int
    """Maximum number of events per page. Defaults to 20."""

    offset: int
    """
    Opaque pagination cursor: pass the X-Next-Offset value from the previous
    response to fetch the next page. When set, paging continues from this cursor and
    since is ignored, while until still bounds the page. It is not an event's seq
    field, so do not derive it from the response body.
    """

    since: str
    """
    Start of the window: an RFC-3339 timestamp, or a duration like 5m meaning that
    long ago. Defaults to 5m. Ignored when offset is set.
    """

    until: str
    """
    End of the window (exclusive): an RFC-3339 timestamp, or a duration like 5m
    meaning that long ago.
    """
