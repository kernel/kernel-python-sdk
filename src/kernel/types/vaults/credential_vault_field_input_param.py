# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .credential_vault_field_type import CredentialVaultFieldType

__all__ = ["CredentialVaultFieldInputParam"]


class CredentialVaultFieldInputParam(TypedDict, total=False):
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
    pages; use arm_passkey to sign in with one and register_passkey to create one.
    """

    encrypted_value: str
    """Alternative to value for custom credential collection web apps.

    Use this only if you run your own credential collection web app and want values
    encrypted in the browser, sent to your backend still encrypted, and forwarded to
    Kernel's API still encrypted. In every other case, including server-side code
    that already holds the plaintext, use value. The field's value encrypted
    client-side as a compact JWE with alg ECDH-ES and enc A256GCM to the key from
    GET /vaults/{id_or_name}/encryption_key, with that key's kid in the protected
    header. Compression is not supported. The decrypted value follows the same rules
    as value, including that an empty string clears the field on update. A kid that
    is not this vault's key returns 400 encryption_key_mismatch; fetch the key again
    and re-encrypt. Other malformed or undecryptable values return 400
    invalid_request. The whole request body is limited to 128 KiB.
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

    value: str
    """
    Optional initial value satisfying the declared type, at most 16 KiB in UTF-8
    bytes. Omit to leave unset; null and empty strings are rejected on creation.
    Sensitive values are encrypted and never copied into the returned spec. Use this
    unless your own credential collection web app encrypts values in the browser;
    mutually exclusive with encrypted_value.
    """
