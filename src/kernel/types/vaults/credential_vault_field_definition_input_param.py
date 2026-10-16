# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .credential_vault_field_type import CredentialVaultFieldType

__all__ = ["CredentialVaultFieldDefinitionInputParam"]


class CredentialVaultFieldDefinitionInputParam(TypedDict, total=False):
    """A field definition without a value.

    Field updates add fields with this shape and set their values in `fields`.
    """

    name: Required[str]
    """Unique stable field name used to key values, updates, and browser fills."""

    type: Required[CredentialVaultFieldType]
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
    pages.
    """

    label: str
    """Optional human-readable display label.

    It is returned as non-secret metadata and never affects value keys, updates, or
    browser fills. Use single-line, trimmed display text without control or
    formatting characters. The server enforces a 128-byte UTF-8 limit.
    """

    required: bool

    sensitive: bool
    """
    Set false explicitly for ordinary usernames, email addresses, and other
    non-secret identifiers. Reserve true for secrets such as passwords, API tokens,
    and TOTP seeds. Password, totp, and passkey fields must be true. Omission
    defaults to true for safety; do not rely on that default for every field. False
    permits API reads and form prefilling.
    """
