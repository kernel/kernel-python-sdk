# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AddPaymentMethodVaultItemOperationRequestParam"]


class AddPaymentMethodVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Start hosted enrollment of a card in a connected Kernel wallet, including its first card, only when the wallet advertises add_payment_method. Returns a new payment method in pending_enrollment with a single-use card_enrollment URL for the cardholder. Card details go directly to the card vault and are never accepted by this API. Each call creates a separate link that expires after 30 minutes; a failed or expired enrollment does not affect the wallet's other payment methods. Scoped API keys require vaults:write in addition to vaults:use on this vault; otherwise the operation returns 403.
    """

    type: Required[Literal["add_payment_method"]]
