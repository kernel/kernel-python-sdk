# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .recommendation import Recommendation

__all__ = ["RecommendationSummary"]


class RecommendationSummary(BaseModel):
    analysis_id: str
    """ID of the most recently requested analysis for this exact target."""

    analysis_status: Literal["running", "completed", "failed", "canceled", "expired"]
    """Lifecycle status of the most recently requested analysis for this exact target."""

    last_requested_at: datetime
    """
    Most recent time the selected project requested an analysis for this exact
    target.
    """

    recommendation: Optional[Recommendation] = None
    """Recommendation produced by the latest analysis.

    Null when that analysis did not produce one.
    """

    recommended_config_label: Optional[str] = None
    """Display label for the recommended browser configuration."""

    success_rate: Optional[float] = None
    """Success rate for the recommended configuration.

    Null when the latest analysis did not produce one.
    """

    target: str
    """
    Normalized exact target previously analyzed by the selected project, including
    scheme, host, port, and path.
    """
