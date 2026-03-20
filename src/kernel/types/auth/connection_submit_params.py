# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["ConnectionSubmitParams"]


class ConnectionSubmitParams(TypedDict, total=False):
    fields: Dict[str, str]
    """Map of field name to value"""

    mfa_option_id: str
    """The MFA method type to select (when mfa_options were returned)"""

    sign_in_option_id: str
    """The sign-in option ID to select (when sign_in_options were returned)"""

    sso_button_selector: str
    """XPath selector for the SSO button to click (ODA).

    Use sso_provider instead for CUA.
    """

    sso_provider: str
    """
    SSO provider to click, matching the provider field from pending_sso_buttons
    (e.g., "google", "github"). Cannot be used with sso_button_selector.
    """
