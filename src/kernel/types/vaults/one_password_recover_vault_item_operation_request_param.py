# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OnePasswordRecoverVaultItemOperationRequestParam"]


class OnePasswordRecoverVaultItemOperationRequestParam(TypedDict, total=False):
    """Kernel encountered a recoverable error while linking this 1Password account.

    Use this action to get a new link to recover the connection. After recovery completes, start a new authorization on the same item.
    """

    type: Required[Literal["1pw_recover"]]
