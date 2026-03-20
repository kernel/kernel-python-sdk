# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ConnectionUpdateParams", "Credential", "Proxy"]


class ConnectionUpdateParams(TypedDict, total=False):
    allowed_domains: SequenceNotStr[str]
    """Additional domains valid for this auth flow (replaces existing list)"""

    credential: Credential
    """Reference to credentials for the auth connection. Use one of:

    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    health_check_interval: int
    """Interval in seconds between automatic health checks"""

    login_url: str
    """Login page URL. Set to empty string to clear."""

    proxy: Proxy
    """Proxy selection.

    Provide either id or name. The proxy must belong to the caller's org.
    """

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

    Provide either id or name. The proxy must belong to the caller's org.
    """

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
