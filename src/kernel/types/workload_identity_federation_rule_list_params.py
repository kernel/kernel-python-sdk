# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WorkloadIdentityFederationRuleListParams"]


class WorkloadIdentityFederationRuleListParams(TypedDict, total=False):
    issuer_id: str

    limit: int

    offset: int

    project_id: str

    query: str
    """Case-insensitive substring match against name or description; exact ID match."""

    service_account_id: str

    status: Literal["active", "archived", "all"]
