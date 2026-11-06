# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VgsWalletVaultItemSpecParam", "ProviderConfig"]


class ProviderConfig(TypedDict, total=False):
    """Select a VGS configuration.

    Required, because there are no Kernel-managed VGS credentials for this provider.
    """

    id: str

    name: str


class VgsWalletVaultItemSpecParam(TypedDict, total=False):
    """Cards kept in the customer's own VGS vault.

    The wallet binds a VGS provider configuration and is connected on creation; it holds no cards and has no payment methods. Each purchase is a card item that carries the card's aliases from the customer's vault. The configuration binding cannot be changed after creation.
    """

    provider: Required[Literal["vgs"]]

    provider_config: Required[ProviderConfig]
    """Select a VGS configuration.

    Required, because there are no Kernel-managed VGS credentials for this provider.
    """
