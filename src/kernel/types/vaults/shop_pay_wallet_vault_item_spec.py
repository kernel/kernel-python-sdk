# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ShopPayWalletVaultItemSpec", "Authorization", "AuthorizationClient"]


class AuthorizationClient(BaseModel):
    type: Literal["kernel_managed"]


class Authorization(BaseModel):
    client: AuthorizationClient

    method: Literal["oauth"]


class ShopPayWalletVaultItemSpec(BaseModel):
    """Shop Pay wallet connected through Kernel's Shop app.

    Creation returns a shop_pay_oauth action: the shopper signs in to Shop and approves the connection, and the wallet connects. The connected wallet's payment_methods expansion lists the shopper's saved Shop Pay cards.
    """

    authorization: Authorization

    provider: Literal["shop_pay"]
