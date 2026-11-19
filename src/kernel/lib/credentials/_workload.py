from __future__ import annotations

import json
import math
import time
import inspect
from typing import Dict, Union, Mapping, Optional, cast
from dataclasses import dataclass

import httpx

from ._http import BoundedResponse, send, async_send
from ._types import (
    Principal,
    AccessTokenProvider,
    FederationAccessToken,
    IdentityTokenProvider,
    AsyncAccessTokenProvider,
    AsyncIdentityTokenProvider,
    is_async_callable,
)
from ._errors import WorkloadIdentityError
from ..._utils import asyncify
from ._constants import (
    ENV_IDENTITY_TOKEN,
    MAX_ASSERTION_BYTES,
    TOKEN_ENDPOINT_PATH,
    GRANT_TYPE_JWT_BEARER,
    api_origin,
    require_https,
    api_base_url_from_env,
    resolve_auth_base_url,
)
from ._providers import IdentityTokenFile, IdentityTokenSource, StaticIdentityToken

__all__ = [
    "WorkloadIdentityCredentials",
    "WorkloadIdentityError",
    "exchange_federation_assertion",
    "async_exchange_federation_assertion",
]

_OAUTH_ERROR_FIELDS = ("error", "error_description", "error_uri")

# Longest OAuth error field kept on an error. A misrouted endpoint could echo
# the request back, so this bounds how much of it can reach logs.
_MAX_ERROR_FIELD_CHARS = 256

_REPLAY_HINT = "Every exchange needs a fresh provider token: most identity providers' tokens can be exchanged only once"
_ONE_SHOT_REPLAY_HINT = f"{_REPLAY_HINT}, so the same assertion cannot be exchanged again."
_RESOURCE_HINT = "Set resource to the Kernel API origin with no trailing slash."


def _replay_hint(provider: object) -> str:
    """What to do about "Credential was already used", for where the identity token came from."""
    if isinstance(provider, StaticIdentityToken):
        return f"{_REPLAY_HINT}, so a static {ENV_IDENTITY_TOKEN} works for a single exchange."
    if isinstance(provider, IdentityTokenFile):
        return (
            f"{_REPLAY_HINT}. The file at {provider.path} still held a token that had already been exchanged, "
            "so whatever writes that file must rotate it before each refresh. For Kubernetes projected "
            "service-account tokens, the issuer can be configured to allow reuse instead."
        )
    return f"{_REPLAY_HINT}, so the identity token provider must return a newly issued token on every call."


_WHAT = "the token endpoint"


def _validated_assertion(token: object) -> str:
    if inspect.isawaitable(token):
        if inspect.iscoroutine(token):
            # Closing it stops Python warning that the coroutine was never awaited.
            token.close()
        raise TypeError("The identity token provider is async and cannot be awaited here; use `AsyncKernel` instead.")
    if not isinstance(token, str):
        raise TypeError(f"The identity token provider returned {type(token).__name__} instead of a str.")
    token = token.strip()
    if not token:
        raise WorkloadIdentityError("The identity token provider returned an empty token.")
    size = len(token.encode("utf-8"))
    if size > MAX_ASSERTION_BYTES:
        raise WorkloadIdentityError(
            f"The identity token is {size} bytes, over the {MAX_ASSERTION_BYTES}-byte limit. That is almost "
            "certainly not a JWT; check that the identity token source points at the token, not a key or certificate."
        )
    return token


def _redacted(value: str, *, assertion: str) -> str:
    value = value.replace(assertion, "[REDACTED]")
    if len(value) > _MAX_ERROR_FIELD_CHARS:
        value = value[:_MAX_ERROR_FIELD_CHARS] + "..."
    return value


def _redacted_error_fields(payload: object, *, assertion: str) -> Dict[str, str]:
    """The OAuth error fields of an error response, with the assertion removed and long values cut."""
    if not isinstance(payload, dict):
        return {}
    fields: Dict[str, str] = {}
    for key in _OAUTH_ERROR_FIELDS:
        value = cast("Dict[str, object]", payload).get(key)
        if isinstance(value, str):
            fields[key] = _redacted(value, assertion=assertion)
    return fields


