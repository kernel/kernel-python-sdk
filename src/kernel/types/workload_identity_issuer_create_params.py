# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .workload_identity_preset_type import WorkloadIdentityPresetType
from .workload_identity_key_source_param import WorkloadIdentityKeySourceParam
from .workload_identity_token_validation_param import WorkloadIdentityTokenValidationParam

__all__ = ["WorkloadIdentityIssuerCreateParams"]


class WorkloadIdentityIssuerCreateParams(TypedDict, total=False):
    name: Required[str]

    description: str

    enabled: bool

    issuer_url: str
    """Exact expected signed issuer.

    Optional for github_actions and google_cloud, which each have one fixed issuer.
    """

    jwks: WorkloadIdentityKeySourceParam

    preset_type: WorkloadIdentityPresetType
    """The kind of identity provider.

    GitHub Actions, Google Cloud and Microsoft Entra issuers are recognized by their
    issuer URL and must use their own type. Defaults to the type the issuer URL
    belongs to, or custom_oidc.
    """

    token_validation: WorkloadIdentityTokenValidationParam
