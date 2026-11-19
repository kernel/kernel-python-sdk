# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKeyPrincipal"]


class APIKeyPrincipal(BaseModel):
    id: str

    type: Literal["user", "service_account"]
