# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    limit: int
    """Limit the number of tasks to return."""

    offset: int
    """Offset the number of tasks to return."""

    session_id: str
    """Only return tasks linked to this browser ID."""
