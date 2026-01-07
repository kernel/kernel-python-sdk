# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Target domain this credential is for"""

    name: Required[str]
    """Unique name for the credential within the organization"""

    values: Required[Dict[str, str]]
    """Field name to value mapping (e.g., username, password)"""

    sso_provider: str
    """
    If set, indicates this credential should be used with the specified SSO provider
    (e.g., google, github, microsoft). When the target site has a matching SSO
    button, it will be clicked first before filling credential values on the
    identity provider's login page.
    """

    totp_secret: str
    """Base32-encoded TOTP secret for generating one-time passwords.

    Used for automatic 2FA during login.
    """
