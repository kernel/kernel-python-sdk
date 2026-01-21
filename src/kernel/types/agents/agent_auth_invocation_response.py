# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .discovered_field import DiscoveredField

__all__ = ["AgentAuthInvocationResponse", "MfaOption", "PendingSSOButton"]


class MfaOption(BaseModel):
    """An MFA method option for verification"""

    label: str
    """The visible option text"""

    type: Literal["sms", "call", "email", "totp", "push", "security_key"]
    """The MFA delivery method type"""

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


class AgentAuthInvocationResponse(BaseModel):
    """Response from get invocation endpoint"""

    app_name: str
    """App name (org name at time of invocation creation)"""

    domain: str
    """Domain for authentication"""

    expires_at: datetime
    """When the handoff code expires"""

    status: Literal["IN_PROGRESS", "SUCCESS", "EXPIRED", "CANCELED", "FAILED"]
    """Invocation status"""

    step: Literal[
        "initialized", "discovering", "awaiting_input", "awaiting_external_action", "submitting", "completed", "expired"
    ]
    """Current step in the invocation workflow"""

    type: Literal["login", "auto_login", "reauth"]
    """The invocation type:

    - login: First-time authentication
    - reauth: Re-authentication for previously authenticated agents
    - auto_login: Legacy type (no longer created, kept for backward compatibility)
    """

    error_message: Optional[str] = None
    """Error message explaining why the invocation failed (present when status=FAILED)"""

    external_action_message: Optional[str] = None
    """
    Instructions for user when external action is required (present when
    step=awaiting_external_action)
    """

    live_view_url: Optional[str] = None
    """Browser live view URL for debugging the invocation"""

    mfa_options: Optional[List[MfaOption]] = None
    """
    MFA method options to choose from (present when step=awaiting_input and MFA
    selection is required)
    """

    pending_fields: Optional[List[DiscoveredField]] = None
    """Fields currently awaiting input (present when step=awaiting_input)"""

    pending_sso_buttons: Optional[List[PendingSSOButton]] = None
    """SSO buttons available on the page (present when step=awaiting_input)"""

    sso_provider: Optional[str] = None
    """SSO provider being used for authentication (e.g., google, github, microsoft)"""

    submitted_fields: Optional[List[str]] = None
    """
    Names of fields that have been submitted (present when step=submitting or later)
    """
