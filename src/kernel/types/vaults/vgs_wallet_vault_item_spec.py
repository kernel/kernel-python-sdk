# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VgsWalletVaultItemSpec", "ProviderConfig"]


class ProviderConfig(BaseModel):
    """Select a VGS configuration.

    Required, because there are no Kernel-managed VGS credentials for this provider.
    """

    id: Optional[str] = None

    name: Optional[str] = None


class VgsWalletVaultItemSpec(BaseModel):
    """Cards kept in the customer's own VGS vault.

    The wallet binds a VGS provider configuration and is connected on creation; it holds no cards and has no payment methods. Each purchase is a card item that carries the card's aliases from the customer's vault. The configuration binding cannot be changed after creation.
    """

    provider: Literal["vgs"]

    provider_config: ProviderConfig
    """Select a VGS configuration.

    Required, because there are no Kernel-managed VGS credentials for this provider.
    """
