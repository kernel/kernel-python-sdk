# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["ConnectionSubmitParams"]


class ConnectionSubmitParams(TypedDict, total=False):
    fields: Dict[str, str]
    """Map of field name to value"""

    mfa_option_id: str
    """Optional MFA option ID if user selected an MFA method"""

    sso_button_selector: str
    """Optional XPath selector if user chose to click an SSO button instead"""
