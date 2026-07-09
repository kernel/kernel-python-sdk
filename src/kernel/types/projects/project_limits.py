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
    """
    Maximum concurrent browsers for this project, covering both on-demand sessions
    (`browsers.create()`) and browser pool reservations. Null means no project-level
    cap.
    """

    max_pooled_sessions: Optional[int] = None
    """Deprecated: pooled browsers now count toward `max_concurrent_sessions`.

    Always null once the unified concurrency limit is enabled for your organization.
    """
