# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..browser_proxy_config_param import BrowserProxyConfigParam
from ..browser_captcha_solver_param import BrowserCaptchaSolverParam
from .managed_auth_browser_location_param import ManagedAuthBrowserLocationParam
from ..browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = [
    "ManagedAuthBrowserConfigParam",
    "Telemetry",
    "TelemetryExport",
    "TelemetryExportOtlp",
    "TelemetryExportOtlpDestination",
    "TelemetryStorage",
]


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


class TelemetryStorage(TypedDict, total=False):
    """Whether to persist this session's captured telemetry to Kernel storage."""

    enabled: bool
    """Whether captured telemetry is persisted to Kernel storage.

    Defaults to true. Setting false requires an OTLP destination and cannot be
    changed after the browser is created.
    """


class Telemetry(TypedDict, total=False):
    """Browser telemetry configuration using the same semantics as browser create."""

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

    storage: TelemetryStorage
    """Whether to persist this session's captured telemetry to Kernel storage."""


class ManagedAuthBrowserConfigParam(TypedDict, total=False):
    """
    Browser configuration applied to browser sessions created for a managed auth connection. Managed auth controls the profile, headless mode, timeout, start URL, kiosk mode, and viewport.
    """

    captcha_solver: BrowserCaptchaSolverParam
    """Automatic CAPTCHA solving for managed auth browser sessions.

    When provided without stealth, stealth no longer defaults to true. Enabling it
    does not select a proxy: a connection on direct egress stays there; set
    proxy.mode=default for Kernel's default stealth proxy. Turning it off on a
    connection that uses Kernel's default stealth proxy moves it to direct egress.
    Omit on update to keep the current setting, or on login to inherit it.
    """

    location: ManagedAuthBrowserLocationParam
    """
    Browser locale for the connection's login, reauthentication, and health-check
    sessions. Set on create or update; not supported on login.
    """

    proxy: BrowserProxyConfigParam
    """Proxy configuration for managed auth browser sessions.

    Omit on create to derive the default from stealth, or on update and login to
    preserve or inherit the connection default.
    """

    region: Literal["us-east", "us-west", "eu-west", "ap-southeast"]
    """Browser region.

    Omit on create to use us-east, on update to keep the current region, or on login
    to inherit it. Login overrides apply only to that login. Non-default regions
    require an eligible plan and organization access.
    """

    stealth: bool
    """
    Whether managed auth browser sessions use stealth mode: CAPTCHA solving with
    Kernel's default stealth proxy unless proxy is set. Defaults to true when
    neither stealth nor captcha_solver is provided. Cannot be combined with
    captcha_solver.enabled=false. Setting it does not change an existing proxy,
    including direct egress; use proxy.mode=default for Kernel's default stealth
    proxy. Reports true for a connection with only captcha_solver enabled; proxy
    shows its egress. Deprecated in favor of captcha_solver and proxy.
    """

    telemetry: Optional[Telemetry]
    """Browser telemetry configuration using the same semantics as browser create."""
