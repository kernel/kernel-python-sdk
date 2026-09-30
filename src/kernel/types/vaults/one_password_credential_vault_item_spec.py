# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordCredentialVaultItemSpec", "Requests", "RequestsEntry", "RequestsEntryParameters"]


class RequestsEntryParameters(BaseModel):
    website: str


class RequestsEntry(BaseModel):
    parameters: RequestsEntryParameters

    type: str
    """Must be login."""

    keywords: Optional[List[str]] = None

    reason: Optional[str] = None


class Requests(BaseModel):
    """Credential Request v2 input sent to the extension.

    A credential item may request up to five login entries.
    """

    entries: List[RequestsEntry]

    version: int
    """Must be 2."""

    goal: Optional[str] = None


class OnePasswordCredentialVaultItemSpec(BaseModel):
    """
    Stored-token credentials omit account and never return access_token or integration_key.
    """

    provider: Literal["1password"]

    requests: Requests
    """Credential Request v2 input sent to the extension.

    A credential item may request up to five login entries.
    """

    access_token_expires_at: Optional[datetime] = None
    """Customer-supplied expiry metadata, if provided."""

    account: Optional[str] = None
