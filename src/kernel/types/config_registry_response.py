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

    guidance: Optional[str] = None
    """Short advisory markdown to facilitate navigating this target.

    Returned even when no configuration reached the target, since knowing what
    prevented success is useful without a configuration. Not verified against this
    target. Null when nothing applicable was observed or no notes exist.
    """
