# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

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
    """Unique name for the credential within the project"""

    updated_at: datetime
    """When the credential was last updated"""

    has_totp_secret: Optional[bool] = None
    """Whether this credential has a TOTP secret configured for automatic 2FA"""

    has_values: Optional[bool] = None
    """Whether this credential has stored values (email, password, etc.)"""

    sso_provider: Optional[str] = None
    """
    If set, indicates this credential should be used with the specified SSO provider
    (e.g., google, github, microsoft). When the target site has a matching SSO
    button, it will be clicked first before filling credential values on the
    identity provider's login page.
    """

    totp_algorithm: Optional[Literal["SHA1", "SHA256", "SHA512"]] = None
    """HMAC algorithm used to generate TOTP codes.

    Defaults to SHA1 for credentials created before this metadata was stored.
    """

    totp_code: Optional[str] = None
    """Current TOTP code.

    Only included in create/update responses when totp_secret was just set.
    """

    totp_code_expires_at: Optional[datetime] = None
    """When the totp_code expires. Only included when totp_code is present."""

    totp_digits: Optional[int] = None
    """Number of digits in generated TOTP codes.

    Defaults to 6 for credentials created before this metadata was stored.
    """

    totp_period: Optional[int] = None
    """TOTP rotation period in seconds.

    Defaults to 30 for credentials created before this metadata was stored.
    """

    value_keys: Optional[List[str]] = None
    """The field names stored in this credential's values (e.g., username, password).

    Values themselves are never returned. Included on single-credential responses
    (create, get by id or name, update); omitted from list responses.
    """
