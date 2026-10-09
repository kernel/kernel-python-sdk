# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VaultEncryptionKey", "Jwk"]


class Jwk(BaseModel):
    """P-256 public key in JWK form."""

    crv: Literal["P-256"]

    kty: Literal["EC"]

    x: str
    """Base64url-encoded x coordinate."""

    y: str
    """Base64url-encoded y coordinate."""


class VaultEncryptionKey(BaseModel):
    """Public key for encrypted_value on credential fields.

    Use this only if you run your own credential collection web app and want values encrypted in the browser, sent to your backend still encrypted, and forwarded to Kernel's API still encrypted. In every other case, including server-side code that already holds the plaintext, use value. Each vault has its own key; a value encrypted for one vault is rejected by every other vault. The key is created on first request and stays the same for the vault's lifetime, so it may be cached.
    """

    alg: Literal["ECDH-ES"]
    """JWE key management algorithm."""

    enc: Literal["A256GCM"]
    """JWE content encryption algorithm."""

    jwk: Jwk
    """P-256 public key in JWK form."""

    kid: str
    """Key ID. Set it as the kid protected header of every encrypted_value."""
