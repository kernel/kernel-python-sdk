# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordCredentialAccountState"]


class OnePasswordCredentialAccountState(BaseModel):
    provider: Literal["1password"]

    status: Literal["pending_authorization", "connected", "reconnect_required", "declined", "revoking"]
    """
    revoking means the account was deleted or disconnected and Kernel is waiting for
    1Password to confirm the revoke; it cannot be used and Kernel keeps retrying.
    """

    status_reason: Optional[str] = None
