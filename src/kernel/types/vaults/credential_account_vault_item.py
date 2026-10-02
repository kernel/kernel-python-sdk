# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .one_password_oauth_action import OnePasswordOAuthAction
from .one_password_credential_account_spec import OnePasswordCredentialAccountSpec
from .one_password_credential_account_state import OnePasswordCredentialAccountState

__all__ = ["CredentialAccountVaultItem", "AvailableExpansion", "AvailableOperation"]


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

    type: Literal[
        "authorize",
        "collect",
        "prepare_checkout",
        "fill",
        "1pw_create_access_request",
        "1pw_access_request_status",
        "1pw_fill",
        "1pw_recover",
        "1pw_update_access_token",
        "webmcp_invoke",
    ]


class CredentialAccountVaultItem(BaseModel):
    id: str

    available_expansions: List[AvailableExpansion]

    available_operations: List[AvailableOperation]
    """Advertises 1pw_recover when Kernel can recover a failed account link.

    Recovery is unavailable while authorization is pending or after the connection
    has already been reset.
    """

    created_at: datetime

    key: str
    """Immutable item key assigned when the item is created."""

    spec: OnePasswordCredentialAccountSpec

    state: OnePasswordCredentialAccountState

    type: Literal["credential_account"]

    updated_at: datetime

    action: Optional[OnePasswordOAuthAction] = None

    expires_at: Optional[datetime] = None