def _request_id(headers: httpx.Headers, *, assertion: str) -> Optional[str]:
    request_id: Optional[str] = headers.get("x-request-id") or headers.get("request-id")
    return _redacted(request_id, assertion=assertion) if request_id else None


def _parse_json(content: bytes) -> object:
    try:
        return json.loads(content)
    except ValueError:
        return None


def _exchange_error(response: BoundedResponse, *, assertion: str, replay_hint: str) -> WorkloadIdentityError:
    fields = _redacted_error_fields(_parse_json(response.content), assertion=assertion)
    error = fields.get("error")
    description = fields.get("error_description")

    message = f"Token exchange failed (HTTP {response.status_code})"
    detail = ": ".join(part for part in (error, description) if part)
    if detail:
        message = f"{message}: {detail}"
    if error == "invalid_grant" and description and "already used" in description.lower():
        message = f"{message}. {replay_hint}"
    elif error == "invalid_target":
        message = f"{message}. {_RESOURCE_HINT}"
    return WorkloadIdentityError(
        message,
        status_code=response.status_code,
        error=error,
        error_description=description,
        request_id=_request_id(response.headers, assertion=assertion),
        body=fields,
    )


def _parse_exchange_response(
    response: BoundedResponse, *, assertion: str, requested_at: float, replay_hint: str
) -> FederationAccessToken:
    if response.status_code != 200:
        raise _exchange_error(response, assertion=assertion, replay_hint=replay_hint)

    status_code = response.status_code
    request_id = _request_id(response.headers, assertion=assertion)

    # Nothing from a success body goes into an error message: it holds the access token.
    def malformed(reason: str) -> WorkloadIdentityError:
        return WorkloadIdentityError(
            f"Token endpoint returned an unusable response: {reason}.", status_code=status_code, request_id=request_id
        )

    payload = _parse_json(response.content)
    if not isinstance(payload, dict):
        raise malformed("the body is not a JSON object")
    data = cast("Dict[str, object]", payload)

    token_type = data.get("token_type")
    if token_type is not None and not (isinstance(token_type, str) and token_type.lower() == "bearer"):
        raise malformed("token_type is not Bearer")

    access_token = data.get("access_token")
    if not isinstance(access_token, str) or not access_token:
        raise malformed("access_token is missing")

    expires_in = data.get("expires_in")
    if isinstance(expires_in, bool) or not isinstance(expires_in, (int, float)):
        raise malformed("expires_in is missing or not a number")
    if not math.isfinite(expires_in) or expires_in <= 0:
        raise malformed("expires_in is not a positive number")

    principal: Optional[Principal] = None
    raw_principal = data.get("principal")
    if isinstance(raw_principal, dict):
        principal_type = cast("Dict[str, object]", raw_principal).get("type")
        principal_id = cast("Dict[str, object]", raw_principal).get("id")
        if isinstance(principal_type, str) and isinstance(principal_id, str):
            principal = Principal(type=principal_type, id=principal_id)

    def optional_str(key: str) -> Optional[str]:
        value = data.get(key)
        return value if isinstance(value, str) else None

    return FederationAccessToken(
        token=access_token,
        # Counted from before the request was sent, so the token is never
        # believed to outlive what the server issued.
        expires_at=requested_at + expires_in,
        scope=optional_str("scope"),
        project_id=optional_str("project_id"),
        principal=principal,
        federation_rule_id=optional_str("federation_rule_id"),
    )


