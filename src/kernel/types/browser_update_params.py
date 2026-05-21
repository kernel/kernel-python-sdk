# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.browser_profile import BrowserProfile
from .shared_params.browser_viewport import BrowserViewport
from .browsers.browser_telemetry_config_param import BrowserTelemetryConfigParam

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

    telemetry: Optional[BrowserTelemetryConfigParam]
    """Telemetry configuration.

    Omit, set to null, or set to an empty object ({}) to leave the existing
    configuration unchanged (no-op). To enable capture for all categories using VM
    defaults, set browser to an empty object ({"browser": {}}). To stop capture, set
    every category's enabled to false.
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
