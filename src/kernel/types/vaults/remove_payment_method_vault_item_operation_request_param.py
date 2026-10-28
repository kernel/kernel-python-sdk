# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RemovePaymentMethodVaultItemOperationRequestParam"]


class RemovePaymentMethodVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Remove one payment method from a Kernel wallet, only when the wallet advertises remove_payment_method. Removal deletes the stored card and blocks new purchases, fills and confirmations funded by it without affecting the wallet's other payment methods; the wallet stays connected even with no payment methods left. A purchase funded by the method with an unresolved outcome blocks removal with 409 purchase_unresolved. If the provider outcome is uncertain the method stays in removal_pending and keeps refusing payments; retry the removal later. Removal is not proof that a payment did not occur. Scoped API keys require vaults:write in addition to vaults:use on this vault; otherwise the operation returns 403.
    """

    payment_method_id: Required[str]
    """ID from the wallet's payment_methods expansion."""

    type: Required[Literal["remove_payment_method"]]
