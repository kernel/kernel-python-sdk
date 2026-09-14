# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .credential_vault_item_spec import CredentialVaultItemSpec
from .credential_vault_item_state import CredentialVaultItemState
from .credential_collection_action import CredentialCollectionAction

__all__ = ["CredentialVaultItem", "AvailableExpansion", "AvailableOperation"]


class AvailableExpansion(BaseModel):
    """
    Live data that can currently be requested by passing its type to the item GET expand parameter.
    """

    description: str

    type: Literal["payment_methods"]


class AvailableOperation(BaseModel):
    """An operation that is currently valid for this item.

    Read the description before invoking it through the item operations endpoint.
    """

    description: str

    type: Literal["authorize", "collect", "prepare_checkout", "fill"]


class CredentialVaultItem(BaseModel):
    id: str

    available_expansions: List[AvailableExpansion]

    available_operations: List[AvailableOperation]
    """Advertises collect for ready and pending_collection items.

    Browser fill is advertised only when separately implemented and eligible.
    """

    created_at: datetime

    key: str
    """Immutable item key assigned when the item is created."""

    spec: CredentialVaultItemSpec

    state: CredentialVaultItemState

    type: Literal["credential"]

    updated_at: datetime

    version: int
    """
    Starts at 1 and increments on PATCH and successful hosted submission, but not
    collection-link renewal.
    """

    action: Optional[CredentialCollectionAction] = None
    """
    One schema-derived form for the item, available in ready or pending_collection
    state. Render every form-supported field as editable; omit totp fields and
    preserve their stored seeds. Prefill non-sensitive values, and allow existing
    sensitive values to be preserved or replaced without ever revealing them. No
    field subsets or per-request form configuration exist. Validate required fields
    against the resulting values, including preserved secrets. Submit changed values
    only, using the version used to render the form. Scoped hosted submission
    rejects totp edits; seed writes require the ordinary authenticated item API.
    Customer forms likewise omit totp from their payloads. Save edits atomically. A
    successful hosted submission increments the version, marks ready, and consumes
    the session; an empty edit may complete collection while preserving values. A
    customer form uses PATCH for changed values and does not send an empty PATCH
    when nothing changed. Kernel-hosted bearer sessions require no Kernel account
    and are bound to the item version. Expired, superseded, consumed, or
    deleted-item sessions cannot submit. Authenticated item GET renews expired
    active sessions for ready or pending items; pending items always receive an
    action. A ready item with no active session omits the action until collect is
    invoked. Concurrent renewals return the same link. Renewal changes neither
    values nor item version. An expired link cannot renew itself. The hosted form
    handles its collection protocol; callers only open the returned URL and do not
    extract or submit its token through the public API. For customer-hosted forms,
    use @onkernel/vault-react and an authenticated customer backend calling the
    ordinary item GET/PATCH API. Kernel does not store customer collection URLs or
    authenticate the customer's end users. Treat URLs and submitted values as
    secrets and exclude them from logs, traces, and errors.
    """
