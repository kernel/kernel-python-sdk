# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProxyUpdateParams"]


class ProxyUpdateParams(TypedDict, total=False):
    name: Required[str]
    """New proxy name.

    Proxy names are trimmed and length-checked only; duplicates are allowed because
    proxies are updated by ID, not by name.
    """
