# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordCredentialAccountSpec", "Authorization", "AuthorizationClient"]


class AuthorizationClient(BaseModel):
    type: Literal["kernel_managed"]


class Authorization(BaseModel):
    client: AuthorizationClient

    method: Literal["oauth"]


class OnePasswordCredentialAccountSpec(BaseModel):
    authorization: Authorization

    provider: Literal["1password"]
