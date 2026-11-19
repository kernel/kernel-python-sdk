from __future__ import annotations

import os
import json
import pathlib
import importlib
import threading
from typing import Any, Dict, Tuple, Union, Optional
from urllib.parse import quote
from typing_extensions import override

import httpx

from ._http import BoundedResponse, send, async_send
from ._errors import WorkloadIdentityError
from ..._utils import asyncify
from ._constants import (
    ENV_IDENTITY_TOKEN,
    ENV_GITHUB_REQUEST_URL,
    ENV_IDENTITY_TOKEN_FILE,
    ENV_GITHUB_REQUEST_TOKEN,
    ENV_IDENTITY_TOKEN_AUDIENCE,
    require_https,
    api_base_url_from_env,
    resolve_auth_base_url,
)

__all__ = [
    "IdentityTokenFile",
    "StaticIdentityToken",
    "IdentityTokenSource",
    "GitHubActionsIdentityToken",
    "GCPMetadataIdentityToken",
    "AWSSTSIdentityToken",
]

_GCP_IDENTITY_URL = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"

# boto3 added `sts.get_web_identity_token` in this release.
MIN_BOTO3_VERSION = "1.41.0"


class IdentityTokenFile:
    """Reads the identity token from a file on every call.

    Tokens such as Kubernetes projected service-account tokens are rotated in
    place, so the file is never cached.
    """

    def __init__(self, path: Union[str, "os.PathLike[str]", None] = None) -> None:
        resolved = path if path is not None else os.environ.get(ENV_IDENTITY_TOKEN_FILE)
        if not resolved:
            raise WorkloadIdentityError(
                f"No identity token file path given. Pass a path or set the {ENV_IDENTITY_TOKEN_FILE} environment variable."
            )
        self._path = pathlib.Path(resolved)

    @property
    def path(self) -> pathlib.Path:
        return self._path

    def __call__(self) -> str:
        try:
            content = self._path.read_text(encoding="utf-8").strip()
        except FileNotFoundError as err:
            raise WorkloadIdentityError(f"Identity token file not found at {self._path}.") from err
        except IsADirectoryError as err:
            raise WorkloadIdentityError(
                f"Identity token path {self._path} is a directory. Point at the token file itself."
            ) from err
        except (OSError, UnicodeDecodeError) as err:
            # Only the error's type and OS reason: a decode error's message can quote file contents.
            reason = err.strerror if isinstance(err, OSError) else "not valid UTF-8"
            raise WorkloadIdentityError(
                f"Identity token file at {self._path} could not be read: {type(err).__name__}: {reason}"
            ) from None
        if not content:
            raise WorkloadIdentityError(
                f"Identity token file at {self._path} is empty. For a Kubernetes projected "
                "service-account token, check the volume mount and the projection's audience."
            )
        return content


class StaticIdentityToken:
    """A fixed identity token, good for exactly one exchange.

    Most providers' tokens can be exchanged only once, and an exchange that
    timed out may still have used the token. A second call therefore raises
    instead of sending the same token again.
    """

    def __init__(self, token: str) -> None:
        token = token.strip()
        if not token:
            raise WorkloadIdentityError("The static identity token is empty.")
        self._token: Optional[str] = token
        self._lock = threading.Lock()

    def __call__(self) -> str:
        with self._lock:
            token, self._token = self._token, None
        if token is None:
            raise WorkloadIdentityError(
                "The static identity token was already exchanged once and cannot be reused. "
                "Every exchange needs a fresh provider token, so a static token (such as "
                f"{ENV_IDENTITY_TOKEN}) lasts only until the first access token expires. For a "
                f"longer-running client, use {ENV_IDENTITY_TOKEN_FILE}, a built-in source "
                "(github_actions, gcp_metadata, aws_sts), or your own identity token provider."
            )
        return token


