# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VaultFillFieldResult"]


class VaultFillFieldResult(BaseModel):
    index: int
    """Zero-based index into the request fields array."""

    status: Literal["filled", "failed", "not_attempted", "unknown"]
    """
    Filled means the fill action completed, not that the website retained or
    accepted the value.
    """

    error_code: Optional[
        Literal[
            "target_changed",
            "element_not_found",
            "ambiguous_selector",
            "element_not_editable",
            "option_not_found",
            "timeout",
            "execution_failed",
        ]
    ] = None
    """Present only for failed or unknown fields.

    Never includes secret values, DOM content, or raw browser errors.
    """
