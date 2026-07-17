# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..shared.error_event import ErrorEvent
from ..shared.heartbeat_event import HeartbeatEvent

__all__ = [
    "ConnectionFollowResponse",
    "ManagedAuthStateEvent",
    "ManagedAuthStateEventChoice",
    "ManagedAuthStateEventDiscoveredField",
    "ManagedAuthStateEventField",
    "ManagedAuthStateEventMfaOption",
    "ManagedAuthStateEventPendingSSOButton",
    "ManagedAuthStateEventSignInOption",
]


class ManagedAuthStateEventChoice(BaseModel):
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


class ManagedAuthStateEventDiscoveredField(BaseModel):
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


class ManagedAuthStateEventField(BaseModel):
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


class ManagedAuthStateEventMfaOption(BaseModel):
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


class ManagedAuthStateEventPendingSSOButton(BaseModel):
    """An SSO button for signing in with an external identity provider"""

    label: str
    """Visible button text"""

    provider: str
    """Identity provider name"""

    selector: str
    """XPath selector for the button"""


class ManagedAuthStateEventSignInOption(BaseModel):
    """A non-MFA choice presented during the auth flow (e.g.

    account selection, org picker)
    """

    id: str
    """Unique identifier for this option (used to submit selection back)"""

    label: str
    """Display text for the option"""

    description: Optional[str] = None
    """Additional context such as email address or org name"""


class ManagedAuthStateEvent(BaseModel):
    """An event representing the current state of a managed auth flow."""

    event: Literal["managed_auth_state"]
    """Event type identifier (always "managed_auth_state")."""

    flow_status: Literal["IN_PROGRESS", "SUCCESS", "FAILED", "EXPIRED", "CANCELED"]
    """Current flow status."""

    flow_step: Literal["DISCOVERING", "AWAITING_INPUT", "AWAITING_EXTERNAL_ACTION", "SUBMITTING", "COMPLETED"]
    """Current step in the flow."""

    timestamp: datetime
    """Time the state was reported."""

    choices: Optional[List[ManagedAuthStateEventChoice]] = None
    """Canonical choices awaiting selection.

    Prefer this over pending_sso_buttons, mfa_options, and sign_in_options when
    present.
    """

    discovered_fields: Optional[List[ManagedAuthStateEventDiscoveredField]] = None
    """
    Fields awaiting input (present when flow_step=AWAITING_INPUT; may also be
    present with AWAITING_EXTERNAL_ACTION as fallback actions).
    """

    error_code: Optional[str] = None
    """Machine-readable error code (present when flow_status=FAILED)."""

    error_message: Optional[str] = None
    """Error message (present when flow_status=FAILED)."""

    external_action_message: Optional[str] = None
    """
    Instructions for external action (present when
    flow_step=AWAITING_EXTERNAL_ACTION).
    """

    fields: Optional[List[ManagedAuthStateEventField]] = None
    """Canonical fields awaiting input.

    Prefer this over discovered_fields when present.
    """

    flow_type: Optional[Literal["LOGIN", "REAUTH"]] = None
    """Type of the current flow."""

    hosted_url: Optional[str] = None
    """URL to redirect user to for hosted login."""

    live_view_url: Optional[str] = None
    """Browser live view URL for debugging."""

    mfa_options: Optional[List[ManagedAuthStateEventMfaOption]] = None
    """
    MFA method options (present when flow_step=AWAITING_INPUT; may also be present
    with AWAITING_EXTERNAL_ACTION as fallback actions).
    """

    pending_sso_buttons: Optional[List[ManagedAuthStateEventPendingSSOButton]] = None
    """
    SSO buttons available (present when flow_step=AWAITING_INPUT; may also be
    present with AWAITING_EXTERNAL_ACTION as fallback actions).
    """

    post_login_url: Optional[str] = None
    """URL where the browser landed after successful login."""

    sign_in_options: Optional[List[ManagedAuthStateEventSignInOption]] = None
    """
    Non-MFA choices presented during the auth flow, such as account selection or org
    pickers (present when flow_step=AWAITING_INPUT; may also be present with
    AWAITING_EXTERNAL_ACTION as fallback actions).
    """

    website_error: Optional[str] = None
    """Visible error message from the website (e.g., 'Incorrect password').

    Present when the website displays an error during login.
    """


ConnectionFollowResponse: TypeAlias = Annotated[
    Union[ManagedAuthStateEvent, ErrorEvent, HeartbeatEvent], PropertyInfo(discriminator="event")
]
