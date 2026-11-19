# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .browser_proxy_mode import BrowserProxyMode

__all__ = ["BrowserProxyConfig"]


class BrowserProxyConfig(BaseModel):
    """Browser proxy configuration.

    Provide exactly one of mode, id, or name; an empty object is invalid.
    Set mode to direct for no proxy. Set mode to default to use Kernel's default stealth proxy for browsers with CAPTCHA solving enabled, including stealth browsers, or direct egress otherwise.
    Select id or name to use that proxy. The selected proxy must be in the same project as the browser. Names must match exactly one active proxy; use id for stable references.
    Proxy configuration changes only egress and does not change CAPTCHA solver behavior. A browser using mode=direct keeps the CAPTCHA solver if it was enabled.
    When proxy is omitted on browser creation, stealth browsers use Kernel's default stealth proxy and other browsers use direct egress. When omitted on update, the current configuration is unchanged.
    """

    id: Optional[str] = None
    """Proxy ID."""

    mode: Optional[BrowserProxyMode] = None
    """Proxy egress mode.

    direct forces no proxy. default uses Kernel's default stealth proxy for browsers
    with CAPTCHA solving enabled, including stealth browsers, or direct egress
    otherwise. default is primarily useful on browser update to restore the browser
    default after selected-proxy egress.
    """

    name: Optional[str] = None
    """Proxy name. Must match exactly one active proxy in the project."""