class IdentityTokenSource:
    """Base for the built-in sources that request a token for a given audience.

    A source is also a plain identity token provider: calling it fetches a
    token with its own HTTP client. `WorkloadIdentityCredentials` calls `fetch`
    or `async_fetch` instead, passing the auth base URL as the default audience
    and the API client's HTTP client.
    """

    def __init__(self, *, audience: Optional[str] = None) -> None:
        self._audience = audience

    def __call__(self) -> str:
        return self.fetch(default_audience=None, http_client=None)

    def audience(self, default_audience: Optional[str]) -> str:
        """Explicit audience, then `KERNEL_IDENTITY_TOKEN_AUDIENCE`, then the auth base URL."""
        return (
            self._audience
            or os.environ.get(ENV_IDENTITY_TOKEN_AUDIENCE)
            or default_audience
            or resolve_auth_base_url(None, api_base_url=api_base_url_from_env())
        )

    def fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.Client]) -> str:
        raise NotImplementedError

    async def async_fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.AsyncClient]) -> str:
        raise NotImplementedError


class GitHubActionsIdentityToken(IdentityTokenSource):
    """Requests a GitHub Actions OIDC token for the running job.

    The job needs `permissions: id-token: write`. The request URL stays valid
    for the whole job, so every exchange gets a new token.
    """

    _what = "the GitHub Actions identity token endpoint"

    @staticmethod
    def available() -> bool:
        return bool(os.environ.get(ENV_GITHUB_REQUEST_URL) and os.environ.get(ENV_GITHUB_REQUEST_TOKEN))

    @staticmethod
    def require_available() -> None:
        if not GitHubActionsIdentityToken.available():
            raise WorkloadIdentityError(
                f"{ENV_GITHUB_REQUEST_URL} and {ENV_GITHUB_REQUEST_TOKEN} are not set, so a GitHub Actions "
                "identity token cannot be requested. Add `permissions: id-token: write` to the workflow or job."
            )

    def _request(self, default_audience: Optional[str]) -> Tuple[str, Dict[str, str]]:
        self.require_available()
        url = os.environ[ENV_GITHUB_REQUEST_URL]
        require_https(url, field=ENV_GITHUB_REQUEST_URL)
        separator = "&" if "?" in url else "?"
        url = f"{url}{separator}audience={quote(self.audience(default_audience), safe='')}"
        request_token = os.environ[ENV_GITHUB_REQUEST_TOKEN].strip()
        headers = {"Authorization": f"Bearer {request_token}", "Accept": "application/json"}
        return url, headers

    def _token(self, response: BoundedResponse) -> str:
        if response.status_code != 200:
            raise WorkloadIdentityError(
                f"GitHub Actions identity token request failed (HTTP {response.status_code}). "
                "Check that the workflow or job has `permissions: id-token: write`."
            )
        try:
            value: object = json.loads(response.content)["value"]
        except (ValueError, KeyError, TypeError):
            value = None
        if not isinstance(value, str) or not value:
            raise WorkloadIdentityError("GitHub Actions identity token response did not contain a token.")
        return value

    @override
    def fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.Client]) -> str:
        url, headers = self._request(default_audience)
        return self._token(send(http_client, "GET", url, headers=headers, what=self._what))

    @override
    async def async_fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.AsyncClient]) -> str:
        url, headers = self._request(default_audience)
        return self._token(await async_send(http_client, "GET", url, headers=headers, what=self._what))


