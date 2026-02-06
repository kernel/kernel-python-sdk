# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LoginResponse"]


class LoginResponse(BaseModel):
    """Response from starting a login flow"""

    id: str
    """Managed auth ID"""

    flow_expires_at: datetime
    """When the login flow expires"""

    flow_type: Literal["LOGIN", "REAUTH"]
    """Type of login flow started"""

    hosted_url: str
    """URL to redirect user to for login"""

    handoff_code: Optional[str] = None
    """One-time code for handoff (internal use)"""

    live_view_url: Optional[str] = None
    """Browser live view URL for watching the login flow"""
