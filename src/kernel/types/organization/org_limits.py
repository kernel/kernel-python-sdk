# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OrgLimits"]


class OrgLimits(BaseModel):
    default_project_max_concurrent_sessions: Optional[int] = None
    """
    Default maximum concurrent browsers applied to every project that has no
    explicit per-project override. Null means no org-level default, so such projects
    are uncapped (only the org-wide limit applies). Applies to existing and newly
    created projects.
    """

    max_concurrent_sessions: Optional[int] = None
    """
    The organization's effective concurrency limit — the maximum browsers running at
    once, covering both on-demand sessions and browser pool reservations — from its
    plan or an override. Read-only and shared across all projects in the org; a
    per-project default cannot exceed it.
    """
