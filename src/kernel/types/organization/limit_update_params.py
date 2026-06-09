# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LimitUpdateParams"]


class LimitUpdateParams(TypedDict, total=False):
    default_project_max_concurrent_sessions: Optional[int]
    """
    Default maximum concurrent browser sessions for projects without an explicit
    override. Set to 0 to remove the default; omit to leave unchanged. Cannot exceed
    the organization's concurrent session ceiling.
    """
