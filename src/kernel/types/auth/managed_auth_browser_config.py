# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..browser_proxy_config import BrowserProxyConfig
from ..browser_captcha_solver import BrowserCaptchaSolver
from .managed_auth_browser_location import ManagedAuthBrowserLocation
from ..browsers.browser_telemetry_categories_config import BrowserTelemetryCategoriesConfig

__all__ = [
    "ManagedAuthBrowserConfig",
    "Telemetry",
    "TelemetryExport",
    "TelemetryExportOtlp",
    "TelemetryExportOtlpDestination",
    "TelemetryStorage",
]


class TelemetryExportOtlpDestination(BaseModel):
    """OTLP destination to export this session's captured telemetry to.

    Provide either id or name. Requires telemetry capture to be enabled.
    """

    id: Optional[str] = None
    """OTLP destination ID"""

    name: Optional[str] = None
    """OTLP destination name"""


class TelemetryExportOtlp(BaseModel):
    """
    Export captured telemetry over OTLP to one of the org's configured destinations.
    """

    destination: Optional[TelemetryExportOtlpDestination] = None
    """OTLP destination to export this session's captured telemetry to.

    Provide either id or name. Requires telemetry capture to be enabled.
    """

    enabled: Optional[bool] = None
    """Whether to export captured telemetry over OTLP.

    Setting destination implies enabled=true, so this only needs to be set
    explicitly to disable export (enabled=false with a destination is rejected).
    """


class TelemetryExport(BaseModel):
    """Where to export this session's captured telemetry.

    Omit to capture without exporting.
    """

    otlp: Optional[TelemetryExportOtlp] = None
    """
    Export captured telemetry over OTLP to one of the org's configured destinations.
    """


class TelemetryStorage(BaseModel):
    """Whether to persist this session's captured telemetry to Kernel storage."""

    enabled: Optional[bool] = None
    """Whether captured telemetry is persisted to Kernel storage.

    Defaults to true. Setting false requires an OTLP destination and cannot be
    changed after the browser is created.
    """


class Telemetry(BaseModel):
    """Browser telemetry configuration using the same semantics as browser create."""

    browser: Optional[BrowserTelemetryCategoriesConfig] = None
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

    enabled: Optional[bool] = None
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

    export: Optional[TelemetryExport] = None
    """Where to export this session's captured telemetry.

    Omit to capture without exporting.
    """

    storage: Optional[TelemetryStorage] = None
    """Whether to persist this session's captured telemetry to Kernel storage."""


class ManagedAuthBrowserConfig(BaseModel):
    """
    Browser configuration applied to browser sessions created for a managed auth connection. Managed auth controls the profile, headless mode, timeout, start URL, kiosk mode, and viewport.
    """

    captcha_solver: Optional[BrowserCaptchaSolver] = None
    """Automatic CAPTCHA solving for managed auth browser sessions.

    When provided without stealth, stealth no longer defaults to true. Enabling it
    does not select a proxy: a connection on direct egress stays there; set
    proxy.mode=default for Kernel's default stealth proxy. Turning it off on a
    connection that uses Kernel's default stealth proxy moves it to direct egress.
    Omit on update to keep the current setting, or on login to inherit it.
    """

    location: Optional[ManagedAuthBrowserLocation] = None
    """
    Browser locale for the connection's login, reauthentication, and health-check
    sessions. Set on create or update; not supported on login.
    """

    proxy: Optional[BrowserProxyConfig] = None
    """Proxy configuration for managed auth browser sessions.

    Omit on create to derive the default from stealth, or on update and login to
    preserve or inherit the connection default.
    """

    region: Optional[Literal["us-east", "us-west", "eu-west", "ap-southeast"]] = None
    """Browser region.

    Omit on create to use us-east, on update to keep the current region, or on login
    to inherit it. Login overrides apply only to that login. Non-default regions
    require an eligible plan and organization access.
    """

    stealth: Optional[bool] = None
    """
    Whether managed auth browser sessions use stealth mode: CAPTCHA solving with
    Kernel's default stealth proxy unless proxy is set. Defaults to true when
    neither stealth nor captcha_solver is provided. Cannot be combined with
    captcha_solver.enabled=false. Setting it does not change an existing proxy,
    including direct egress; use proxy.mode=default for Kernel's default stealth
    proxy. Reports true for a connection with only captcha_solver enabled; proxy
    shows its egress. Deprecated in favor of captcha_solver and proxy.
    """

    telemetry: Optional[Telemetry] = None
    """Browser telemetry configuration using the same semantics as browser create."""
