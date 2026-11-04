# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .vgs_card_input_param import VgsCardInputParam

__all__ = ["VgsCardVaultItemSpecParam"]


class VgsCardVaultItemSpecParam(TypedDict, total=False):
    """One live purchase with a card in the customer's VGS vault.

    authorize reveals card.pan_alias and card.cvc_alias through Kernel's VGS outbound proxy, which replaces both with aliases in Kernel's vault before they reach Kernel; Kernel never receives the card number or security code. The card is then ready with no further approval, until expires_at, by default five minutes after authorize. fill types Kernel's aliases on merchant_url's origin, and Kernel's VGS proxy replaces them with the card's details when the browser submits checkout. An expired card requires a new purchase with a freshly collected CVC alias. The amount and merchant are recorded but do not restrict payment requests sent by the browser. Card updates are not supported; delete and create a new item instead.
    """

    amount: Required[int]
    """Integer amount in minor currency units (at most 1000000)."""

    card: Required[VgsCardInputParam]
    """The card's aliases in the customer's VGS vault, its expiry and last four digits.

    Write-only: stored encrypted and never returned in the item, its events or logs.
    A repeated PUT with the same key must send the same card.
    """

    currency: Required[str]
    """ISO 4217 code.

    Supported: aud, brl, cad, chf, czk, dkk, eur, gbp, hkd, inr, jpy, krw, mxn, nok,
    nzd, pln, sek, sgd, usd, zar.
    """

    merchant_name: Required[str]

    merchant_url: Required[str]
    """Merchant checkout URL. Fill is allowed only on this URL's origin."""

    provider: Required[Literal["vgs"]]

    wallet: Required[str]
    """Key of the VGS wallet item whose configuration reads the aliases."""
