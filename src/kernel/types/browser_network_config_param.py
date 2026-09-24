# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BrowserNetworkConfigParam", "ProxyRoute", "ProxyRouteProxy"]


class ProxyRouteProxy(TypedDict, total=False):
    """Select an active non-direct proxy by ID or name. Responses always use ID."""

    id: str

    name: str


class ProxyRoute(TypedDict, total=False):
    hosts: Required[SequenceNotStr[str]]
    """Exact hostnames or leading \\**.

    wildcard patterns (subdomains only); patterns cannot include ports, and matching
    ignores the destination port. Hosts not matched by any route use the session's
    top-level proxy (or the browser default when proxy is omitted).
    """

    proxy: Required[ProxyRouteProxy]
    """Select an active non-direct proxy by ID or name. Responses always use ID."""


class BrowserNetworkConfigParam(TypedDict, total=False):
    """Network configuration for a browser session or browser pool."""

    private_hosts: SequenceNotStr[str]
    """
    Destinations the browser reaches directly through the session's own network
    instead of through Kernel-managed egress — for private hosts reachable over a
    VPN or tunnel the session has joined (e.g. a Tailscale tailnet). By default,
    private IP ranges already route directly: RFC1918 (10.0.0.0/8, 172.16.0.0/12,
    192.168.0.0/16), CGNAT/Tailscale (100.64.0.0/10), and IPv6 ULA (fc00::/7). An
    explicitly supplied list replaces those defaults with exactly the entries given,
    and an empty list ([]) disables them so all traffic uses Kernel-managed egress;
    omit private_hosts to keep the defaults. Entries are hostname patterns
    ("_.example.ts.net", "preview.internal") or IP/CIDR literals ("100.64.0.0/10",
    "10.1.30.63"). IP and CIDR entries only match URLs written with a literal IP
    address; they never match hostnames that resolve into the range, so private DNS
    names need a hostname entry even when they resolve inside the default ranges.
    CIDRs must be in canonical masked form (host bits zero), and only the private
    ranges listed above are accepted; public, loopback, link-local, and unspecified
    ranges are rejected. Exact IPv6 addresses must be bracketed ("[fd00::1]"); IPv6
    CIDR ranges are unbracketed ("fd00::/8"). Wildcards are limited to one leading
    "_." over a suffix with at least two labels that is not a public suffix (so
    "_.co.uk" or "_.ts.net" are rejected, while "\\**.example.ts.net" is accepted).
    Hostname and IP entries may carry a port; CIDR ranges may not. Hostname entries
    are not resolved during validation, so callers must ensure they identify private
    destinations. Not related to a proxy's bypass_hosts, which selects between
    upstream-proxy and Kernel-managed direct egress and cannot reach into a VPN.
    """

    proxy_routes: Iterable[ProxyRoute]
    """Per-destination proxy routes for a browser session.

    After setup, a destination hostname is matched against every route's hosts,
    regardless of port; route order does not matter. An exact hostname beats a
    wildcard, and a longer wildcard suffix beats a shorter one (for a.b.example.com:
    "a.b.example.com" > "_.b.example.com" > "_.example.com"). A host pattern may
    appear in only one route. "\\**.example.com" matches subdomains only, not
    example.com. A matched request selects the route's proxy instead of the
    session's top-level proxy (including mode: direct); the route proxy's own
    bypass_hosts still apply. If the route proxy becomes unavailable, matched
    requests fail closed without falling back. Requests that match no route use the
    session's default egress from the top-level proxy field (or the browser default
    when proxy is omitted: stealth proxy or direct egress). Routes take effect once
    the session is created; start_url and other traffic during browser setup use the
    top-level proxy. Setting routes requires proxy v3. Not supported on browser
    pools.
    """
