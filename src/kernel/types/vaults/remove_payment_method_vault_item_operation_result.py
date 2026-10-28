# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RemovePaymentMethodVaultItemOperationResult"]


class RemovePaymentMethodVaultItemOperationResult(BaseModel):
    payment_method_id: str

    status: Literal["removed"]

    type: Literal["remove_payment_method"]
