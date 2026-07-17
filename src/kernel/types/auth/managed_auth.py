# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ManagedAuth",
    "Choice",
    "Credential",
    "DiscoveredField",
    "Field",
    "MfaOption",
    "PendingSSOButton",
    "SignInOption",
]


class Choice(BaseModel):
    """Canonical auth-flow choice awaiting user selection."""

    id: str
    """Stable choice identifier for canonical submit."""

    label: str
    """Human-readable choice label."""

    type: Literal[
        "mfa_method", "sso_provider", "sign_in_method", "auth_method", "identifier_method", "account", "other"
    ]
    """Choice type."""

    description: Optional[str] = None
    """Additional context for the choice."""

    observed_selector: Optional[str] = None
    """Selector for the visible choice, when available."""


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

    hint: Optional[str] = None
    """
    Contextual help text near the field that tells the user what to enter (e.g.,
    "Enter the phone ending in (**_) _**-\\**\\**92")
    """

    linked_mfa_type: Optional[Literal["sms", "call", "email", "totp", "push", "password", "switch"]] = None
    """
    If this field is associated with an MFA option, the type of that option (e.g.,
    password field linked to "Enter password" option)
    """

    placeholder: Optional[str] = None
    """Field placeholder"""

    required: Optional[bool] = None
    """Whether field is required"""


class Field(BaseModel):
    """Canonical field awaiting user input."""

    id: str
    """Stable field identifier for canonical submit."""

    ref: str
    """Credential reference name to store the submitted value under."""

    type: Literal["identifier", "password", "code", "totp_code", "totp_secret", "text"]
    """Managed-auth field type."""

    label: Optional[str] = None
    """Human-readable label shown to the user."""

    observed_selector: Optional[str] = None
    """Selector for the visible field, when available."""

    required: Optional[bool] = None
    """Whether this field is required."""


