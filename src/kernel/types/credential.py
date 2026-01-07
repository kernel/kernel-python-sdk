# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Credential"]


class Credential(BaseModel):
    """A stored credential for automatic re-authentication"""

    id: str
    """Unique identifier for the credential"""

    created_at: datetime
    """When the credential was created"""

    domain: str
    """Target domain this credential is for"""

    name: str
    """Unique name for the credential within the organization"""

    updated_at: datetime
    """When the credential was last updated"""

    has_totp_secret: Optional[bool] = None
    """Whether this credential has a TOTP secret configured for automatic 2FA"""

    sso_provider: Optional[str] = None
    """
    If set, indicates this credential should be used with the specified SSO provider
    (e.g., google, github, microsoft). When the target site has a matching SSO
    button, it will be clicked first before filling credential values on the
    identity provider's login page.
    """

    totp_code: Optional[str] = None
    """Current 6-digit TOTP code.

    Only included in create/update responses when totp_secret was just set.
    """

    totp_code_expires_at: Optional[datetime] = None
    """When the totp_code expires. Only included when totp_code is present."""
