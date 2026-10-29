# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShopPayWalletVaultItemSpecParam", "Authorization", "AuthorizationClient"]


class AuthorizationClient(TypedDict, total=False):
    type: Required[Literal["kernel_managed"]]


class Authorization(TypedDict, total=False):
    client: Required[AuthorizationClient]

    method: Required[Literal["oauth"]]


class ShopPayWalletVaultItemSpecParam(TypedDict, total=False):
    """Shop Pay wallet connected through Kernel's Shop app.

    Creation returns a shop_pay_oauth action: the shopper signs in to Shop and approves the connection, and the wallet connects. The connected wallet's payment_methods expansion lists the shopper's saved Shop Pay cards.
    """

    authorization: Required[Authorization]

    provider: Required[Literal["shop_pay"]]
