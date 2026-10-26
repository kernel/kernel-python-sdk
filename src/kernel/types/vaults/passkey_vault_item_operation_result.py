# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PasskeyVaultItemOperationResult"]


class PasskeyVaultItemOperationResult(BaseModel):
    status: Literal["armed", "disarmed"]
    """
    armed means the browser will answer matching passkey requests; it does not mean
    a page has asked yet. disarmed means the browser no longer uses this item's
    passkeys.
    """

    type: Literal["arm_passkey", "register_passkey", "disarm_passkey"]

    rp_id: Optional[str] = None
    """Relying party the armed passkey answers for. Returned by arm_passkey."""
