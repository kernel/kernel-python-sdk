# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["KernelWalletVaultItemSpecParam"]


class KernelWalletVaultItemSpecParam(TypedDict, total=False):
    """
    Cards stored with Kernel-managed credentials, each a payment method of the wallet. Each card is enrolled through a card_enrollment action: the cardholder enters the card and their email on a Kernel-hosted page. Where the wallet advertises add_payment_method, creation returns an empty connected wallet and each card is enrolled with that operation. Otherwise creation returns the wallet's default card's card_enrollment action, and the wallet connects once that card is stored. Kernel then enrolls each card for an agentic network token when the issuer supports it. The card number never reaches Kernel. The connected wallet's payment_methods expansion lists the cards; capabilities.single_use_card.eligible is false, with a network_token_* reason, until the card has a network token, and authorize returns 400 for such a card unless Kernel supports checkout delivery without a network token for that card. In that case, fill types the checkout details. Visa purchases require the cardholder to complete a spend_approval action before Kernel issues a one-time code; Mastercard purchases need no hosted approval.
    """

    provider: Required[Literal["kernel"]]
