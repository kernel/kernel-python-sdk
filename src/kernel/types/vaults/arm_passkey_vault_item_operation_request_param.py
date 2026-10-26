# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ArmPasskeyVaultItemOperationRequestParam"]


class ArmPasskeyVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Let a browser attached to the item's vault sign in with a stored passkey.
    Only invoke when the item advertises `arm_passkey`. Returns immediately;
    there is no time limit. While armed, when a page in that browser whose
    origin matches the passkey's relying party asks for a passkey
    (`navigator.credentials.get`, including autofill requests made at page
    load), Kernel answers with this passkey. The private key never enters the
    browser: Kernel signs on its servers, using the origin Chrome reports for
    the requesting frame. Arming a passkey for a relying party replaces any
    passkey armed earlier in the browser for the same relying party. The arm
    lasts until `disarm_passkey`, the browser ends, the vault is detached, or
    the item or field is deleted. Drive the sign-in with your own browser
    tools and inspect the page to confirm it. A page opened in a new tab
    or window can run its first scripts before Kernel's handler attaches;
    if such a page asks for a passkey as soon as it loads, reload it. While
    armed, any script running on the relying party's pages can obtain a
    sign-in without user interaction, as with a password manager that
    fills automatically; disarm when the task is done. Passkeys report a
    signature counter of 0 and backup flags, as synced passkeys do.
    """

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    type: Required[Literal["arm_passkey"]]

    field: str
    """Passkey field to arm.

    Required when more than one passkey field holds a passkey.
    """
