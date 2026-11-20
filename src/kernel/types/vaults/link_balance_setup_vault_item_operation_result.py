# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LinkBalanceSetupVaultItemOperationResult"]


class LinkBalanceSetupVaultItemOperationResult(BaseModel):
    """Share url with the user; only the user can complete the page.

    It does not expire and is the same for first-time setup, adding money and changing the threshold. Observe the result through the payment_methods expansion (a method with type balance and its balance.available) rather than assuming the user finished.
    """

    type: Literal["link_balance_setup"]

    url: str
