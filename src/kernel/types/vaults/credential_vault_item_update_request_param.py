# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .credential_vault_item_spec_update_param import CredentialVaultItemSpecUpdateParam

__all__ = ["CredentialVaultItemUpdateRequestParam"]


class CredentialVaultItemUpdateRequestParam(TypedDict, total=False):
    """Atomically update description and selected values.

    Omitted properties are
    preserved. Field names, types, required flags, and sensitivity cannot change.
    Unknown field names return 400; stale versions or mismatched item types
    return 409 without changing the item. A successful update increments version
    and invalidates outstanding Kernel-hosted collection sessions. If required
    values remain missing, return pending_collection and a fresh collection
    action. Otherwise return ready without an action; collect can open the form
    again without clearing values. Customer URLs have no Kernel-managed expiry.
    """

    spec: Required[CredentialVaultItemSpecUpdateParam]

    type: Required[Literal["credential"]]

    version: Required[int]
    """Expected current item version from the latest read."""

    expected_item_id: str
    """Optional immutable item ID precondition.

    Returns 409 if the key now identifies a different item. Accepted writes target
    this immutable ID, preventing replacement-key races. Supply this when submitting
    a form bound to a previously read item.
    """
