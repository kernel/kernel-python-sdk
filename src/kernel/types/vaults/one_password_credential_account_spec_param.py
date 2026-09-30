# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OnePasswordCredentialAccountSpecParam", "Authorization", "AuthorizationClient"]


class AuthorizationClient(TypedDict, total=False):
    type: Required[Literal["kernel_managed"]]


class Authorization(TypedDict, total=False):
    client: Required[AuthorizationClient]

    method: Required[Literal["oauth"]]


class OnePasswordCredentialAccountSpecParam(TypedDict, total=False):
    authorization: Required[Authorization]

    provider: Required[Literal["1password"]]
