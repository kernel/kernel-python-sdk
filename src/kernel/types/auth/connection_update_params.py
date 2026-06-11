# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ConnectionUpdateParams", "Credential", "Proxy"]


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
    """Proxy selection.

    Provide either id or name. The proxy must be in the same project as the resource
    referencing it.
    """

    record_session: bool
    """Whether to record browser sessions for this connection by default"""

    save_credentials: bool
    """Whether to save credentials after every successful login"""


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
    """Proxy selection.

    Provide either id or name. The proxy must be in the same project as the resource referencing it.
    """

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
