# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .vault_fill_field_result import VaultFillFieldResult

__all__ = ["FillVaultItemOperationResult"]


class FillVaultItemOperationResult(BaseModel):
    fields: List[VaultFillFieldResult]
    """Exactly one result per request binding, in request order.

    After the first failed or unknown field, all remaining fields are not_attempted.
    """

    status: Literal["completed", "failed", "unknown"]
    """Completed only when all fields were filled.

    Failed when execution stopped with known outcomes. Unknown when any field's
    outcome cannot be determined. None of these statuses confirms payment or
    merchant acceptance.
    """

    type: Literal["fill"]
