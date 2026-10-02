# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelWalletVaultItemSpec"]


class KernelWalletVaultItemSpec(BaseModel):
    """
    One card Kernel enrolls for Visa or Mastercard agentic network tokens using Kernel-managed credentials. Creation returns a card_enrollment action: the cardholder enters the card and their email on a Kernel-hosted page, then Kernel enrolls the securely stored card. The card number never reaches Kernel. The connected wallet's payment_methods expansion lists the enrolled card. Visa cards can be enrolled, but Visa purchases are not yet supported: authorize returns 400.
    """

    provider: Literal["kernel"]
