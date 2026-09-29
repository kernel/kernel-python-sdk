# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OnePasswordRequestAccessVaultItemOperationRequestParam"]


class OnePasswordRequestAccessVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Request access to login entries in the end-user's own, non-shared 1Password vault through the browser extension, auto-loaded into the browser. The end-user approves access in the 1Password app. Shared-vault items and passkeys are not supported. Per-entry reason and keywords overrides are only supported for a single login entry.
    """

    browser_id: Required[str]
    """Kernel browser session used to invoke the extension."""

    type: Required[Literal["1pw_create_access_request"]]

    goal: str

    keywords: SequenceNotStr[str]

    reason: str
