# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WorkloadIdentityPresetType"]

WorkloadIdentityPresetType: TypeAlias = Literal[
    "github_actions", "aws", "google_cloud", "microsoft_entra", "kubernetes", "custom_oidc"
]
