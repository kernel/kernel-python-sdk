# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OnePasswordCredentialVaultItemState",
    "AccessRequest",
    "AccessRequestEntry",
    "AccessRequestEntryParameters",
    "AccessRequestRequest",
    "AccessRequestRequestEntry",
    "AccessRequestRequestEntryParameters",
    "AccessRequestResolved",
]


class AccessRequestEntryParameters(BaseModel):
    website: Optional[str] = None


class AccessRequestEntry(BaseModel):
    id: Optional[str] = None

    keywords: Optional[List[str]] = None

    parameters: Optional[AccessRequestEntryParameters] = None

    reason: Optional[str] = None

    type: Optional[str] = None


class AccessRequestRequestEntryParameters(BaseModel):
    website: Optional[str] = None


class AccessRequestRequestEntry(BaseModel):
    id: Optional[str] = None

    keywords: Optional[List[str]] = None

    parameters: Optional[AccessRequestRequestEntryParameters] = None

    reason: Optional[str] = None

    type: Optional[str] = None


class AccessRequestRequest(BaseModel):
    """The request object if returned by the extension.

    The observed create response may omit entries; no entry IDs are invented.
    """

    entries: Optional[List[AccessRequestRequestEntry]] = None

    goal: Optional[str] = None

    version: Optional[int] = None


class AccessRequestResolved(BaseModel):
    reference: str
    """1Password credential reference.

    Pass it unchanged as resourcePath to the extension's fillCredential or to the
    1Password SDK.
    """

    entry_id: Optional[str] = FieldInfo(alias="entryId", default=None)
    """The requested entry this login satisfies, when known."""


class AccessRequest(BaseModel):
    """Non-secret broker state.

    Granted credential references are returned in resolved only for credentials with a customer-supplied access token; otherwise they stay encrypted server-side and can only be used by the fill operation.
    """

    id: str

    has_autofill_token: bool

    state: str
    """One of pending, resolved, denied, or failed."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Provider-created timestamp as returned by the broker."""

    entries: Optional[List[AccessRequestEntry]] = None
    """Login entries returned directly on accessRequest by the observed extension
    build.

    Omitted when the provider does not supply them.
    """

    goal: Optional[str] = None
    """Goal echoed by the observed createAccessRequest response when present."""

    granted_count: Optional[int] = None

    identity: Optional[str] = None
    """Opaque provider identity returned by the broker."""

    path: Optional[str] = None
    """Provider path if supplied in the broker response."""

    request: Optional[AccessRequestRequest] = None
    """The request object if returned by the extension.

    The observed create response may omit entries; no entry IDs are invented.
    """

    resolved: Optional[List[AccessRequestResolved]] = None
    """Granted logins in the shape 1Password's getAccessRequestStatus returns.

    Present only for ready credentials with a customer-supplied access token, on
    single-item responses to callers that can use the vault. Each reference works
    only with that credential's access token and integration key.
    """


class OnePasswordCredentialVaultItemState(BaseModel):
    provider: Literal["1password"]

    status: Literal["pending_authorization", "ready", "declined", "failed"]

    access_request: Optional[AccessRequest] = None
    """Non-secret broker state.

    Granted credential references are returned in resolved only for credentials with
    a customer-supplied access token; otherwise they stay encrypted server-side and
    can only be used by the fill operation.
    """

    access_request_id: Optional[str] = None
    """
    Opaque request ID returned by the 1Password broker after a successful
    createAccessRequest call.
    """

    status_reason: Optional[str] = None
