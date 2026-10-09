# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CredentialVaultFieldUpdateParam"]


class CredentialVaultFieldUpdateParam(TypedDict, total=False):
    """Set exactly one of value or encrypted_value.

    Use value unless the update comes from your own credential collection web app that encrypts values in the browser; see encrypted_value.
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

    value: Optional[str]
    """
    Replacement value (at most 16 KiB in UTF-8 bytes), or null or an empty string to
    immediately clear the stored value. Clearing a required form-supported field
    reopens collection; clearing an optional field does not prevent readiness.
    Values must satisfy the declared field type. For totp, value is the generator
    seed, never a current code. Clearing a required totp field returns 400 because
    it cannot be collected in a form.
    """