class MfaOption(BaseModel):
    """An MFA method option for verification"""

    label: str
    """The visible option text"""

    type: Literal["sms", "call", "email", "totp", "push", "password", "switch"]
    """The MFA delivery method type.

    Includes 'password' for auth method selection pages and 'switch' for generic
    method-switcher links like "Use another method" that do not name a specific
    method.
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


class SignInOption(BaseModel):
    """A non-MFA choice presented during the auth flow (e.g.

    account selection, org picker)
    """

    id: str
    """Unique identifier for this option (used to submit selection back)"""

    label: str
    """Display text for the option"""

    description: Optional[str] = None
    """Additional context such as email address or org name"""


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

    record_session: bool
    """Whether to record browser session replays for this connection by default.

    Useful for debugging login flows. Can be overridden per-login.
    """

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

    auto_reauth: Optional[bool] = None
    """Whether automatic re-authentication is permitted for this connection.

    This is an opt-in flag only — it does not check whether re-auth is actually
    feasible. Even when true, re-auth only runs when the system has what it needs to
    perform it (for example, saved credentials for the required login fields), and
    only after a scheduled health check detects an expired session — so this flag
    has no effect when `health_checks` is false. When false, expired sessions
    detected by a health check are marked as `NEEDS_AUTH` instead of attempting
    re-auth.
    """

    browser_session_id: Optional[str] = None
    """
    ID of the underlying browser session driving the current flow (present when flow
    in progress). Use this to inspect or terminate the browser session via the
    `/browsers` API.
    """

    can_reauth: Optional[bool] = None
    """
    Whether Kernel can automatically re-authenticate this connection when the
    session expires. Requires a prior successful login plus either a Kernel
    credential or an external credential reference. See `can_reauth_reason` for the
    specific outcome.
    """

    can_reauth_reason: Optional[
        Literal[
            "external_credential",
            "cua_has_credential",
            "has_credential",
            "viable_plans_found",
            "no_requirements_recorded",
            "requirements_satisfiable",
            "no_prior_successful_login",
            "no_credential",
            "no_viable_plans",
            "viable_plans_require_external_action",
            "requires_external_action",
            "requires_totp_without_secret",
            "requires_sms_code",
            "requires_email_code",
        ]
    ] = None
    """
    Machine-readable reason for the current value of `can_reauth`. Affirmative
    values (re-auth is possible):

    - `external_credential` — an external credential provider is attached
    - `cua_has_credential` — CUA flow with a stored credential
    - `has_credential` — Kernel credential is attached (optimistic; plan viability
      not checked)
    - `viable_plans_found` — at least one stored login plan can be replayed
    - `no_requirements_recorded` — no recorded credential requirements to fail
      against
    - `requirements_satisfiable` — recorded requirements can be met by the attached
      credential

    Negative values (a human must complete the login flow):

    - `no_prior_successful_login` — connection has never completed a successful
      login
    - `no_credential` — no Kernel or external credential attached
    - `no_viable_plans` — credential attached but no replayable login plan exists
      yet
    - `viable_plans_require_external_action` — stored plans need an external step
      (email link, push, etc.)
    - `requires_external_action` — recorded requirements include an external step
    - `requires_totp_without_secret` — flow needs a TOTP code but no TOTP secret is
      stored
    - `requires_sms_code` — flow needs an SMS code that cannot be received
      automatically
    - `requires_email_code` — flow needs an email code that cannot be received
      automatically
    """

    choices: Optional[List[Choice]] = None
    """Canonical choices awaiting selection.

    Prefer this over pending_sso_buttons, mfa_options, and sign_in_options when
    present.
    """

    credential: Optional[Credential] = None
    """Reference to credentials for the auth connection. Use one of:

    - { name } for Kernel credentials
    - { provider, path } for external provider item
    - { provider, auto: true } for external provider domain lookup
    """

    discovered_fields: Optional[List[DiscoveredField]] = None
    """
    Fields awaiting input (present when flow_step=awaiting_input; may also be
    present with awaiting_external_action as fallback actions)
    """

    error_code: Optional[str] = None
    """Machine-readable error code (present when flow_status=failed)"""

    error_message: Optional[str] = None
    """Error message (present when flow_status=failed)"""

    external_action_message: Optional[str] = None
    """
    Instructions for external action (present when
    flow_step=awaiting_external_action)
    """

    fields: Optional[List[Field]] = None
    """Canonical fields awaiting input.

    Prefer this over discovered_fields when present.
    """

    flow_expires_at: Optional[datetime] = None
    """When the current flow expires (null when no flow in progress).

    A flow past this timestamp is no longer valid and its `flow_status` will be
    `EXPIRED`. Clients may start a new login to supersede a stale `IN_PROGRESS` flow
    past this timestamp.
    """

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

    health_checks: Optional[bool] = None
    """Whether periodic health checks are enabled for this connection.

    When false, the system will not automatically verify authentication status, and
    `auto_reauth` has no effect on the automatic flow (since re-auth is only
    triggered by a failed scheduled health check). Manually triggering a health
    check via the API still works regardless of this setting.
    """

    hosted_url: Optional[str] = None
    """URL to redirect user to for hosted login (present when flow in progress)"""

    last_auth_at: Optional[datetime] = None
    """Deprecated alias for `last_auth_check_at`.

    Despite the name, this is the last health-check timestamp, not the last
    successful authentication. Use `last_auth_check_at` instead.
    """

    last_auth_check_at: Optional[datetime] = None
    """
    When the most recent auth health check ran for this connection, regardless of
    outcome. Updated on every health check and does not by itself indicate that the
    profile is currently authenticated - use `status` for that. May be newer than
    `flow_expires_at` when a flow is still in progress because health checks
    continue to run in parallel.
    """

    live_view_url: Optional[str] = None
    """Browser live view URL for debugging (present when flow in progress)"""

    login_url: Optional[str] = None
    """Optional login page URL to skip discovery"""

    mfa_options: Optional[List[MfaOption]] = None
    """
    MFA method options (present when flow_step=awaiting_input; may also be present
    with awaiting_external_action as fallback actions)
    """

    pending_sso_buttons: Optional[List[PendingSSOButton]] = None
    """
    SSO buttons available (present when flow_step=awaiting_input; may also be
    present with awaiting_external_action as fallback actions)
    """

    post_login_url: Optional[str] = None
    """URL where the browser landed after successful login"""

    proxy_id: Optional[str] = None
    """ID of the proxy associated with this connection, if any."""

    sign_in_options: Optional[List[SignInOption]] = None
    """
    Non-MFA choices presented during the auth flow, such as account selection or org
    pickers (present when flow_step=awaiting_input; may also be present with
    awaiting_external_action as fallback actions).
    """

    sso_provider: Optional[str] = None
    """SSO provider being used (e.g., google, github, microsoft)"""

    website_error: Optional[str] = None
    """Visible error message from the website (e.g., 'Incorrect password').

    Present when the website displays an error during login.
    """
