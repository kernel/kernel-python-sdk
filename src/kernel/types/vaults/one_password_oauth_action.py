# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordOAuthAction"]


class OnePasswordOAuthAction(BaseModel):
    name: Literal["1password_oauth"]

    url: str
    """1Password-hosted OAuth authorization URL for the human to open."""
