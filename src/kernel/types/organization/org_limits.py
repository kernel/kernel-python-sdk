# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OrgLimits"]


class OrgLimits(BaseModel):
    auth_connections_used: int
    """
    The organization's current non-deleted managed auth connections, counted
    org-wide across every project. Compare against max_auth_connections to show
    remaining capacity before a create is rejected with 403 insufficient_plan.
    """

    max_auth_connections: Optional[int] = None
    """Maximum managed auth connections the organization's plan allows.

    Null means unlimited. Counted org-wide, so it cannot be multiplied across
    projects.
    """

    max_vaults: Optional[int] = None
    """Maximum non-deleted vaults allowed org-wide across all projects.

    Null means unlimited.
    """

    min_health_check_interval_seconds: int
    """
    Smallest health_check_interval the organization's plan accepts on a managed auth
    connection. Requests below this are rejected with 400. Existing connections
    stored below the floor are grandfathered until edited.
    """

    vaults_used: int
    """Current non-deleted vault count across all projects in the organization."""

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
