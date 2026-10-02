# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ManagedAuthCredentialVaultItemSpecInputParam"]


class ManagedAuthCredentialVaultItemSpecInputParam(TypedDict, total=False):
    """A credential backed by a managed auth connection.

    The item stores no values:
    it reads the connection's saved credential at fill time, so updates made
    through managed auth apply immediately. The connection must be in the vault's
    project and hold a saved Kernel credential. The check is the saved credential,
    not connection status: a connection that needs re-authentication qualifies,
    and an authenticated one without a saved credential does not. Returns 404 for
    an unknown connection, and 409 when the connection is in another project, has
    no saved credential yet, or uses an external credential provider such as
    1Password. No collection form is offered; managed auth collects the login.
    """

    connection_id: Required[str]
    """ID of the managed auth connection whose saved credential this item reads.

    List connections with `GET /auth/connections`.
    """

    provider: Required[Literal["managed_auth"]]

    description: str
    """Optional display text for the item, such as the site or service name.

    Set at creation and cannot be changed later; repeating the request with a
    different description returns 409. At most 16 KiB in UTF-8 bytes.
    """
