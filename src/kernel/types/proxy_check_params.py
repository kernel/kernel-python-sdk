# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProxyCheckParams"]


class ProxyCheckParams(TypedDict, total=False):
    url: str
    """An optional URL to test reachability against.

    If provided, the proxy check will test connectivity to this URL instead of the
    default test URLs. Only HTTP and HTTPS schemes are allowed, and the URL must
    resolve to a public IP address. For ISP and datacenter proxies, the exit IP is
    stable, so a successful check reliably indicates that subsequent browser
    sessions will reach the target site with the same IP. For residential and mobile
    proxies, the exit node changes between requests, so a successful check validates
    proxy configuration but does not guarantee that a subsequent browser session
    will use the same exit IP or reach the same site — it is useful for verifying
    credentials and connectivity, not for predicting site-specific behavior.
    """
