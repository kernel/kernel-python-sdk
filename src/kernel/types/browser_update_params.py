# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .tags_param import TagsParam
from .browser_proxy_config_param import BrowserProxyConfigParam
from .shared_params.browser_profile import BrowserProfile
from .shared_params.browser_viewport import BrowserViewport
from .browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = [
    "BrowserUpdateParams",
    "Telemetry",
    "TelemetryExport",
    "TelemetryExportOtlp",
    "TelemetryExportOtlpDestination",
    "Viewport",
]


class BrowserUpdateParams(TypedDict, total=False):
    disable_default_proxy: bool
    """
    If true, stealth browsers connect directly instead of using the default stealth
    proxy. Deprecated in favor of proxy.mode.
    """

    name: Optional[str]
    """Human-readable name for the browser session.

    Omit to leave unchanged, set to an empty string to clear the name. When set,
    must be unique among active sessions within the project.
    """

    profile: BrowserProfile
    """Profile to load into the browser session.

    Only allowed if the session does not already have a profile loaded.
    """

    proxy: BrowserProxyConfigParam
    """Proxy configuration to apply.

    Omit to leave the current configuration unchanged. Cannot be combined with
    proxy_id or disable_default_proxy. Set mode to direct to switch to direct egress
    regardless of stealth. Set mode to default to restore the browser default after
    using a selected proxy: Kernel's default stealth proxy for a stealth browser, or
    direct egress for a non-stealth browser. Updating proxy does not change stealth
    or CAPTCHA solver behavior.
    """

    proxy_id: Optional[str]
    """ID of the proxy to use.

    Omit to leave unchanged, set to empty string to remove proxy. Deprecated in
    favor of proxy.
    """

    tags: Optional[TagsParam]
    """User-defined key-value tags for the browser session.

    Omit to leave unchanged. Provide a map to replace the entire tag set (full
    replace, not a merge). Set to an empty object ({}) to clear all tags. Up to 50
    pairs.
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


class TelemetryExportOtlpDestination(TypedDict, total=False):
    """OTLP destination to export this session's captured telemetry to.

    Provide either id or name. Requires telemetry capture to be enabled.
    """

    id: str
    """OTLP destination ID"""

    name: str
    """OTLP destination name"""


class TelemetryExportOtlp(TypedDict, total=False):
    """
    Export captured telemetry over OTLP to one of the org's configured destinations.
    """

    destination: TelemetryExportOtlpDestination
    """OTLP destination to export this session's captured telemetry to.

    Provide either id or name. Requires telemetry capture to be enabled.
    """

    enabled: bool
    """Whether to export captured telemetry over OTLP.

    Setting destination implies enabled=true, so this only needs to be set
    explicitly to disable export (enabled=false with a destination is rejected).
    """


class TelemetryExport(TypedDict, total=False):
    """Where to export this session's captured telemetry.

    Omit to capture without exporting.
    """

    otlp: TelemetryExportOtlp
    """
    Export captured telemetry over OTLP to one of the org's configured destinations.
    """


class Telemetry(TypedDict, total=False):
    """Telemetry configuration.

    Omit, set to null, or set to an empty object ({}) to leave the existing configuration unchanged. Set enabled to true to enable capture using VM defaults. Set enabled to false to stop capture. Provide browser category settings for per-category updates. Explicitly disabling all four categories also stops capture.
    """

    browser: BrowserTelemetryCategoriesConfigParam
    """Per-category capture flags.

    The operational categories (control, connection, system, captcha) are captured
    whenever telemetry is enabled; set one to enabled=false to opt out. The CDP
    categories (console, network, page, interaction), screenshot and platform are
    off by default; set enabled=true to opt in. On create, provided categories layer
    onto the default set. On update, provided categories merge onto the session's
    current config; when no telemetry is active this falls back to the default set
    (matching create). If browser is omitted or empty, the default set is used. A
    browser config that disables every category stops capture on update and starts
    no capture on create.
    """

    enabled: bool
    """Request shortcut for browser telemetry capture.

    True enables capture; with no browser category settings it captures the default
    set (control, connection, system, captcha), and any browser category settings
    are layered onto that default set. On update, enabled=true resolves the config
    fresh from the default set plus any provided categories, replacing the session's
    current selection rather than merging onto it; omit enabled to merge categories
    onto the current selection instead. False stops capture on update and starts no
    capture on create. enabled=false cannot be combined with browser category
    settings.
    """

    export: TelemetryExport
    """Where to export this session's captured telemetry.

    Omit to capture without exporting.
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
