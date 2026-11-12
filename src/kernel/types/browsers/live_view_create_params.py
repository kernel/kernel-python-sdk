# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_live_view_scope import BrowserLiveViewScope

__all__ = ["LiveViewCreateParams"]


class LiveViewCreateParams(TypedDict, total=False):
    scope: BrowserLiveViewScope
    """`read` shows the browser without accepting input.

    `control` also lets the viewer drive the browser through the live view.
    """

    ttl_seconds: int
    """Seconds until the URL expires.

    Omit to keep it valid until the browser is deleted.
    """
