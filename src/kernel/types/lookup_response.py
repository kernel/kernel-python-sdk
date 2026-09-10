# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .target import Target
from .._models import BaseModel
from .recommendation import Recommendation

__all__ = ["LookupResponse"]


class LookupResponse(BaseModel):
    recommendation: Optional[Recommendation] = None

    target: Target
