# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .credential_vault_field_type import CredentialVaultFieldType

__all__ = ["CredentialVaultFieldDefinition"]


class CredentialVaultFieldDefinition(BaseModel):
    name: str
    """Stable field name used to key values, updates, and browser fills."""

    required: bool
    """Whether a nonempty value is required for readiness and form submission."""

    sensitive: bool
    """Whether the value is omitted from every item response.

    Reserve true for secrets such as passwords, API tokens, and TOTP seeds. Ordinary
    usernames and email addresses should be false so the form can display and
    prefill them.
    """

    type: CredentialVaultFieldType
    """
    Text, email, and password have form inputs; totp does not and is omitted from
    both Kernel-hosted and customer React forms. Password and totp must be
    sensitive. A totp value is an RFC 4648 Base32 generator seed (case-insensitive,
    optional trailing padding), not an otpauth URI or current code. Reject invalid
    or empty decoded seeds. Browser fill generates an RFC 6238 code at execution
    time using HMAC-SHA1, 6 digits, and a 30-second period. Preserve leading zeros;
    never fill the seed. Custom algorithms, digits, periods, and form enrollment are
    unsupported.
    """
