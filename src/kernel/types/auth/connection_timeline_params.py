# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectionTimelineParams"]


class ConnectionTimelineParams(TypedDict, total=False):
    limit: int
    """Maximum number of events to return"""

    offset: int
    """Number of events to skip"""

    type: Literal["login", "reauth", "health_check"]
    """Filter the timeline to a single event type."""
