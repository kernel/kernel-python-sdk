# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .vault_payment_method import VaultPaymentMethod

__all__ = ["AddPaymentMethodVaultItemOperationResult"]


class AddPaymentMethodVaultItemOperationResult(BaseModel):
    """The payment method created in pending_enrollment.

    Deliver action.url to the cardholder; it is a single-use capability and must not be logged. Observe completion through the wallet's payment_methods expansion.
    """

    payment_method: VaultPaymentMethod

    type: Literal["add_payment_method"]
