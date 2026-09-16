# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .proxy import Proxy
from .browser import Browser
from .._models import BaseModel
from .evidence import Evidence

__all__ = ["Recommendation"]


class Recommendation(BaseModel):
    browser: Browser
    """Browser settings that can be passed directly to `POST /browsers`."""

    evidence: Evidence

    match_scope: Literal["exact", "host", "domain"]
    """Specificity of knowledge matched for this recommendation.

    Exact matches use knowledge for the requested target; host and domain matches
    use broader fallback knowledge.
    """

    matched_target: str
    """Target value that supplied the recommendation."""

    proxy: Proxy
    """Proxy recipe for the recommended browser."""

    type: Literal["recommendation"]
