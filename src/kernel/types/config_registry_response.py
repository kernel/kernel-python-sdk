# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .target import Target
from .._models import BaseModel
from .analysis import Analysis
from .recommendation_result import RecommendationResult

__all__ = ["ConfigRegistryResponse"]


class ConfigRegistryResponse(BaseModel):
    analysis: Optional[Analysis] = None
    """Pollable analysis after workflow submission is acknowledged.

    Null when no refresh was submitted.
    """

    recommendation: Optional[RecommendationResult] = None
    """A recommendation or a structured no-recommendation result."""

    target: Target
