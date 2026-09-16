# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NoRecommendation"]


class NoRecommendation(BaseModel):
    code: Literal["proxy_restricted", "target_not_evaluable", "no_working_configuration", "inconclusive"]
    """
    Machine-readable reason Kernel cannot currently provide a config recommendation.
    """

    message: str
    """Human-readable explanation suitable for display."""

    type: Literal["no_recommendation"]
