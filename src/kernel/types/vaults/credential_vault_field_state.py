# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CredentialVaultFieldState"]


class CredentialVaultFieldState(BaseModel):
    has_value: bool

    value: Optional[str] = None
    """Present exactly when has_value is true and the field is not sensitive.

    Reflects the latest developer or human edit. For totp, has_value indicates a
    stored seed; neither the seed nor a generated code is returned.
    """
