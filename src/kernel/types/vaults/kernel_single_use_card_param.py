# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .single_use_card_billing_address_param import SingleUseCardBillingAddressParam

__all__ = ["KernelSingleUseCardParam"]


class KernelSingleUseCardParam(TypedDict, total=False):
    """
    Details of a card the caller supplies, such as a single-use virtual card from its issuer. Mutually exclusive with payment_method_id. The card details are stored encrypted for fill and never returned; reads return only reference. Kernel deletes them shortly after the card's expires_at; deleting the card, its wallet or its vault deletes them immediately. A card whose expiry month has ended is rejected.
    """

    cvc: Required[str]

    exp_month: Required[str]

    exp_year: Required[str]

    number: Required[str]
    """Card number; must pass the Luhn check."""

    billing_address: SingleUseCardBillingAddressParam
    """Billing address filled with the billing\\__\\** fill fields. Never returned."""

    name: str
    """Cardholder name, filled as billing_name."""

    reference: str
    """The caller's identifier for the card, such as the issuer's card ID.

    Returned unchanged on reads.
    """
