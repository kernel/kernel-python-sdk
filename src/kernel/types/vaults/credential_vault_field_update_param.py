# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CredentialVaultFieldUpdateParam"]


class CredentialVaultFieldUpdateParam(TypedDict, total=False):
    value: Required[Optional[str]]
    """
    Replacement value (at most 16 KiB in UTF-8 bytes), or null or an empty string to
    immediately clear the stored value. Clearing a required form-supported field
    reopens collection; clearing an optional field does not prevent readiness.
    Values must satisfy the declared field type. For totp, value is the generator
    seed, never a current code. Clearing a required totp field returns 400 because
    it cannot be collected in a form.
    """
