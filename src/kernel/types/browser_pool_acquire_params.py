# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .tags_param import TagsParam

__all__ = ["BrowserPoolAcquireParams"]


class BrowserPoolAcquireParams(TypedDict, total=False):
    acquire_timeout_seconds: int
    """Maximum number of seconds to wait for a browser to be available.

    Defaults to the calculated time it would take to fill the pool at the currently
    configured fill rate.
    """

    name: str
    """
    Optional human-readable name for the acquired browser session, used to find it
    later in the dashboard. Must be unique among active sessions within the pool's
    project. Applies to this lease only and is cleared when the browser is released
    back to the pool.
    """

    tags: TagsParam
    """
    Optional user-defined key-value tags for the acquired browser session, used to
    find and group sessions later. Applies to this lease only and are cleared when
    the browser is released back to the pool. Up to 50 pairs.
    """
