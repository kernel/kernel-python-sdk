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
    "ManagedAuthStateEventDiscoveredField",
    "ManagedAuthStateEventMfaOption",
    "ManagedAuthStateEventPendingSSOButton",
]


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

    linked_mfa_type: Optional[Literal["sms", "call", "email", "totp", "push", "password"]] = None
    """
    If this field is associated with an MFA option, the type of that option (e.g.,
    password field linked to "Enter password" option)
    """

    placeholder: Optional[str] = None
    """Field placeholder"""

    required: Optional[bool] = None
    """Whether field is required"""


class ManagedAuthStateEventMfaOption(BaseModel):
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


class ManagedAuthStateEventPendingSSOButton(BaseModel):
    """An SSO button for signing in with an external identity provider"""

    label: str
    """Visible button text"""

    provider: str
    """Identity provider name"""

    selector: str
    """XPath selector for the button"""


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

    discovered_fields: Optional[List[ManagedAuthStateEventDiscoveredField]] = None
    """Fields awaiting input (present when flow_step=AWAITING_INPUT)."""

    error_code: Optional[str] = None
    """Machine-readable error code (present when flow_status=FAILED)."""

    error_message: Optional[str] = None
    """Error message (present when flow_status=FAILED)."""

    external_action_message: Optional[str] = None
    """
    Instructions for external action (present when
    flow_step=AWAITING_EXTERNAL_ACTION).
    """

    flow_type: Optional[Literal["LOGIN", "REAUTH"]] = None
    """Type of the current flow."""

    hosted_url: Optional[str] = None
    """URL to redirect user to for hosted login."""

    live_view_url: Optional[str] = None
    """Browser live view URL for debugging."""

    mfa_options: Optional[List[ManagedAuthStateEventMfaOption]] = None
    """
    MFA method options (present when flow_step=AWAITING_INPUT and MFA selection
    required).
    """

    pending_sso_buttons: Optional[List[ManagedAuthStateEventPendingSSOButton]] = None
    """SSO buttons available (present when flow_step=AWAITING_INPUT)."""

    post_login_url: Optional[str] = None
    """URL where the browser landed after successful login."""

    website_error: Optional[str] = None
    """Visible error message from the website (e.g., 'Incorrect password').

    Present when the website displays an error during login.
    """


ConnectionFollowResponse: TypeAlias = Annotated[
    Union[ManagedAuthStateEvent, ErrorEvent, HeartbeatEvent], PropertyInfo(discriminator="event")
]
