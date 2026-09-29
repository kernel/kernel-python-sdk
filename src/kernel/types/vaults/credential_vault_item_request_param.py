# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .credential_vault_item_spec_input_param import CredentialVaultItemSpecInputParam

__all__ = ["CredentialVaultItemRequestParam"]


class CredentialVaultItemRequestParam(TypedDict, total=False):
    """
    Ask the end-user whether to link their site credential through 1Password.
    If they choose 1Password, connect their account and request access to a login
    in their own non-shared vault; passkeys are not supported. If they decline
    or that path fails, collect a Kernel-hosted credential item instead. Never
    automatically retry an uncertain 1Password request or fill.
    Do not use credential items for credit card data. Use wallet and card item types instead.
    Kernel credentials declare fields and may enter pending_collection.
    1Password credentials either reference a connected credential_account or
    store a supplied access token and integration key encrypted on the item.
    They store no login values or selectors. Repeating the original creation
    request returns the current item without overwriting later state. A
    different request at the same key returns 409.
    """

    spec: Required[CredentialVaultItemSpecInputParam]
    """Credential fields are for login and other non-payment credentials.

    Do not store, collect, or fill credit card data in credential items. Use wallet
    and card item types for credit cards and payment checkout instead. Field order
    is preserved in the user-facing collection form, so list fields in the same
    top-to-bottom order as the website.
    """

    type: Required[Literal["credential"]]
