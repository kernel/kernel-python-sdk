# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    app_name: str
    """Filter results by application name."""

    app_version: str
    """Filter results by application version. Requires app_name to be set."""

    limit: int
    """Limit the number of deployments to return."""

    offset: int
    """Offset the number of deployments to return."""
