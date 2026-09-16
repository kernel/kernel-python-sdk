# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Evidence"]


class Evidence(BaseModel):
    accessed: int

    blocked: int

    inconclusive: int

    last_observed_at: datetime
    """Most recent contributing observation.

    Recommendations remain eligible regardless of age and can be returned while a
    new analysis refreshes them.
    """

    run_count: int

    sample_size: int
    """Number of judged trials."""

    success_rate: float
    """Accessed trials divided by judged trials. Inconclusive trials are excluded."""

    last_supported_at: Optional[datetime] = None
    """
    Most recent contributing run whose evidence supported recommending this
    configuration. Omitted when no individual run independently met the
    recommendation threshold.
    """
