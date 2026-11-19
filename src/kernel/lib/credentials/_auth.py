from __future__ import annotations

import os
import inspect
import logging
import functools
import threading
from typing import Any, Dict, Tuple, Union, Mapping, TypeVar, Callable, Iterator, Optional, cast
from contextlib import contextmanager
from contextvars import ContextVar

import httpx

from ._cache import TokenCache
from ._chain import has_federation_env, default_credentials
from ._types import (
    AccessTokenProvider,
    ClientBoundProvider,
    AsyncAccessTokenProvider,
    is_async_callable,
)
from ._errors import WorkloadIdentityError
from ._workload import WorkloadIdentityCredentials
from ._constants import ENV_API_KEY, ENV_FEDERATION_RULE_ID
from ..browser_routing.routing import direct_vm_request_body_is_replayable

__all__ = [
    "TokenCache",
    "AccessTokenProvider",
    "AsyncAccessTokenProvider",
    "MISSING_CREDENTIALS_MESSAGE",
    "resolve_credentials",
    "make_token_cache",
    "token_cache_auth_headers",
    "cached_auth_headers",
    "refresh_token_cache",
    "should_retry_with_fresh_token",
    "with_unauthorized_retry_scope",
    "copy_credentials",
]

log: logging.Logger = logging.getLogger(__name__)

_Provider = Union[AccessTokenProvider, AsyncAccessTokenProvider]
# `Kernel` takes a sync provider, `AsyncKernel` either kind.
_ProviderT = TypeVar("_ProviderT", AccessTokenProvider, _Provider)
_RequestT = TypeVar("_RequestT", bound=Callable[..., Any])

_MISSING_API_KEY_MESSAGE = (
    "The api_key client option must be set either by passing api_key to the client "
    f"or by setting the {ENV_API_KEY} environment variable"
)
MISSING_CREDENTIALS_MESSAGE = (
    f"{_MISSING_API_KEY_MESSAGE}. Alternatively, configure workload identity federation by passing credentials "
    f"to the client or by setting {ENV_FEDERATION_RULE_ID} with an identity token source"
)

_warned_lock = threading.Lock()
_warned_api_key_shadows_federation = False


def _warn_api_key_shadows_federation() -> None:
    global _warned_api_key_shadows_federation
    with _warned_lock:
        if _warned_api_key_shadows_federation:
            return
        _warned_api_key_shadows_federation = True
    log.warning(
        "%s and %s are both set. Using the API key; unset %s to use workload identity federation.",
        ENV_API_KEY,
        ENV_FEDERATION_RULE_ID,
        ENV_API_KEY,
    )


def resolve_credentials(
    *, api_key: Optional[str], credentials: Optional[_ProviderT]
) -> Union[_ProviderT, WorkloadIdentityCredentials, None]:
    """The credentials provider a client should use, or `None` when it authenticates with an API key.

    Precedence: an explicit `api_key=` or `credentials=` argument, then
    `KERNEL_API_KEY`, then workload identity federation from the environment.
    Federation variables that do not add up to a usable source raise the
    missing-API-key error with the reason appended.
    """
    if credentials is not None:
        if api_key is not None:
            raise ValueError("The `api_key` and `credentials` arguments are mutually exclusive")
        return credentials
    if api_key is not None:
        return None
    if os.environ.get(ENV_API_KEY):
        if has_federation_env():
            _warn_api_key_shadows_federation()
        return None
    try:
        return default_credentials()
    except WorkloadIdentityError as err:
        raise WorkloadIdentityError(
            f"{_MISSING_API_KEY_MESSAGE}. Workload identity federation cannot be used instead: {err}"
        ) from None


def make_token_cache(
    credentials: Optional[_Provider],
    *,
    base_url: Union[str, httpx.URL],
    http_client: Union[httpx.Client, httpx.AsyncClient],
    inherited: Optional[TokenCache] = None,
) -> Optional[TokenCache]:
    """The token cache for a client using `credentials`. `inherited` is the cache of the client it was copied from."""
    if credentials is None:
        return None
    if inherited is not None:
        return inherited
    provider = credentials
    if isinstance(provider, ClientBoundProvider):
        provider = provider.for_client(base_url=str(base_url), http_client=http_client)
    if isinstance(http_client, httpx.Client) and is_async_callable(provider):
        raise TypeError("`Kernel` cannot await an async `credentials` provider; use `AsyncKernel` instead.")
    return TokenCache(provider)


