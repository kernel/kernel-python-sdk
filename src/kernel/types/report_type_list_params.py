# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReportTypeListParams"]


class ReportTypeListParams(TypedDict, total=False):
    task_id: Required[str]
    """Task the agent is finding a report type for."""

    limit: int
    """Limit the number of report types to return."""

    offset: int
    """Offset the number of report types to return."""

    query: str
    """What the agent wants to report, in its own words.

    Types are ranked by how closely their meaning matches, most relevant first; they
    need not share any words. Only this text affects the ranking, not the task.
    Without it, or if ranking is unavailable, types are listed by name.
    """
