# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProxyUpdateParams", "Config"]


class ProxyUpdateParams(TypedDict, total=False):
    config: Config
    """Changes to an ISP proxy's exit IP. Accepted only for proxies of type `isp`."""

    name: str
    """New proxy name.

    Proxy names are trimmed and length-checked only; duplicates are allowed because
    proxies are updated by ID, not by name.
    """


class Config(TypedDict, total=False):
    """Changes to an ISP proxy's exit IP. Accepted only for proxies of type `isp`."""

    ip_address: Required[str]
    """Reserved exit IP to move the proxy to.

    The IP must be active in the organization's allocation and in the proxy's
    country. The proxy keeps its ID. The new endpoint is probed before anything
    changes; a failed probe leaves the proxy as it was. Live browsers open new
    connections on the new IP within a few seconds; established connections drain on
    the old one.
    """