def token_cache_auth_headers(token_cache: TokenCache) -> Dict[str, str]:
    """Auth headers for a sync client, refreshing the access token first if it needs it."""
    return {"Authorization": f"Bearer {token_cache.get_token()}"}


def cached_auth_headers(token_cache: TokenCache) -> Dict[str, str]:
    """Auth headers for an async client.

    A property cannot await, so the client awaits `refresh_token_cache` while
    preparing each request, and this reads the token that call left in the cache.
    Before the client's first request there is no token and no header.
    """
    token = token_cache.cached_token()
    return {"Authorization": f"Bearer {token}"} if token is not None else {}


async def refresh_token_cache(token_cache: Optional[TokenCache]) -> None:
    if token_cache is not None:
        await token_cache.async_get_token()


# Whether the request being made in this thread or task has used its one 401
# retry. `None` outside `unauthorized_retry_scope`. The base client's retry loop
# passes nothing from one attempt to the next, so the client's `request()` opens
# a scope around the whole loop and `_should_retry` records the retry in it.
_unauthorized_retry_used: "ContextVar[Optional[bool]]" = ContextVar("kernel_unauthorized_retry_used", default=None)


@contextmanager
def unauthorized_retry_scope() -> Iterator[None]:
    """Covers every attempt of one request, so that it gets at most one retry for a 401."""
    reset_token = _unauthorized_retry_used.set(False)
    try:
        yield
    finally:
        _unauthorized_retry_used.reset(reset_token)


def with_unauthorized_retry_scope(request: _RequestT) -> _RequestT:
    """Wrap a client's `request` method so that each call runs in its own `unauthorized_retry_scope`.

    The wrapper keeps the method's signature, overloads included.
    """
    if inspect.iscoroutinefunction(request):

        @functools.wraps(request)
        async def async_scoped(*args: Any, **kwargs: Any) -> Any:
            with unauthorized_retry_scope():
                return await request(*args, **kwargs)

        return cast(_RequestT, async_scoped)

    @functools.wraps(request)
    def scoped(*args: Any, **kwargs: Any) -> Any:
        with unauthorized_retry_scope():
            return request(*args, **kwargs)

    return cast(_RequestT, scoped)


def should_retry_with_fresh_token(response: httpx.Response, token_cache: Optional[TokenCache]) -> bool:
    """Whether a 401 should be retried with a newly exchanged access token.

    Drops the rejected token from the cache, so the next attempt or request
    exchanges again. Each request gets one such retry, whatever its other
    attempts failed with; after that a 401 is left to the normal retry rules,
    which raise it. A bearer token the cache did not issue, or a body that
    cannot be sent again, is not retried.
    """
    if token_cache is None or response.status_code != 401:
        return False
    scheme, _, sent_token = response.request.headers.get("Authorization", "").partition(" ")
    if scheme != "Bearer" or not sent_token or not token_cache.reject(sent_token):
        return False
    if _unauthorized_retry_used.get() is not False:
        return False
    if not direct_vm_request_body_is_replayable(response.request):
        return False
    _unauthorized_retry_used.set(True)
    return True


def copy_credentials(
    client: Any,
    *,
    api_key: Optional[str],
    credentials: Optional[_Provider],
    base_url: Union[str, httpx.URL, None],
    http_client: Union[httpx.Client, httpx.AsyncClient],
    token_cache: Optional[TokenCache],
    extra_kwargs: Mapping[str, Any],
) -> Tuple[Optional[str], Mapping[str, Any]]:
    """The `api_key` and extra constructor arguments for a copy of `client`.

    An `api_key` or `credentials` passed to `copy()` replaces whichever of the
    two the client uses. Otherwise the copy inherits it, and shares the token
    cache as long as it talks to the same API through the same HTTP client.
    """
    if api_key is not None and credentials is not None:
        raise ValueError("The `api_key` and `credentials` arguments are mutually exclusive")
    if credentials is not None:
        return None, {"credentials": credentials, "_token_cache": token_cache, **extra_kwargs}

    inherited_cache: Optional[TokenCache] = client._token_cache
    if api_key or inherited_cache is None:
        return api_key or client.api_key, extra_kwargs

    same_base_url = base_url is None or str(base_url).rstrip("/") == str(client.base_url).rstrip("/")
    if token_cache is None and same_base_url and http_client is client._client:
        token_cache = inherited_cache
    return None, {"credentials": client._credentials, "_token_cache": token_cache, **extra_kwargs}
