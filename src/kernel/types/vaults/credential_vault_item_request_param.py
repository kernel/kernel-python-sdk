# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .credential_vault_item_spec_input_param import CredentialVaultItemSpecInputParam

__all__ = ["CredentialVaultItemRequestParam"]


class CredentialVaultItemRequestParam(TypedDict, total=False):
    """
    Create a credential item without a wallet or external provider.
    Do not use credential items to store, collect, or fill credit card data,
    including card numbers (PANs), security codes (CVV/CVC), or expiration dates.
    Use wallet and card item types for credit cards and payment checkout instead.
    If all required fields have values, return ready without a collection action;
    collect can still open its form. Otherwise return pending_collection with
    a time-scoped Kernel-hosted collection action. Missing
    optional fields alone do not trigger collection. Repeating the original
    creation request returns the current item without overwriting later edits;
    a different request at the same key returns 409. Use PATCH for updates.
    Required totp fields must include a valid seed on creation; otherwise return
    400 rather than opening a form that cannot collect it. Optional totp fields
    may be unset and populated later through PATCH.
    """

    spec: Required[CredentialVaultItemSpecInputParam]
    """Credential fields are for login and other non-payment credentials.

    Do not store, collect, or fill credit card data in credential items. Use wallet
    and card item types for credit cards and payment checkout instead.
    """

    type: Required[Literal["credential"]]
