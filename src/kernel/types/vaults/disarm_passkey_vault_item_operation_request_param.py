# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DisarmPasskeyVaultItemOperationRequestParam"]


class DisarmPasskeyVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Stop a browser from using this item's passkeys: removes its armed
    passkeys and its pending registration into this item. Pages that already
    loaded keep Kernel's WebAuthn handler but get the browser's own behavior.
    """

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    type: Required[Literal["disarm_passkey"]]

    field: str
    """Limit disarming to one passkey field.

    Omit to disarm every passkey field of the item.
    """
