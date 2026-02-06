# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuthAgent", "Credential"]


class Credential(BaseModel):
    """Reference to credentials for managed auth.

    Use one of:
    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    auto: Optional[bool] = None
    """If true, lookup by domain from the specified provider"""

    name: Optional[str] = None
    """Kernel credential name"""

    path: Optional[str] = None
    """Provider-specific path (e.g., "VaultName/ItemName" for 1Password)"""

    provider: Optional[str] = None
    """External provider name (e.g., "my-1p")"""


class AuthAgent(BaseModel):
    """
    An auth agent that manages authentication for a specific domain and profile combination
    """

    id: str
    """Unique identifier for the auth agent"""

    domain: str
    """Target domain for authentication"""

    profile_name: str
    """Name of the profile associated with this auth agent"""

    status: Literal["AUTHENTICATED", "NEEDS_AUTH"]
    """Current authentication status of the managed profile"""

    allowed_domains: Optional[List[str]] = None
    """
    Additional domains that are valid for this auth agent's authentication flow
    (besides the primary domain). Useful when login pages redirect to different
    domains.

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

    can_reauth: Optional[bool] = None
    """
    Whether automatic re-authentication is possible (has credential_id, selectors,
    and login_url)
    """

    credential: Optional[Credential] = None
    """Reference to credentials for managed auth. Use one of:

    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    credential_id: Optional[str] = None
    """
    ID of the linked Kernel credential for automatic re-authentication (deprecated,
    use credential)
    """

    has_selectors: Optional[bool] = None
    """
    Whether this auth agent has stored selectors for deterministic re-authentication
    """

    last_auth_check_at: Optional[datetime] = None
    """When the last authentication check was performed"""

    post_login_url: Optional[str] = None
    """URL where the browser landed after successful login.

    Query parameters and fragments are stripped for privacy.
    """
