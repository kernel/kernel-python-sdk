# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvocationListParams"]


class InvocationListParams(TypedDict, total=False):
    action_name: str
    """Filter results by action name."""

    app_name: str
    """Filter results by application name."""

    deployment_id: str
    """Filter results by deployment ID."""

    limit: int
    """Limit the number of invocations to return."""

    offset: int
    """Offset the number of invocations to return."""

    query: str
    """Search invocations by ID, app name, or action name."""

    since: str
    """
    Show invocations that have started since the given time (RFC timestamps or
    durations like 5m).
    """

    status: Literal["queued", "running", "succeeded", "failed"]
    """Filter results by invocation status."""

    version: str
    """Filter results by application version."""
