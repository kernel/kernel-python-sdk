# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.error_model import ErrorModel

__all__ = ["Analysis"]


class Analysis(BaseModel):
    id: str
    """Discovery run ID used to poll analysis status."""

    created_at: datetime
    """Time the analysis was created."""

    expires_at: datetime
    """Deadline after which a still-running analysis becomes expired."""

    failure: Optional[ErrorModel] = None
    """Present for failed, canceled, or expired analyses.

    Messages contain safe retry guidance rather than internal workflow errors.
    """

    finished_at: Optional[datetime] = None
    """Time the analysis reached a terminal status. Null while it is running."""

    status: Literal["running", "completed", "failed", "canceled", "expired"]
    """Lifecycle status of a background analysis."""
