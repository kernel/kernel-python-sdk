# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "OnePasswordCredentialVaultItemSpecInputParam",
    "Requests",
    "RequestsEntry",
    "RequestsEntryParameters",
    "Resolved",
]


class RequestsEntryParameters(TypedDict, total=False):
    website: Required[str]


class RequestsEntry(TypedDict, total=False):
    parameters: Required[RequestsEntryParameters]

    type: Required[str]
    """Must be login."""

    id: str
    """1Password's ID for this entry in an access request you created.

    Supply it only with resolved.
    """

    keywords: SequenceNotStr[str]

    reason: str


class Requests(TypedDict, total=False):
    """Credential Request v2 input sent to the extension.

    A credential item may request up to five login entries.
    """

    entries: Required[Iterable[RequestsEntry]]

    version: Required[int]
    """Must be 2."""

    goal: str


class Resolved(TypedDict, total=False):
    reference: Required[str]
    """1Password credential reference.

    Pass it unchanged as resourcePath to the extension's fillCredential or to the
    1Password SDK.
    """

    entry_id: Annotated[str, PropertyInfo(alias="entryId")]
    """The requested entry this login satisfies, when known."""


class OnePasswordCredentialVaultItemSpecInputParam(TypedDict, total=False):
    """
    A login request backed by a connected 1Password account or by a customer-supplied access token and matching integration key. Supply either account or both secrets, never both. Supplied secrets are write-only and never returned. Supply requests for new items; website remains supported for existing account-backed callers. To use an access request you already created and the user approved with the same access token and integration key, also supply access_request_id, resolved, and each requests entry's id; the item is created ready and Kernel doesn't create an access request.
    """

    provider: Required[Literal["1password"]]

    access_request_id: str
    """
    ID of an approved access request you created with this access_token and
    integration_key. Requires resolved.
    """

    access_token: str
    """Customer-supplied 1Password broker token.

    Requires integration_key; stored encrypted on this item. Omit if providing a
    connected credential_account item via the account field.
    """

    access_token_expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional supplied token expiry metadata for stored-token credentials.

    Omit if providing a connected credential_account item via the account field.
    """

    account: str
    """Key of a connected credential_account item in the same vault.

    Omit for stored-token credentials.
    """

    integration_key: str
    """Matching customer-supplied integration key.

    Requires access_token; stored encrypted on this item. Omit if providing a
    connected credential_account item via the account field.
    """

    requests: Requests
    """Credential Request v2 input sent to the extension.

    A credential item may request up to five login entries.
    """

    resolved: Iterable[Resolved]
    """
    Granted logins from 1Password's status for access_request_id, as returned by the
    1Password SDK or extension. Requires access_request_id and an id on every
    requests entry. entryId may be omitted only when requests has one entry. Kernel
    doesn't verify the references; 1Password checks them when filling.
    """

    website: str
    """Legacy single-login shorthand. Supply requests instead."""
