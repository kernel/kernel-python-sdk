# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .workload_identity_match_param import WorkloadIdentityMatchParam
from .workload_identity_target_param import WorkloadIdentityTargetParam
from .workload_identity_authorization_param import WorkloadIdentityAuthorizationParam

__all__ = ["WorkloadIdentityFederationRuleCreateParams"]


class WorkloadIdentityFederationRuleCreateParams(TypedDict, total=False):
    authorization: Required[WorkloadIdentityAuthorizationParam]

    expected_audience: Required[str]

    issuer_id: Required[str]

    match: Required[WorkloadIdentityMatchParam]

    name: Required[str]

    target: Required[WorkloadIdentityTargetParam]

    description: str

    enabled: bool
