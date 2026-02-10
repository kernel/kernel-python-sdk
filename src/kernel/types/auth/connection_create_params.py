# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ConnectionCreateParams", "Credential", "Proxy"]


class ConnectionCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Domain for authentication"""

    profile_name: Required[str]
    """Name of the profile to manage authentication for"""

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

    credential: Credential
    """Reference to credentials for the auth connection. Use one of:

    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    health_check_interval: int
    """Interval in seconds between automatic health checks.

    When set, the system periodically verifies the authentication status and
    triggers re-authentication if needed. Must be between 300 (5 minutes) and 86400
    (24 hours). Default is 3600 (1 hour).
    """

    login_url: str
    """Optional login page URL to skip discovery"""

    proxy: Proxy
    """Proxy selection.

    Provide either id or name. The proxy must belong to the caller's org.
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
    """Proxy selection.

    Provide either id or name. The proxy must belong to the caller's org.
    """

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
