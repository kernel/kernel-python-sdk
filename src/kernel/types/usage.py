# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Usage"]


class Usage(BaseModel):
    content_fetches: int
    """
    Number of result URLs for which a Kernel browser retrieval was attempted,
    excluding cache-only hits.
    """

    results_count: int
    """
    Number of result entries returned, including failed entries on the contents
    endpoint.
    """

    cost: Optional[float] = None
    """Total customer charge in USD when billing data is available."""
