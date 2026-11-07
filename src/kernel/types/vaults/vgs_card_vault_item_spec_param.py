# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .vgs_card_input_param import VgsCardInputParam

__all__ = ["VgsCardVaultItemSpecParam"]


class VgsCardVaultItemSpecParam(TypedDict, total=False):
    """One live purchase with a card in the customer's VGS vault.

    With card_mode full, authorize reveals card.pan_alias and card.cvc_alias through Kernel's VGS outbound proxy; with card_mode cvc_only, for a card the merchant already holds on file whose checkout page asks only for the security code, it reveals card.cvc_alias alone. The proxy replaces each revealed value with an alias in Kernel's vault before it reaches Kernel; Kernel never receives the card number or security code. The card is then ready with no further approval, until expires_at, by default five minutes after authorize. fill types Kernel's aliases on merchant_url's origin, and Kernel's VGS proxy replaces them with the card's details when the browser submits checkout; a cvc_only card fills only the cvc field, and reports no masks because it has no last4 to verify. A cvc_only card's payment window routes all of the browser's egress through Kernel's VGS outbound proxy, exactly as widely as a full card's: while it is open the proxy reveals the card's aliases to any destination the browser sends them to, not only the security code. An expired card requires a new purchase with a freshly collected CVC alias. The amount and merchant are recorded but do not restrict payment requests sent by the browser. Card updates are not supported; delete and create a new item instead.
    """

    amount: Required[int]
    """Integer amount in minor currency units (at most 1000000)."""

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

    card: VgsCardInputParam
    """Required when creating the card. Never returned."""

    card_mode: Literal["full", "cvc_only"]
    """Which card this purchase supplies, and the only part of it a read returns.

    full is a whole card from the customer's vault. cvc_only is a card the merchant
    already holds on file, whose checkout page asks for nothing but the security
    code. It must match spec.card: a full card that is missing pan_alias is rejected
    rather than treated as cvc_only. Omit it for full, which a read also omits.
    """
