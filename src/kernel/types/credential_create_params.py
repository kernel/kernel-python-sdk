# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Target domain this credential is for"""

    name: Required[str]
    """Unique name for the credential within the project"""

    values: Required[Dict[str, str]]
    """Field name to value mapping (e.g., username, password)"""

    sso_provider: str
    """
    If set, indicates this credential should be used with the specified SSO provider
    (e.g., google, github, microsoft). When the target site has a matching SSO
    button, it will be clicked first before filling credential values on the
    identity provider's login page.
    """

    totp_algorithm: Literal["SHA1", "SHA256", "SHA512"]
    """HMAC algorithm used to generate TOTP codes.

    Defaults to SHA1 and is ignored when an `otpauth://` URI supplies the algorithm.
    """

    totp_digits: int
    """Number of digits in generated TOTP codes.

    Defaults to 6 and is ignored when an `otpauth://` URI supplies the digit count.
    """

    totp_period: int
    """TOTP rotation period in seconds.

    Defaults to 30 and is ignored when an `otpauth://` URI supplies the period.
    """

    totp_secret: str
    """
    Accepts a 16-128 character base32-encoded TOTP secret or an `otpauth://totp/...`
    URI. The range accepts existing shorter seeds and longer seeds regardless of
    HMAC algorithm; RFC 6238 recommends unpadded base32 lengths of 32/52/103 for
    SHA1/SHA256/SHA512. Only URI parameters present override the corresponding
    explicit TOTP fields. Used for automatic 2FA during login.
    """
