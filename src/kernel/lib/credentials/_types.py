from __future__ import annotations

import inspect
import functools
from typing import Union, Callable, Optional, Protocol, Awaitable
from dataclasses import dataclass
from typing_extensions import TypeGuard, override, runtime_checkable

import httpx

__all__ = [
    "AccessToken",
    "Principal",
    "FederationAccessToken",
    "AccessTokenProvider",
    "AsyncAccessTokenProvider",
    "ClientBoundProvider",
    "IdentityTokenProvider",
    "AsyncIdentityTokenProvider",
]


def _mask(token: object) -> str:
    # str() first: a repr must not raise, even for a malformed token.
    text = str(token)
    return f"...{text[-4:]}" if len(text) >= 12 else "**********"


@dataclass(frozen=True, repr=False)
class AccessToken:
    """A Kernel access token and when it expires.

    `expires_at` is unix seconds. `None` means the token does not expire, so
    `TokenCache` never refreshes it. `repr()` masks the token.
    """

    token: str
    expires_at: Optional[float] = None

    @override
    def __repr__(self) -> str:
        return f"{type(self).__name__}(token='{_mask(self.token)}', expires_at={self.expires_at!r})"


@dataclass(frozen=True)
class Principal:
    """The identity an access token was issued to, such as a service account."""

    type: str
    id: str


@dataclass(frozen=True, repr=False)
class FederationAccessToken(AccessToken):
    """An access token from a workload identity exchange, with what the token endpoint reported about it."""

    scope: Optional[str] = None
    project_id: Optional[str] = None
    principal: Optional[Principal] = None
    federation_rule_id: Optional[str] = None

    @override
    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(token='{_mask(self.token)}', expires_at={self.expires_at!r}, "
            f"scope={self.scope!r}, project_id={self.project_id!r}, principal={self.principal!r}, "
            f"federation_rule_id={self.federation_rule_id!r})"
        )


class AccessTokenProvider(Protocol):
    """Callable that returns a new access token.

    Calling the provider is the refresh mechanism; caching is done by
    `TokenCache`. `force_refresh` is true for the first call after a 401, so a
    provider that keeps its own cache must bypass it. A provider that takes no
    `force_refresh` argument is called without one.
    """

    def __call__(self, *, force_refresh: bool = False) -> AccessToken: ...


class AsyncAccessTokenProvider(Protocol):
    """Async version of `AccessTokenProvider`, for `AsyncKernel`."""

    async def __call__(self, *, force_refresh: bool = False) -> AccessToken: ...


# Returns the workload's own identity token (a JWT from its identity provider).
# It is called once per exchange and must return a new token each time, because
# most providers' tokens can be exchanged only once.
IdentityTokenProvider = Callable[[], str]
AsyncIdentityTokenProvider = Callable[[], Awaitable[str]]


@runtime_checkable
class ClientBoundProvider(Protocol):
    """A provider that exchanges tokens through the client it is given to.

    The client calls `for_client` once at construction with its own base URL
    and HTTP client, and uses the provider that is returned. Other providers
    are used as they are.
    """

    def for_client(
        self, *, base_url: str, http_client: Union[httpx.Client, httpx.AsyncClient]
    ) -> Union[AccessTokenProvider, AsyncAccessTokenProvider]: ...


def is_async_callable(obj: object) -> TypeGuard[Callable[..., Awaitable[object]]]:
    """True for an `async def` function, an object whose `__call__` is one, or a `functools.partial` of either."""
    while isinstance(obj, functools.partial):
        obj = obj.func
    return inspect.iscoroutinefunction(obj) or inspect.iscoroutinefunction(getattr(obj, "__call__", None))  # noqa: B004
