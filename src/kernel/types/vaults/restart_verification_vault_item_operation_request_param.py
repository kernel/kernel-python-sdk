# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RestartVerificationVaultItemOperationRequestParam"]


class RestartVerificationVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Explicitly prepare a fresh local verification session for the same Kernel Visa purchase and connected wallet, only when restart_verification is advertised. Kernel must have durable proof of an initial attestation failure before intent dispatch. Replaces the spend_approval capability and discards session-bound verification data without calling the provider or granting spend consent. The cardholder must use the new link, verify again and explicitly approve the purchase. Unknown intent creation, legacy unclassified recovery, enrollment completion, issuance and confirmation cannot restart. Do not automatically retry this operation.
    """

    type: Required[Literal["restart_verification"]]
