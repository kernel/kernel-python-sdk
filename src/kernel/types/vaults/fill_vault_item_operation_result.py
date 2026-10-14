# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .vault_fill_field_result import VaultFillFieldResult

__all__ = ["FillVaultItemOperationResult"]


class FillVaultItemOperationResult(BaseModel):
    fields: List[VaultFillFieldResult]
    """
    One result per request binding, in request order; empty when the fill used no
    bindings. After the first failed or unknown field, all remaining fields are
    not_attempted.
    """

    status: Literal["completed", "failed", "unknown"]
    """Completed when the fill finished.

    Failed when execution stopped with known outcomes. Unknown when an outcome
    cannot be determined. Completed means values were supplied to the page, not that
    the site accepted or submitted them.
    """

    type: Literal["fill"]
