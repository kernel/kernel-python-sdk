# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReportListParams"]


class ReportListParams(TypedDict, total=False):
    task_id: Required[str]
    """Task whose reports to list."""

    limit: int
    """Limit the number of reports to return."""

    offset: int
    """Offset the number of reports to return."""

    type: str
    """Only return reports of this type."""
