# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthorizeVaultItemOperationRequestParam"]


class AuthorizeVaultItemOperationRequestParam(TypedDict, total=False):
    """Authorize a Link card using its existing purchase specification.

    Use only after explicit user approval and when the item advertises authorize. Do not automatically retry provider failures or indeterminate outcomes. Checkout context is not accepted.
    """

    type: Required[Literal["authorize"]]
