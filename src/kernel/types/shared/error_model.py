# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .error_detail import ErrorDetail

__all__ = ["ErrorModel"]


class ErrorModel(BaseModel):
    code: str
    """Application-specific error code (machine-readable)"""

    message: str
    """Human-readable error description for debugging"""

    details: Optional[List[ErrorDetail]] = None
    """Additional error details (for multiple errors)"""

    inner_error: Optional[ErrorDetail] = None

    unsupported_fields: Optional[List[str]] = None
    """Request fields that are incompatible with the requested browser platform."""
