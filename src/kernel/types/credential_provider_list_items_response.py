# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .credential_provider_item import CredentialProviderItem

__all__ = ["CredentialProviderListItemsResponse"]


class CredentialProviderListItemsResponse(BaseModel):
    items: Optional[List[CredentialProviderItem]] = None
