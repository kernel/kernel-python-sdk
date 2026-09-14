# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VaultCheckoutContextParam"]


class VaultCheckoutContextParam(TypedDict, total=False):
    """Required when preparing an unused AgentCard card for Square.

    Consent is bound to this browser and declared merchant origin, not a tab. Wait for the item's ready_to_submit status before native Pay and submit within its readiness deadline. Unused preparations expire automatically; every preparation is single-use, including after failure or expiry.
    """

    browser_id: Required[str]
    """Active browser session with this vault bound to it."""

    environment: Required[Literal["production", "sandbox"]]
    """Square environment, independent of the AgentCard credential mode."""

    merchant_origin: Required[str]
    """Canonical HTTPS origin of the top-level merchant document, not the Square
    iframe.

    HTTP localhost is accepted for tests.
    """
