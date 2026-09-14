# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectVaultItemOperationRequestParam"]


class CollectVaultItemOperationRequestParam(TypedDict, total=False):
    """Return the credential item with its collection action.

    Supported for ready
    and pending_collection credential items. Always render the same form from
    every form-supported field; totp fields have no form input and are omitted.
    No caller-selected field subsets or form overrides are accepted.
    Reuse an active Kernel-hosted session or renew an expired session atomically.
    Customer-hosted forms use their own backend and ordinary item GET/PATCH. Opening
    the form does not clear values or change readiness or item version.
    To observe edits on a ready item, record its version and poll GET without
    wait until the version changes, then reconcile the returned state. Version
    changes may also come from PATCH; they do not identify a particular form
    submission. Customer-hosted apps use their own submission callback, including
    for unchanged forms. The wait parameter waits for readiness, not edits.
    """

    type: Required[Literal["collect"]]
