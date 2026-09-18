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
    Text, email, and password have form inputs; totp does not and is omitted from
    both Kernel-hosted and customer React forms. Password and totp must be
    sensitive. A totp value is an RFC 4648 Base32 generator seed (case-insensitive,
    optional trailing padding), not an otpauth URI or current code. Reject invalid
    or empty decoded seeds. Browser fill generates an RFC 6238 code at execution
    time using HMAC-SHA1, 6 digits, and a 30-second period. Preserve leading zeros;
    never fill the seed. Custom algorithms, digits, periods, and form enrollment are
    unsupported.
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
    and TOTP seeds. Password and totp fields must be true. Omission defaults to true
    for safety; do not rely on that default for every field. False permits API reads
    and form prefilling.
    """

    value: str
    """
    Optional initial value satisfying the declared type, at most 16 KiB in UTF-8
    bytes. Omit to leave unset; null and empty strings are rejected on creation.
    Sensitive values are encrypted and never copied into the returned spec.
    """
