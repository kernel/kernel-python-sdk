# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProjectLimits"]


class ProjectLimits(BaseModel):
    max_concurrent_invocations: Optional[int] = None
    """Maximum concurrent app invocations for this project.

    Null means no project-level cap.
    """

    max_concurrent_sessions: Optional[int] = None
    """Maximum concurrent browser sessions for this project.

    Null means no project-level cap.
    """

    max_persistent_sessions: Optional[int] = None
    """Maximum persistent browser sessions for this project.

    Null means no project-level cap.
    """

    max_pooled_sessions: Optional[int] = None
    """Maximum pooled sessions capacity for this project.

    Null means no project-level cap.
    """
