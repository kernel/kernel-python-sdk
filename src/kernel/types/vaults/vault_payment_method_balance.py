# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .vault_payment_method_amount import VaultPaymentMethodAmount

__all__ = ["VaultPaymentMethodBalance"]


class VaultPaymentMethodBalance(BaseModel):
    """Present on stored-value payment methods, such as a Link balance (type `balance`).

    `available` is the amount available to spend, absent when the provider did not report it. Read live from the provider on every request and never stored by Kernel.
    """

    available: Optional[VaultPaymentMethodAmount] = None
