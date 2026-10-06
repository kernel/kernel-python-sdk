# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelWalletVaultItemSpec"]


class KernelWalletVaultItemSpec(BaseModel):
    """One card stored with Kernel-managed credentials.

    Creation returns a card_enrollment action: the cardholder enters the card and their email on a Kernel-hosted page, and the wallet connects once the card is stored. Kernel then enrolls it for an agentic network token when the issuer supports it. The card number never reaches Kernel. The connected wallet's payment_methods expansion lists the card; capabilities.single_use_card.eligible is false, with a network_token_* reason, until the card has a network token, and authorize returns 400 for such a card. Visa purchases require the cardholder to complete a spend_approval action before Kernel issues a one-time code; Mastercard purchases need no hosted approval.
    """

    provider: Literal["kernel"]
