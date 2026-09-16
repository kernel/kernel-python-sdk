# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .vault_checkout_context_param import VaultCheckoutContextParam

__all__ = ["PrepareCheckoutVaultItemOperationRequestParam"]


class PrepareCheckoutVaultItemOperationRequestParam(TypedDict, total=False):
    """Prepare an unused AgentCard card for a supported tokenization checkout.

    Deliver the returned approval URL and keep the approval page open. Poll the item until ready_to_submit, then submit native Pay before preparation.expires_at. Readiness lasts at most 30 seconds. Unused preparations expire automatically. Preparations are single-use even after failure or expiry; do not automatically retry and reconcile uncertain outcomes with the merchant.
    """

    checkout: Required[VaultCheckoutContextParam]
    """
    Required when preparing an unused AgentCard card for a supported tokenization
    processor. Consent is bound to this browser and declared merchant origin, not a
    tab. Wait for the item's ready_to_submit status before native Pay and submit
    within its readiness deadline. Unused preparations expire automatically; every
    preparation is single-use, including after failure or expiry.
    """

    type: Required[Literal["prepare_checkout"]]
