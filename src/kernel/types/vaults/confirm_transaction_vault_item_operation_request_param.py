# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfirmTransactionVaultItemOperationRequestParam"]


class ConfirmTransactionVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Report a real merchant transaction outcome for an issued Kernel Visa or Shop Pay credential. Shop Pay accepts PURCHASE, AUTHORIZATION and CAPTURE. Never infer success from filling checkout or receiving a credential. Supply the observed status, transaction type, actual amount, currency and timestamp. Unknown outcomes require manual reconciliation, not retry. Each purchase accepts one report.
    """

    amount: Required[int]
    """Actual transaction amount in minor units, no greater than the approved limit."""

    currency: Required[str]
    """Must match the approved purchase currency."""

    occurred_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Time the merchant outcome was observed."""

    status: Required[Literal["APPROVED", "DECLINED", "PENDING", "ERROR", "CANCELLED"]]

    transaction_type: Required[
        Literal["PURCHASE", "AUTHORIZATION", "CAPTURE", "REFUND", "REVERSAL", "VERIFICATION", "CHARGEBACK", "FRAUD"]
    ]

    type: Required[Literal["confirm_transaction"]]

    failure_code: str
    """
    Why the purchase did not succeed, for any other outcome, such as 3ds_challenge,
    captcha, login_required, timeout or site_error. payment_declined goes only with
    DECLINED, which takes no other code. Shop Pay reports it; other providers ignore
    it.
    """

    order_id: str
    """The merchant's order number, for an APPROVED outcome.

    Shop Pay reports it; other providers ignore it.
    """

    order_url: str
    """The merchant's https order page, for an APPROVED outcome.

    Shop Pay reports it; other providers ignore it.
    """
