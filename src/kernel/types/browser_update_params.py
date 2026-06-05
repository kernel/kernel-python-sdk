# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.browser_profile import BrowserProfile
from .shared_params.browser_viewport import BrowserViewport
from .browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = ["BrowserUpdateParams", "Telemetry", "Viewport"]


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

    telemetry: Optional[Telemetry]
    """Telemetry configuration.

    Omit, set to null, or set to an empty object ({}) to leave the existing
    configuration unchanged. Set enabled to true to enable capture using VM
    defaults. Set enabled to false to stop capture. Provide browser category
    settings for per-category updates. Explicitly disabling all four categories also
    stops capture.
    """

    viewport: Viewport
    """Viewport configuration to apply to the browser session."""


class Telemetry(TypedDict, total=False):
    """Telemetry configuration.

    Omit, set to null, or set to an empty object ({}) to leave the existing configuration unchanged. Set enabled to true to enable capture using VM defaults. Set enabled to false to stop capture. Provide browser category settings for per-category updates. Explicitly disabling all four categories also stops capture.
    """

    browser: BrowserTelemetryCategoriesConfigParam
    """Per-category capture flags.

    Selection is opt-in: only the categories set to enabled=true are captured;
    anything omitted is off. If enabled is true and browser is omitted or empty, the
    default category set is used. A browser config that enables nothing stops
    capture on update and starts no capture on create.
    """

    enabled: bool
    """Request shortcut for browser telemetry capture.

    True enables capture using the default category set unless browser category
    settings are provided. False stops capture on update and starts no capture on
    create. enabled=false cannot be combined with browser category settings.
    """


class Viewport(BrowserViewport, total=False):
    """Viewport configuration to apply to the browser session."""

    force: bool
    """
    If true, allow the viewport change even when a live view or recording/replay is
    active. Active recordings will be gracefully stopped and restarted at the new
    resolution as separate segments. If false (default), the resize is refused when
    a live view or recording is active.
    """
