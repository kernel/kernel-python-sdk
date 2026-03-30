# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.browser_profile import BrowserProfile
from .shared_params.browser_viewport import BrowserViewport

__all__ = ["BrowserUpdateParams", "Viewport"]


class BrowserUpdateParams(TypedDict, total=False):
    disable_default_proxy: bool
    """
    If true, stealth browsers connect directly instead of using the default stealth
    proxy.
    """

    profile: BrowserProfile
    """Profile to load into the browser session.

    Only allowed if the session does not already have a profile loaded.
    """

    proxy_id: Optional[str]
    """ID of the proxy to use.

    Omit to leave unchanged, set to empty string to remove proxy.
    """

    viewport: Viewport
    """Viewport configuration to apply to the browser session."""


class Viewport(BrowserViewport, total=False):
    """Viewport configuration to apply to the browser session."""

    force: bool
    """
    If true, allow the viewport change even when a live view or recording/replay is
    active. Active recordings will be gracefully stopped and restarted at the new
    resolution as separate segments. If false (default), the resize is refused when
    a live view or recording is active.
    """
