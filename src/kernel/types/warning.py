# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Warning"]


class Warning(BaseModel):
    code: str
    """
    Examples: param_unsupported, preference_unsupported, max_results_clamped,
    domains_truncated, recency_emulated, filter_emulated, date_filter_overridden,
    provider_ineligible, fallback_failed, content_partial.
    """

    message: str

    param: Optional[str] = None

    provider: Optional[str] = None

    result_id: Optional[str] = None
