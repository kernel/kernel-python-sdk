# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .managed_auth_browser_config_param import ManagedAuthBrowserConfigParam
from ..browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = [
    "ConnectionCreateParams",
    "BrowserTelemetry",
    "BrowserTelemetryExport",
    "BrowserTelemetryExportOtlp",
    "BrowserTelemetryExportOtlpDestination",
    "Credential",
    "Proxy",
]


class ConnectionCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Domain for authentication"""

    profile_name: Required[str]
    """Name of the profile to manage authentication for.

    If the profile does not exist, it is created automatically.
    """

    allowed_domains: SequenceNotStr[str]
    """Additional domains valid for this auth flow (besides the primary domain).

    Useful when login pages redirect to different domains.

    The following SSO/OAuth provider domains are automatically allowed by default
    and do not need to be specified:

    - Google: accounts.google.com
    - Microsoft/Azure AD: login.microsoftonline.com, login.live.com
    - Okta: _.okta.com, _.oktapreview.com
    - Auth0: _.auth0.com, _.us.auth0.com, _.eu.auth0.com, _.au.auth0.com
    - Apple: appleid.apple.com
    - GitHub: github.com
    - Facebook/Meta: www.facebook.com
    - LinkedIn: www.linkedin.com
    - Amazon Cognito: \\**.amazoncognito.com
    - OneLogin: \\**.onelogin.com
    - Ping Identity: _.pingone.com, _.pingidentity.com
    """

    auto_reauth: bool
    """
    Whether to permit automatic re-authentication when a scheduled health check
    detects an expired session. This is an opt-in flag only — it does not check
    whether re-auth is actually feasible. Even when true, re-auth only runs when the
    system has what it needs to perform it (for example, saved credentials for the
    required login fields), and only after a scheduled health check detects an
    expired session — so this flag has no effect when `health_checks` is false. When
    false, expired sessions are marked as `NEEDS_AUTH` instead of attempting
    re-auth. Defaults to true.
    """

    browser: ManagedAuthBrowserConfigParam
    """
    Default browser configuration for login, reauthentication, and health-check
    sessions.
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
    """Interval in seconds between automatic health checks.

    When set, the system periodically verifies the authentication status and
    triggers re-authentication if needed. Maximum is 86400 (24 hours). Default is
    3600 (1 hour) or your plan minimum, whichever is larger. The minimum depends on
    your plan: Enterprise: 300 (5 minutes), Startup: 1200 (20 minutes), Hobbyist:
    3600 (1 hour), Free: 21600 (6 hours).
    """

    health_checks: bool
    """Whether to enable periodic health checks.

    When false, the system will not automatically verify authentication status, and
    `auto_reauth` has no effect on the automatic flow (since re-auth is only
    triggered by a failed scheduled health check). Defaults to true.
    """

    login_url: str
    """Optional login page URL to skip discovery"""

    proxy: Proxy
    """Deprecated. Use browser.proxy. Retained during migration for existing clients."""

    record_session: bool
    """Whether to record browser sessions for this connection by default.

    Useful for debugging. Can be overridden per-login. Defaults to false.
    """

    save_credentials: bool
    """Whether to save credentials after every successful login.

    Defaults to true. One-time codes (TOTP, SMS, etc.) are not saved.
    """


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
