# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AddPaymentMethodVaultItemOperationRequestParam"]


class AddPaymentMethodVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Start enrollment of a card in a connected Kernel wallet, including its first card, only when the wallet advertises add_payment_method. Returns a new payment method in pending_enrollment with a single-use action. Card details go directly to the card vault and are never accepted by this API. With enrollment hosted (the default) the action is a card_enrollment URL for the cardholder, which expires after 30 minutes. With enrollment server the action is a card_ingest URL that the card's issuer posts the card to from its backend, which expires after 5 minutes; server enrollment returns 409 when it is not configured for the organization's card backend. A failed or expired enrollment does not affect the wallet's other payment methods. Scoped API keys require vaults:write in addition to vaults:use on this vault; otherwise the operation returns 403.
    """

    type: Required[Literal["add_payment_method"]]

    enrollment: Literal["hosted", "server"]
    """hosted returns a card_enrollment link for the cardholder.

    server returns a card_ingest URL for the card's issuer to post the card to
    server to server.
    """
