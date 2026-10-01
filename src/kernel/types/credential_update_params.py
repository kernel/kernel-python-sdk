# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    name: str
    """New name for the credential"""

    remove_value_keys: SequenceNotStr[str]
    """Field names to remove from the credential's stored values.

    Removals are applied before `values` are merged, so a key present in both is
    kept with its new value.
    """

    sso_provider: Optional[str]
    """If set, indicates this credential should be used with the specified SSO
    provider.

    Set to empty string or null to remove.
    """

    totp_algorithm: Literal["SHA1", "SHA256", "SHA512"]
    """HMAC algorithm used to generate TOTP codes.

    Requires totp_secret and is ignored when an `otpauth://` URI supplies the
    algorithm.
    """

    totp_digits: int
    """Number of digits in generated TOTP codes.

    Requires totp_secret and is ignored when an `otpauth://` URI supplies the digit
    count.
    """

    totp_period: int
    """TOTP rotation period in seconds.

    Requires totp_secret and is ignored when an `otpauth://` URI supplies the
    period.
    """

    totp_secret: str
    """
    Accepts a 16-128 character base32-encoded TOTP secret or an `otpauth://totp/...`
    URI. Only URI parameters present override the corresponding explicit TOTP
    fields. When rotating a raw secret, omitted fields preserve their existing
    values; a new URI defaults unspecified fields to SHA1/6/30. Set to empty string
    to remove the secret and its metadata.
    """

    values: Dict[str, str]
    """Field name to value mapping.

    Values are merged with existing values (new keys added, existing keys
    overwritten).
    """
