# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuthAgent"]


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
    """

    can_reauth: Optional[bool] = None
    """
    Whether automatic re-authentication is possible (has credential_id, selectors,
    and login_url)
    """

    credential_id: Optional[str] = None
    """ID of the linked credential for automatic re-authentication"""

    credential_name: Optional[str] = None
    """Name of the linked credential for automatic re-authentication"""

    has_selectors: Optional[bool] = None
    """
    Whether this auth agent has stored selectors for deterministic re-authentication
    """

    last_auth_check_at: Optional[datetime] = None
    """When the last authentication check was performed"""
