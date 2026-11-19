# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkloadIdentityTokenValidation"]


class WorkloadIdentityTokenValidation(BaseModel):
    max_lifetime_seconds: Optional[int] = None
    """Maximum incoming signed exp minus iat, independent of outgoing token lifetime."""

    replay_protection: Optional[Literal["single_use", "allow_reuse"]] = None
    """Whether an incoming token can be exchanged more than once before it expires.

    Defaults to single_use for github_actions, aws, microsoft_entra and custom_oidc,
    and to allow_reuse for kubernetes, because a pod reads the same projected token
    until it is rotated. google_cloud is always allow_reuse because Google identity
    tokens carry no token ID. allow_reuse can be set on microsoft_entra and
    custom_oidc, and single_use on kubernetes. github_actions and aws are always
    single_use.
    """