class GCPMetadataIdentityToken(IdentityTokenSource):
    """Requests an identity token for the attached service account from the Google Cloud metadata server.

    The request always goes directly to the metadata server. It does not use
    the API client's HTTP client, because a proxy configured there cannot
    reach the link-local metadata address.
    """

    _what = "the Google Cloud metadata server"

    def _request(self, default_audience: Optional[str]) -> Tuple[str, Dict[str, str]]:
        audience = quote(self.audience(default_audience), safe="")
        return f"{_GCP_IDENTITY_URL}?audience={audience}&format=full", {"Metadata-Flavor": "Google"}

    def _token(self, response: BoundedResponse) -> str:
        if response.status_code != 200:
            raise WorkloadIdentityError(
                f"Google Cloud metadata server identity token request failed (HTTP {response.status_code}). "
                "This source needs Google Cloud compute with a service account attached."
            )
        token = response.content.decode("utf-8", errors="replace").strip()
        if not token:
            raise WorkloadIdentityError("Google Cloud metadata server returned an empty identity token.")
        return token

    @override
    def fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.Client]) -> str:
        del http_client
        url, headers = self._request(default_audience)
        return self._token(send(None, "GET", url, headers=headers, what=self._what, trust_env=False))

    @override
    async def async_fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.AsyncClient]) -> str:
        del http_client
        url, headers = self._request(default_audience)
        return self._token(await async_send(None, "GET", url, headers=headers, what=self._what, trust_env=False))


class AWSSTSIdentityToken(IdentityTokenSource):
    """Requests a token from AWS STS `GetWebIdentityToken` with the workload's ambient AWS credentials.

    Needs boto3, which is an optional dependency: `pip install "kernel[aws]"`.
    The region comes from `region`, then `AWS_REGION`, then `AWS_DEFAULT_REGION`,
    and defaults to us-east-1. boto3 refreshes the ambient credentials itself,
    so every exchange gets a new token.
    """

    def __init__(self, *, audience: Optional[str] = None, region: Optional[str] = None) -> None:
        super().__init__(audience=audience)
        self._region = region
        self._sts_client: Any = None
        self._lock = threading.Lock()

    def _client(self) -> Any:
        with self._lock:
            if self._sts_client is None:
                self._sts_client = _regional_sts_client(
                    self._region or os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION") or "us-east-1"
                )
            return self._sts_client

    @override
    def fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.Client]) -> str:
        del http_client
        audience = self.audience(default_audience)
        client = self._client()
        try:
            response = client.get_web_identity_token(Audience=[audience], SigningAlgorithm="RS256", DurationSeconds=300)
        except Exception as err:
            # botocore errors (no credentials, access denied, federation not enabled) name the cause.
            raise WorkloadIdentityError(f"AWS STS GetWebIdentityToken failed: {type(err).__name__}: {err}") from err
        token = response.get("WebIdentityToken")
        if not isinstance(token, str) or not token:
            raise WorkloadIdentityError("AWS STS GetWebIdentityToken response did not contain a token.")
        return token

    @override
    async def async_fetch(self, *, default_audience: Optional[str], http_client: Optional[httpx.AsyncClient]) -> str:
        del http_client
        return await asyncify(self.fetch)(default_audience=default_audience, http_client=None)


def _regional_sts_client(region: str) -> Any:
    try:
        boto3: Any = importlib.import_module("boto3")
    except ImportError as err:
        raise WorkloadIdentityError(
            "The aws_sts identity token source needs boto3, which is not installed. "
            f'Install it with `pip install "kernel[aws]"` (boto3>={MIN_BOTO3_VERSION}).'
        ) from err

    client = boto3.client("sts", region_name=region)
    if not hasattr(client, "get_web_identity_token"):
        raise WorkloadIdentityError(
            f"The installed boto3 ({getattr(boto3, '__version__', 'unknown version')}) does not support STS "
            f'GetWebIdentityToken. Upgrade with `pip install -U "kernel[aws]"` (boto3>={MIN_BOTO3_VERSION}).'
        )
    # GetWebIdentityToken is not served by the global endpoint, which boto3
    # selects for some regions when AWS_STS_REGIONAL_ENDPOINTS=legacy.
    if client.meta.endpoint_url == "https://sts.amazonaws.com":
        client = boto3.client("sts", region_name=region, endpoint_url=f"https://sts.{region}.amazonaws.com")
    return client
