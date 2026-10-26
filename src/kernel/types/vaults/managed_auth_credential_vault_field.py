# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .credential_vault_field_type import CredentialVaultFieldType

__all__ = ["ManagedAuthCredentialVaultField"]


class ManagedAuthCredentialVaultField(BaseModel):
    type: CredentialVaultFieldType
    """
    Text, email, and password have form inputs; totp and passkey do not and are
    omitted from both Kernel-hosted and customer React forms. Password, totp, and
    passkey must be sensitive. A totp value is an RFC 4648 Base32 generator seed
    (case-insensitive, optional trailing padding), not an otpauth URI or current
    code. Reject invalid or empty decoded seeds. Browser fill generates an RFC 6238
    code at execution time using HMAC-SHA1, 6 digits, and a 30-second period.
    Preserve leading zeros; never fill the seed. Custom algorithms, digits, periods,
    and form enrollment are unsupported. A passkey value is a JSON-encoded FIDO
    Credential Exchange Format passkey object with unpadded base64url
    `credentialId`, `userHandle` (at most 64 bytes), and `key` (a PKCS#8 ECDSA P-256
    private key), a lowercase `rpId` domain, and optional `username` and
    `userDisplayName`. Other CXF members are ignored. Passkeys are never filled into
    pages; use arm_passkey to sign in with one and register_passkey to create one.
    """
