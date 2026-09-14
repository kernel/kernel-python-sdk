# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .card_vault_item_spec_param import CardVaultItemSpecParam
from .credential_vault_item_spec_update_param import CredentialVaultItemSpecUpdateParam

__all__ = ["ItemUpdateParams", "CardVaultItemUpdateRequest", "CredentialVaultItemUpdateRequest"]


class CardVaultItemUpdateRequest(TypedDict, total=False):
    id_or_name: Required[str]

    spec: Required[CardVaultItemSpecParam]
    """Live payment card. Test-mode card creation is not supported."""

    type: Literal["card"]


class CredentialVaultItemUpdateRequest(TypedDict, total=False):
    id_or_name: Required[str]

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


ItemUpdateParams: TypeAlias = Union[CardVaultItemUpdateRequest, CredentialVaultItemUpdateRequest]
