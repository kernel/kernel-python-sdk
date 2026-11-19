# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WorkloadIdentityTokenValidationParam"]


class WorkloadIdentityTokenValidationParam(TypedDict, total=False):
    max_lifetime_seconds: int
    """Maximum incoming signed exp minus iat, independent of outgoing token lifetime."""

    replay_protection: Literal["single_use", "allow_reuse"]
    """Whether an incoming token can be exchanged more than once before it expires.

    Defaults to single_use for github_actions, aws, microsoft_entra and custom_oidc,
    and to allow_reuse for kubernetes, because a pod reads the same projected token
    until it is rotated. google_cloud is always allow_reuse because Google identity
    tokens carry no token ID. allow_reuse can be set on microsoft_entra and
    custom_oidc, and single_use on kubernetes. github_actions and aws are always
    single_use.
    """
