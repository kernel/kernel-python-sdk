# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BrowserNetworkConfig", "ProxyRoute", "ProxyRouteProxy"]


class ProxyRouteProxy(BaseModel):
    """Select an active non-direct proxy by ID or name. Responses always use ID."""

    id: Optional[str] = None

    name: Optional[str] = None


class ProxyRoute(BaseModel):
    hosts: List[str]
    """Exact hostnames or leading \\**.

    wildcard patterns (subdomains only); patterns cannot include ports, and matching
    ignores the destination port. Hosts not matched by any route use the session's
    top-level proxy (or the browser default when proxy is omitted).
    """

    proxy: ProxyRouteProxy
    """Select an active non-direct proxy by ID or name. Responses always use ID."""


class BrowserNetworkConfig(BaseModel):
    """Network configuration for a browser session or browser pool."""

    allowed_hosts: Optional[List[str]] = None
    """
    Egress allowlist for a browser session: the only destinations the browser may
    reach through Kernel-managed egress. Any other destination is refused with a 403
    whose X-Kernel-Proxy-Error header is network_policy_denied, so pages cannot load
    or send data to unlisted hosts, including with fetch() and WebSockets. Omit the
    field for unfiltered egress; an empty list is invalid. The allowlist applies
    from the browser's first request, and start_url must be allowed by it. Entries
    are exact hostnames ("example.com"), one leading "_." wildcard that matches
    subdomains at any depth but not the domain itself ("_.example.com" matches
    api.example.com, not example.com), public IPv4 addresses ("8.8.8.8"), bracketed
    public IPv6 addresses ("[2001:4860:4860::8888]"), or public CIDR ranges in
    canonical form ("8.8.4.0/24", "2001:4860::/32"). IP and CIDR entries only match
    destinations written as an IP address, never hostnames that resolve into the
    range. Entries cannot include ports, paths, or schemes, and match every port on
    their host. Wildcards over a public suffix ("_.com", "_.github.io") and private
    or reserved IP ranges are rejected, as are entries that overlap private_hosts.
    Enforced at Kernel's egress proxy only: destinations in private_hosts, and
    processes in the browser VM that do not use the browser's proxy, are not
    filtered, and Kernel's own control traffic is always allowed. Requires proxy v3.
    Not supported on browser pools.
    """

    private_hosts: Optional[List[str]] = None
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

    proxy_routes: Optional[List[ProxyRoute]] = None
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