@dataclass(frozen=True)
class _Exchange:
    """One resolved exchange configuration: where to POST, and with what."""

    identity_token_provider: Union[IdentityTokenProvider, AsyncIdentityTokenProvider]
    federation_rule_id: str
    auth_base_url: str
    resource: Optional[str]
    replay_hint: Optional[str] = None
    """Overrides the hint derived from the kind of identity token provider."""

    @property
    def _url(self) -> str:
        return f"{self.auth_base_url}{TOKEN_ENDPOINT_PATH}"

    def _form(self, assertion: str) -> Dict[str, str]:
        # The token endpoint rejects any parameter other than these four.
        form = {
            "grant_type": GRANT_TYPE_JWT_BEARER,
            "assertion": assertion,
            "federation_rule_id": self.federation_rule_id,
        }
        if self.resource is not None:
            form["resource"] = self.resource
        return form

    @property
    def _headers(self) -> Mapping[str, str]:
        # The form content type is set explicitly so nothing along the way can infer another.
        return {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

    def run(self, http_client: Optional[httpx.Client]) -> FederationAccessToken:
        provider = self.identity_token_provider
        if isinstance(provider, IdentityTokenSource):
            token: object = provider.fetch(default_audience=self.auth_base_url, http_client=http_client)
        else:
            token = provider()
        assertion = _validated_assertion(token)

        requested_at = time.time()
        response = send(http_client, "POST", self._url, headers=self._headers, data=self._form(assertion), what=_WHAT)
        return _parse_exchange_response(
            response,
            assertion=assertion,
            requested_at=requested_at,
            replay_hint=self.replay_hint or _replay_hint(self.identity_token_provider),
        )

    async def async_run(self, http_client: Optional[httpx.AsyncClient]) -> FederationAccessToken:
        provider = self.identity_token_provider
        if isinstance(provider, IdentityTokenSource):
            token: object = await provider.async_fetch(default_audience=self.auth_base_url, http_client=http_client)
        elif is_async_callable(provider):
            token = await provider()
        else:
            # A sync provider may block, on a file read for instance, so it runs off the event loop.
            token = await asyncify(provider)()
            if inspect.isawaitable(token):
                token = await token
        assertion = _validated_assertion(token)

        requested_at = time.time()
        response = await async_send(
            http_client, "POST", self._url, headers=self._headers, data=self._form(assertion), what=_WHAT
        )
        return _parse_exchange_response(
            response,
            assertion=assertion,
            requested_at=requested_at,
            replay_hint=self.replay_hint or _replay_hint(self.identity_token_provider),
        )


class _ClientExchange:
    """The `AccessTokenProvider` a `Kernel` client uses: exchanges through that client's HTTP client."""

    def __init__(self, exchange: _Exchange, http_client: httpx.Client) -> None:
        self._exchange = exchange
        self._http_client = http_client

    def __call__(self, *, force_refresh: bool = False) -> FederationAccessToken:
        del force_refresh  # Every call is a new exchange; there is no cache to bypass.
        return self._exchange.run(self._http_client)


class _AsyncClientExchange:
    """The `AsyncAccessTokenProvider` an `AsyncKernel` client uses."""

    def __init__(self, exchange: _Exchange, http_client: httpx.AsyncClient) -> None:
        self._exchange = exchange
        self._http_client = http_client

    async def __call__(self, *, force_refresh: bool = False) -> FederationAccessToken:
        del force_refresh
        return await self._exchange.async_run(self._http_client)


class WorkloadIdentityCredentials:
    """Exchanges the workload's own identity token for a short-lived Kernel access token.

    Pass it as `credentials=` to `Kernel` or `AsyncKernel`. The client caches
    the access token and exchanges again shortly before it expires. Every
    exchange calls `identity_token_provider` for a new identity token, because
    most providers' tokens can be exchanged only once.

    Args:
        identity_token_provider: Returns the workload's identity token (a JWT).
            May be an `async def` function when used with `AsyncKernel`; a sync
            provider is run in a worker thread there.
        federation_rule_id: The `wifr_...` ID of the federation rule to match.
        resource: The API the access token is for. A client the credentials
            are passed to defaults it to the origin of its base URL, such as
            `https://api.onkernel.com`.
        auth_base_url: Where the token endpoint is. Defaults to
            `KERNEL_AUTH_BASE_URL`, then to `https://auth.onkernel.com` when the
            client uses the production API. With any other API base URL it has
            to be set.
        http_client: The HTTP client for exchanges made by calling this object
            directly. A client the credentials are passed to uses its own.

    Calling the object performs one exchange and returns the access token,
    without caching. Like `exchange_federation_assertion`, that exchange sends
    `resource` only when it was given.
    """

    def __init__(
        self,
        *,
        identity_token_provider: Union[IdentityTokenProvider, AsyncIdentityTokenProvider],
        federation_rule_id: str,
        resource: Optional[str] = None,
        auth_base_url: Optional[str] = None,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        if not federation_rule_id:
            raise WorkloadIdentityError("federation_rule_id must not be empty.")
        if auth_base_url:
            require_https(auth_base_url, field="auth_base_url")
        self._identity_token_provider = identity_token_provider
        self._federation_rule_id = federation_rule_id
        self._resource = resource
        self._auth_base_url = auth_base_url
        self._http_client = http_client

    @property
    def federation_rule_id(self) -> str:
        return self._federation_rule_id

    def _exchange(self, *, api_base_url: str, resource: Optional[str]) -> _Exchange:
        return _Exchange(
            identity_token_provider=self._identity_token_provider,
            federation_rule_id=self._federation_rule_id,
            auth_base_url=resolve_auth_base_url(self._auth_base_url, api_base_url=api_base_url),
            resource=resource,
        )

    def for_client(
        self, *, base_url: str, http_client: Union[httpx.Client, httpx.AsyncClient]
    ) -> Union[AccessTokenProvider, AsyncAccessTokenProvider]:
        """Return the provider a client with `base_url` exchanges through, using that client's HTTP client."""
        exchange = self._exchange(api_base_url=base_url, resource=self._resource or api_origin(base_url))
        if isinstance(http_client, httpx.AsyncClient):
            return _AsyncClientExchange(exchange, http_client)
        if is_async_callable(self._identity_token_provider):
            raise TypeError("`Kernel` cannot await an async `identity_token_provider`; use `AsyncKernel` instead.")
        return _ClientExchange(exchange, http_client)

    def __call__(self, *, force_refresh: bool = False) -> FederationAccessToken:
        del force_refresh
        return self._exchange(api_base_url=api_base_url_from_env(), resource=self._resource).run(self._http_client)


def _one_shot(
    assertion: str, *, federation_rule_id: str, resource: Optional[str], auth_base_url: Optional[str]
) -> _Exchange:
    if not federation_rule_id:
        raise WorkloadIdentityError("federation_rule_id must not be empty.")
    return _Exchange(
        identity_token_provider=lambda: assertion,
        federation_rule_id=federation_rule_id,
        auth_base_url=resolve_auth_base_url(auth_base_url, api_base_url=api_base_url_from_env()),
        resource=resource,
        replay_hint=_ONE_SHOT_REPLAY_HINT,
    )


def exchange_federation_assertion(
    *,
    assertion: str,
    federation_rule_id: str,
    resource: Optional[str] = None,
    auth_base_url: Optional[str] = None,
    http_client: Optional[httpx.Client] = None,
) -> FederationAccessToken:
    """Exchange one identity token for a Kernel access token.

    For callers that already hold the identity token and want the access token
    itself; nothing is cached or refreshed. It needs no Kernel credential.
    `resource` is sent only when given. `auth_base_url` defaults to
    `KERNEL_AUTH_BASE_URL`, then to `https://auth.onkernel.com` unless
    `KERNEL_BASE_URL` points at another deployment.

    Most identity providers' tokens can be exchanged only once, so do not call
    this again with the same assertion, even after a timeout.
    """
    exchange = _one_shot(
        assertion, federation_rule_id=federation_rule_id, resource=resource, auth_base_url=auth_base_url
    )
    return exchange.run(http_client)


async def async_exchange_federation_assertion(
    *,
    assertion: str,
    federation_rule_id: str,
    resource: Optional[str] = None,
    auth_base_url: Optional[str] = None,
    http_client: Optional[httpx.AsyncClient] = None,
) -> FederationAccessToken:
    """Async version of `exchange_federation_assertion`."""
    exchange = _one_shot(
        assertion, federation_rule_id=federation_rule_id, resource=resource, auth_base_url=auth_base_url
    )
    return await exchange.async_run(http_client)
