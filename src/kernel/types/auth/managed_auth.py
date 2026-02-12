# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ManagedAuth", "Credential", "DiscoveredField", "MfaOption", "PendingSSOButton"]


class Credential(BaseModel):
    """Reference to credentials for the auth connection.

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


class DiscoveredField(BaseModel):
    """A discovered form field"""

    label: str
    """Field label"""

    name: str
    """Field name"""

    selector: str
    """CSS selector for the field"""

    type: Literal["text", "email", "password", "tel", "number", "url", "code", "totp"]
    """Field type"""

    linked_mfa_type: Optional[Literal["sms", "call", "email", "totp", "push", "password"]] = None
    """
    If this field is associated with an MFA option, the type of that option (e.g.,
    password field linked to "Enter password" option)
    """

    placeholder: Optional[str] = None
    """Field placeholder"""

    required: Optional[bool] = None
    """Whether field is required"""


class MfaOption(BaseModel):
    """An MFA method option for verification"""

    label: str
    """The visible option text"""

    type: Literal["sms", "call", "email", "totp", "push", "password"]
    """
    The MFA delivery method type (includes password for auth method selection pages)
    """

    description: Optional[str] = None
    """Additional instructions from the site"""

    target: Optional[str] = None
    """The masked destination (phone/email) if shown"""


class PendingSSOButton(BaseModel):
    """An SSO button for signing in with an external identity provider"""

    label: str
    """Visible button text"""

    provider: str
    """Identity provider name"""

    selector: str
    """XPath selector for the button"""


class ManagedAuth(BaseModel):
    """Managed authentication that keeps a profile logged into a specific domain.

    Flow fields (flow_status, flow_step, discovered_fields, mfa_options) reflect the most recent login flow and are null when no flow has been initiated.
    """

    id: str
    """Unique identifier for the auth connection"""

    domain: str
    """Target domain for authentication"""

    profile_name: str
    """Name of the profile associated with this auth connection"""

    save_credentials: bool
    """Whether credentials are saved after every successful login.

    One-time codes (TOTP, SMS, etc.) are not saved.
    """

    status: Literal["AUTHENTICATED", "NEEDS_AUTH"]
    """Current authentication status of the managed profile"""

    allowed_domains: Optional[List[str]] = None
    """
    Additional domains that are valid for this auth flow (besides the primary
    domain). Useful when login pages redirect to different domains.

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
    Whether automatic re-authentication is possible (has credential, selectors, and
    login_url)
    """

    can_reauth_reason: Optional[str] = None
    """Reason why automatic re-authentication is or is not possible"""

    credential: Optional[Credential] = None
    """Reference to credentials for the auth connection. Use one of:

    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    discovered_fields: Optional[List[DiscoveredField]] = None
    """Fields awaiting input (present when flow_step=awaiting_input)"""

    error_code: Optional[str] = None
    """Machine-readable error code (present when flow_status=failed)"""

    error_message: Optional[str] = None
    """Error message (present when flow_status=failed)"""

    external_action_message: Optional[str] = None
    """
    Instructions for external action (present when
    flow_step=awaiting_external_action)
    """

    flow_expires_at: Optional[datetime] = None
    """When the current flow expires (null when no flow in progress)"""

    flow_status: Optional[Literal["IN_PROGRESS", "SUCCESS", "FAILED", "EXPIRED", "CANCELED"]] = None
    """Current flow status (null when no flow in progress)"""

    flow_step: Optional[
        Literal["DISCOVERING", "AWAITING_INPUT", "AWAITING_EXTERNAL_ACTION", "SUBMITTING", "COMPLETED"]
    ] = None
    """Current step in the flow (null when no flow in progress)"""

    flow_type: Optional[Literal["LOGIN", "REAUTH"]] = None
    """Type of the current flow (null when no flow in progress)"""

    health_check_interval: Optional[int] = None
    """Interval in seconds between automatic health checks.

    When set, the system periodically verifies the authentication status and
    triggers re-authentication if needed. Maximum is 86400 (24 hours). Default is
    3600 (1 hour). The minimum depends on your plan: Enterprise: 300 (5 minutes),
    Startup: 1200 (20 minutes), Hobbyist: 3600 (1 hour).
    """

    hosted_url: Optional[str] = None
    """URL to redirect user to for hosted login (present when flow in progress)"""

    last_auth_at: Optional[datetime] = None
    """When the profile was last successfully authenticated"""

    live_view_url: Optional[str] = None
    """Browser live view URL for debugging (present when flow in progress)"""

    mfa_options: Optional[List[MfaOption]] = None
    """
    MFA method options (present when flow_step=awaiting_input and MFA selection
    required)
    """

    pending_sso_buttons: Optional[List[PendingSSOButton]] = None
    """SSO buttons available (present when flow_step=awaiting_input)"""

    post_login_url: Optional[str] = None
    """URL where the browser landed after successful login"""

    proxy_id: Optional[str] = None
    """ID of the proxy associated with this connection, if any."""

    sso_provider: Optional[str] = None
    """SSO provider being used (e.g., google, github, microsoft)"""

    website_error: Optional[str] = None
    """Visible error message from the website (e.g., 'Incorrect password').

    Present when the website displays an error during login.
    """
