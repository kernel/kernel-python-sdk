# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordCredentialAccountState"]


class OnePasswordCredentialAccountState(BaseModel):
    provider: Literal["1password"]

    status: Literal["pending_authorization", "connected", "reconnect_required", "declined"]

    status_reason: Optional[str] = None
