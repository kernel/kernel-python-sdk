# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from .managed_auth_browser_config_param import ManagedAuthBrowserConfigParam
from ..browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = [
    "ConnectionUpdateParams",
    "BrowserTelemetry",
    "BrowserTelemetryExport",
    "BrowserTelemetryExportOtlp",
    "BrowserTelemetryExportOtlpDestination",
    "Credential",
    "Proxy",
]


class ConnectionUpdateParams(TypedDict, total=False):
    allowed_domains: SequenceNotStr[str]
    """Additional domains valid for this auth flow (replaces existing list)"""

    auto_reauth: bool
    """Whether automatic re-authentication is permitted for this connection.

    This is an opt-in flag only — it does not check whether re-auth is actually
    feasible. Even when true, re-auth only runs when the system has what it needs to
    perform it (for example, saved credentials for the required login fields), and
    only after a scheduled health check detects an expired session — so this flag
    has no effect when `health_checks` is false. When false, expired sessions
    detected by a health check are marked as `NEEDS_AUTH` instead of attempting
    re-auth.
    """

    browser: ManagedAuthBrowserConfigParam
    """
    Browser configuration updates for future login, reauthentication, and
    health-check sessions. Omitted properties remain unchanged.
    """

    browser_telemetry: Optional[BrowserTelemetry]
    """Deprecated.

    Use browser.telemetry. Retained during migration for existing clients.
    """

    credential: Credential
    """Reference to credentials for the auth connection. Use one of:

    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    health_check_interval: int
    """Interval in seconds between automatic health checks"""

    health_checks: bool
    """Whether periodic health checks are enabled.

    When set to false, the system will not automatically verify authentication
    status, and `auto_reauth` has no effect on the automatic flow (since re-auth is
    only triggered by a failed scheduled health check).
    """

    login_url: str
    """Login page URL. Set to empty string to clear."""

    proxy: Proxy
    """Deprecated. Use browser.proxy. Retained during migration for existing clients."""

    record_session: bool
    """Whether to record browser sessions for this connection by default"""

    save_credentials: bool
    """Whether to save credentials after every successful login"""


class BrowserTelemetryExportOtlpDestination(TypedDict, total=False):
    """OTLP destination to export this session's captured telemetry to.

    Provide either id or name. Requires telemetry capture to be enabled.
    """

    id: str
    """OTLP destination ID"""

    name: str
    """OTLP destination name"""


class BrowserTelemetryExportOtlp(TypedDict, total=False):
    """
    Export captured telemetry over OTLP to one of the org's configured destinations.
    """

    destination: BrowserTelemetryExportOtlpDestination
    """OTLP destination to export this session's captured telemetry to.

    Provide either id or name. Requires telemetry capture to be enabled.
    """

    enabled: bool
    """Whether to export captured telemetry over OTLP.

    Setting destination implies enabled=true, so this only needs to be set
    explicitly to disable export (enabled=false with a destination is rejected).
    """


class BrowserTelemetryExport(TypedDict, total=False):
    """Where to export this session's captured telemetry.

    Omit to capture without exporting.
    """

    otlp: BrowserTelemetryExportOtlp
    """
    Export captured telemetry over OTLP to one of the org's configured destinations.
    """


class BrowserTelemetry(TypedDict, total=False):
    """Deprecated.

    Use browser.telemetry. Retained during migration for existing clients.
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

    export: BrowserTelemetryExport
    """Where to export this session's captured telemetry.

    Omit to capture without exporting.
    """


class Credential(TypedDict, total=False):
    """Reference to credentials for the auth connection.

    Use one of:
    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    auto: bool
    """If true, lookup by domain from the specified provider"""

    name: str
    """Kernel credential name"""

    path: str
    """Provider-specific path (e.g., "VaultName/ItemName" for 1Password)"""

    provider: str
    """External provider name (e.g., "my-1p")"""


class Proxy(TypedDict, total=False):
    """Deprecated. Use browser.proxy. Retained during migration for existing clients."""

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
