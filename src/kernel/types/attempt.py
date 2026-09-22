# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Attempt"]


class Attempt(BaseModel):
    duration_ms: int

    outcome: Literal["success", "empty", "error", "timeout"]

    provider: str

    error_code: Optional[str] = None

    retryable: Optional[bool] = None
