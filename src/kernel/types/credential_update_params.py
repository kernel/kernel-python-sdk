# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    name: str
    """New name for the credential"""

    sso_provider: Optional[str]
    """If set, indicates this credential should be used with the specified SSO
    provider.

    Set to empty string or null to remove.
    """

    totp_secret: str
    """Base32-encoded TOTP secret for generating one-time passwords.

    Spaces and formatting are automatically normalized. Set to empty string to
    remove.
    """

    values: Dict[str, str]
    """Field name to value mapping.

    Values are merged with existing values (new keys added, existing keys
    overwritten).
    """
