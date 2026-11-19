from __future__ import annotations

import os
from typing import Optional

import httpx

from ._errors import WorkloadIdentityError

GRANT_TYPE_JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"
TOKEN_ENDPOINT_PATH = "/token"

# Seconds to wait on the token exchange and on identity-token requests.
TOKEN_EXCHANGE_TIMEOUT = 30.0

DEFAULT_API_BASE_URL = "https://api.onkernel.com"
DEFAULT_AUTH_BASE_URL = "https://auth.onkernel.com"

# Refresh thresholds, as time remaining before expiry. Each is the smaller of
# a fixed number of seconds and a fraction of the token's lifetime, so a token
# that lives for a few seconds is not refreshed on every request.
ADVISORY_REFRESH_SECONDS = 120.0
ADVISORY_REFRESH_FRACTION = 0.4
MANDATORY_REFRESH_SECONDS = 30.0
MANDATORY_REFRESH_FRACTION = 0.1

# Skip advisory refreshes for this long after one fails, so an outage of the
# token endpoint is not hit at request rate.
ADVISORY_REFRESH_BACKOFF_SECONDS = 5.0

# Provider JWTs are a few KiB. A larger assertion is a misconfiguration, such
# as a key or certificate path given as the token file.
MAX_ASSERTION_BYTES = 16 * 1024
MAX_RESPONSE_BYTES = 1 << 20

ENV_API_KEY = "KERNEL_API_KEY"
ENV_BASE_URL = "KERNEL_BASE_URL"
ENV_AUTH_BASE_URL = "KERNEL_AUTH_BASE_URL"
ENV_FEDERATION_RULE_ID = "KERNEL_FEDERATION_RULE_ID"
ENV_IDENTITY_TOKEN_SOURCE = "KERNEL_IDENTITY_TOKEN_SOURCE"
ENV_IDENTITY_TOKEN_AUDIENCE = "KERNEL_IDENTITY_TOKEN_AUDIENCE"
ENV_IDENTITY_TOKEN_FILE = "KERNEL_IDENTITY_TOKEN_FILE"
ENV_IDENTITY_TOKEN = "KERNEL_IDENTITY_TOKEN"

ENV_GITHUB_REQUEST_URL = "ACTIONS_ID_TOKEN_REQUEST_URL"
ENV_GITHUB_REQUEST_TOKEN = "ACTIONS_ID_TOKEN_REQUEST_TOKEN"

_LOOPBACK_HOSTS = frozenset(("localhost", "127.0.0.1", "::1"))


def user_agent() -> str:
    from ..._version import __version__

    return f"Kernel/Python {__version__}"


def require_https(url: str, *, field: str) -> None:
    """Reject a token endpoint that is not https. Plain http is allowed for loopback hosts only."""
    try:
        parsed = httpx.URL(url)
    except httpx.InvalidURL as err:
        raise WorkloadIdentityError(f"{field} is not a valid URL: {url!r}") from err
    if parsed.userinfo:
        # httpx would turn these into an Authorization header, which the token endpoint rejects.
        raise WorkloadIdentityError(f"{field} must not contain a username or password.")
    if parsed.scheme == "https" and parsed.host:
        return
    if parsed.scheme == "http" and parsed.host in _LOOPBACK_HOSTS:
        return
    raise WorkloadIdentityError(
        f"{field} must use https (got {url!r}). The token exchange carries credentials, "
        "so plain http is allowed only for localhost, 127.0.0.1 and ::1."
    )


def is_default_api_base_url(api_base_url: str) -> bool:
    return api_base_url.rstrip("/") == DEFAULT_API_BASE_URL


def resolve_auth_base_url(auth_base_url: Optional[str], *, api_base_url: str) -> str:
    """Explicit value, then `KERNEL_AUTH_BASE_URL`, then production when the API base URL is production."""
    resolved = auth_base_url or os.environ.get(ENV_AUTH_BASE_URL)
    field = "auth_base_url" if auth_base_url else ENV_AUTH_BASE_URL
    if not resolved:
        if not is_default_api_base_url(api_base_url):
            raise WorkloadIdentityError(
                f"The API base URL is {api_base_url!r}, so the auth base URL cannot be inferred. "
                f"Pass `auth_base_url=` or set {ENV_AUTH_BASE_URL} to the token endpoint host for that deployment."
            )
        resolved = DEFAULT_AUTH_BASE_URL
    resolved = resolved.rstrip("/")
    require_https(resolved, field=field)
    return resolved


def api_origin(api_base_url: str) -> str:
    """Scheme, host and port of the API base URL, with no path or trailing slash."""
    url = httpx.URL(api_base_url)
    return str(url.copy_with(userinfo=b"", path="/", query=None, fragment=None)).rstrip("/")


def api_base_url_from_env() -> str:
    """The API base URL a client constructed with no arguments would use."""
    return os.environ.get(ENV_BASE_URL) or DEFAULT_API_BASE_URL
