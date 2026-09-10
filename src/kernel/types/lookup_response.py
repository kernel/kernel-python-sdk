# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .target import Target
from .._models import BaseModel
from .recommendation import Recommendation

__all__ = ["LookupResponse"]


class LookupResponse(BaseModel):
    recommendation: Optional[Recommendation] = None

    target: Target

    guidance: Optional[str] = None
    """Short advisory markdown to facilitate navigating this target.

    Returned even when no configuration reached the target, since knowing what
    prevented success is useful without a configuration. Not verified against this
    target. Null when nothing applicable was observed or no notes exist.
    """
