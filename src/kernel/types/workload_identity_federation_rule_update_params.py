# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .workload_identity_match_param import WorkloadIdentityMatchParam
from .workload_identity_target_param import WorkloadIdentityTargetParam
from .workload_identity_authorization_param import WorkloadIdentityAuthorizationParam

__all__ = ["WorkloadIdentityFederationRuleUpdateParams"]


class WorkloadIdentityFederationRuleUpdateParams(TypedDict, total=False):
    expected_version: Required[int]

    authorization: WorkloadIdentityAuthorizationParam

    description: str

    enabled: bool

    expected_audience: str

    issuer_id: str

    match: WorkloadIdentityMatchParam

    name: str

    target: WorkloadIdentityTargetParam
