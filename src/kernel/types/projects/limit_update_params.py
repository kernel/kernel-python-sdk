# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LimitUpdateParams"]


class LimitUpdateParams(TypedDict, total=False):
    max_concurrent_invocations: Optional[int]
    """Maximum concurrent app invocations for this project.

    Set to 0 to remove the cap; omit to leave unchanged.
    """

    max_concurrent_sessions: Optional[int]
    """Maximum concurrent browser sessions for this project.

    Set to 0 to remove the cap; omit to leave unchanged.
    """

    max_persistent_sessions: Optional[int]
    """Maximum persistent browser sessions for this project.

    Set to 0 to remove the cap; omit to leave unchanged.
    """

    max_pooled_sessions: Optional[int]
    """Maximum pooled sessions capacity for this project.

    Set to 0 to remove the cap; omit to leave unchanged.
    """
