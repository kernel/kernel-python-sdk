# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ManagedAuthCredentialVaultItemSpec"]


class ManagedAuthCredentialVaultItemSpec(BaseModel):
    connection_id: str
    """ID of the managed auth connection whose saved credential this item reads.

    List connections with `GET /auth/connections`.
    """

    provider: Literal["managed_auth"]

    description: Optional[str] = None
    """Display text supplied when the item was created. Omitted when none was given."""
