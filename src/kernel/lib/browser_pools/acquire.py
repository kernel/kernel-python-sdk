from __future__ import annotations

from typing import TYPE_CHECKING, Union
from dataclasses import dataclass
from typing_extensions import TypeAlias

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._exceptions import NotFoundError
from ...types.browser_pool_acquire_response import BrowserPoolAcquireResponse

if TYPE_CHECKING:
    from ..._client import Kernel, AsyncKernel


@dataclass
class Acquired:
    """A browser was leased from the pool."""

    browser: BrowserPoolAcquireResponse


@dataclass
class TimedOut:
    """The long poll expired before a browser became available. Retry to keep waiting."""


@dataclass
class PoolNotFound:
    """No pool exists with the given id or name."""


AcquireResult: TypeAlias = Union[Acquired, TimedOut, PoolNotFound]


def acquire(
    client: "Kernel",
    id_or_name: str,
    *,
    acquire_timeout_seconds: Union[int, Omit] = omit,
    extra_headers: Union[Headers, None] = None,
    extra_query: Union[Query, None] = None,
    extra_body: Union[Body, None] = None,
    timeout: Union[float, httpx.Timeout, None, NotGiven] = not_given,
) -> AcquireResult:
    """Long-polling acquire that surfaces the HTTP outcome as a typed result.

    Returns one of:

    * :class:`Acquired` — a browser was leased from the pool.
    * :class:`TimedOut` — the long poll expired without a browser becoming available.
      Retry to keep waiting.
    * :class:`PoolNotFound` — no pool exists with the given id or name.

    Other API errors (auth, server errors, etc.) still raise.
    """
    try:
        raw = client.browser_pools.with_raw_response.acquire(
            id_or_name,
            acquire_timeout_seconds=acquire_timeout_seconds,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
    except NotFoundError:
        return PoolNotFound()
    if raw.http_response.status_code == 204:
        return TimedOut()
    return Acquired(browser=raw.parse())


async def acquire_async(
    client: "AsyncKernel",
    id_or_name: str,
    *,
    acquire_timeout_seconds: Union[int, Omit] = omit,
    extra_headers: Union[Headers, None] = None,
    extra_query: Union[Query, None] = None,
    extra_body: Union[Body, None] = None,
    timeout: Union[float, httpx.Timeout, None, NotGiven] = not_given,
) -> AcquireResult:
    """Async variant of :func:`acquire`."""
    try:
        raw = await client.browser_pools.with_raw_response.acquire(
            id_or_name,
            acquire_timeout_seconds=acquire_timeout_seconds,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
    except NotFoundError:
        return PoolNotFound()
    if raw.http_response.status_code == 204:
        return TimedOut()
    return Acquired(browser=raw.parse())
