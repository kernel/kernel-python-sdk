# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["OnePasswordCredentialVaultItemSpecInputParam", "Requests", "RequestsEntry", "RequestsEntryParameters"]


class RequestsEntryParameters(TypedDict, total=False):
    website: Required[str]


class RequestsEntry(TypedDict, total=False):
    parameters: Required[RequestsEntryParameters]

    type: Required[str]
    """Must be login."""

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


class OnePasswordCredentialVaultItemSpecInputParam(TypedDict, total=False):
    """
    A login request backed by a connected 1Password account or by a customer-supplied access token and matching integration key. Supply either account or both secrets, never both. Supplied secrets are write-only and never returned. Supply requests for new items; website remains supported for existing account-backed callers.
    """

    provider: Required[Literal["1password"]]

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

    website: str
    """Legacy single-login shorthand. Supply requests instead."""
