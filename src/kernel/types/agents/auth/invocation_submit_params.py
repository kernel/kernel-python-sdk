# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["InvocationSubmitParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    field_values: Required[Dict[str, str]]
    """Values for the discovered login fields"""


class Variant1(TypedDict, total=False):
    sso_button: Required[str]
    """Selector of SSO button to click"""


class Variant2(TypedDict, total=False):
    selected_mfa_type: Required[Literal["sms", "call", "email", "totp", "push", "security_key"]]
    """The MFA delivery method type"""


InvocationSubmitParams: TypeAlias = Union[Variant0, Variant1, Variant2]
