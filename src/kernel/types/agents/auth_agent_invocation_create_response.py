# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuthAgentInvocationCreateResponse"]


class AuthAgentInvocationCreateResponse(BaseModel):
    """Response from creating an invocation. Always returns an invocation_id."""

    expires_at: datetime
    """When the handoff code expires."""

    handoff_code: str
    """One-time code for handoff."""

    hosted_url: str
    """URL to redirect user to."""

    invocation_id: str
    """Unique identifier for the invocation."""

    type: Literal["login", "auto_login", "reauth"]
    """The invocation type:

    - login: First-time authentication
    - reauth: Re-authentication for previously authenticated agents
    - auto_login: Legacy type (no longer created, kept for backward compatibility)
    """
