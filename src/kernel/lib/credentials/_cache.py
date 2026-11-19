from __future__ import annotations

import time
import asyncio
import inspect
import logging
import threading
from typing import Set, Union, Callable, Optional, Awaitable, NamedTuple, cast
from collections import OrderedDict
from dataclasses import dataclass

import anyio

from ._types import AccessToken, AccessTokenProvider, AsyncAccessTokenProvider, is_async_callable
from ._errors import WorkloadIdentityError
from ..._utils import asyncify, get_async_library
from ._constants import (
    ADVISORY_REFRESH_SECONDS,
    ADVISORY_REFRESH_FRACTION,
    MANDATORY_REFRESH_SECONDS,
    MANDATORY_REFRESH_FRACTION,
    ADVISORY_REFRESH_BACKOFF_SECONDS,
)

__all__ = ["TokenCache"]

log: logging.Logger = logging.getLogger(__name__)

_Event = Union[threading.Event, anyio.Event]

# How many issued tokens are remembered, to tell a rejected token of this
# cache from a bearer token the caller supplied.
_ISSUED_TOKENS_KEPT = 4


def _valid_access_token(value: object) -> AccessToken:
    if inspect.iscoroutine(value):
        # Closing it stops Python warning that the coroutine was never awaited.
        value.close()
        raise TypeError(
            "The credentials provider returned a coroutine instead of an AccessToken; pass the `async def` function itself."
        )
    if not isinstance(value, AccessToken):
        raise TypeError(f"The credentials provider returned {type(value).__name__} instead of an AccessToken.")
    return value


def _accepts_force_refresh(provider: Callable[..., object]) -> bool:
    try:
        parameters = inspect.signature(provider).parameters.values()
    except (TypeError, ValueError):
        # No signature to inspect, as for some C callables. Assume the documented contract.
        return True
    return any(
        parameter.name == "force_refresh" or parameter.kind is inspect.Parameter.VAR_KEYWORD for parameter in parameters
    )


def _loggable(error: Exception) -> str:
    """What the log may say about a failed provider call.

    This package's own errors are written without credentials and carry the
    request ID. Anything else was raised by a caller's provider and its text
    could quote a token, so only its type is logged.
    """
    return str(error) if isinstance(error, WorkloadIdentityError) else type(error).__name__


@dataclass(frozen=True)
class _Entry:
    token: str
    advisory_at: float
    """When the advisory refresh window starts. Infinite for a token that never expires."""
    mandatory_at: float


class _Flight:
    """One provider call in progress. Every caller that needs its result waits on `done`."""

    def __init__(self, done: _Event, *, force: bool, generation: int, advisory: bool) -> None:
        self.done = done
        self.force = force
        """Whether the provider is called with `force_refresh=True`."""
        self.generation = generation
        """The cache's invalidation count when the call started."""
        self.advisory = advisory
        self.token: Optional[str] = None
        """The new token, once it is in the cache."""
        self.error: Optional[Exception] = None
        """Why the call failed. If both this and `token` stay `None`, the call
        was cancelled or overtaken by an invalidation."""


class _Step(NamedTuple):
    """What a caller does next: serve `token`, and/or deal with `flight`.

    With a token, a flight is an advisory refresh this caller has to start.
    Without one, the caller makes the provider call itself if `lead`, and
    otherwise waits for the flight another caller is making.
    """

    token: Optional[str]
    flight: Optional[_Flight]
    lead: bool = False


class TokenCache:
    """Caches the access token from an `AccessTokenProvider` and refreshes it before it expires.

    On each `get_token` (or `async_get_token`) call:

    * No cached token: call the provider, cache the result and return it.
    * The cached token has no expiry: return it.
    * Otherwise, by time remaining until expiry:

      - above the advisory threshold: return the cached token;
      - below the advisory threshold, min(120 s, 40% of the token's lifetime):
        return the cached token and refresh in the background. A failed
        background refresh is logged and not retried for a few seconds;
      - below the mandatory threshold, min(30 s, 10% of the lifetime), or
        expired: call the provider and return the new token. A failure raises.

    One provider call runs at a time. Callers that need a new token while one
    is being fetched wait for that call and share its outcome, the token or
    the error, instead of each making their own. A call that began before an
    invalidation does not count: its token is not cached and its waiters go on
    to a new call.

    A cache is used either from sync code or from async code, matching its
    client. With an async provider only `async_get_token` works.
    """

    def __init__(
        self,
        provider: Union[AccessTokenProvider, AsyncAccessTokenProvider],
        *,
        time_source: Callable[[], float] = time.time,
    ) -> None:
        self._provider = provider
        self._is_async_provider = is_async_callable(provider)
        self._accepts_force_refresh = _accepts_force_refresh(provider)
        self._time_source = time_source

        # Guards the fields below. Never held across a provider call.
        self._lock = threading.Lock()
        self._cached: Optional[_Entry] = None
        self._flight: Optional[_Flight] = None
        # Counts invalidations. A provider call that started before the latest
        # one does not get to cache its result.
        self._generation = 0
        # Set by an invalidation: the next provider call passes force_refresh=True.
        self._next_force = False
        self._advisory_failed_at = float("-inf")
        # The most recently issued tokens.
        self._issued: "OrderedDict[str, None]" = OrderedDict()
        # asyncio keeps only weak references to tasks, so running ones are held here.
        self._background_tasks: Set["asyncio.Task[None]"] = set()

    def cached_token(self) -> Optional[str]:
        """The token currently cached, without refreshing it. `None` when nothing is cached."""
        with self._lock:
            return self._cached.token if self._cached is not None else None

    def invalidate(self) -> None:
        """Drop the cached token, so the next call fetches a new one with `force_refresh=True`."""
        with self._lock:
            self._invalidate_locked()

    def reject(self, token: str) -> bool:
        """Record that the API rejected `token`, dropping it if it is still the cached one.

        Returns whether this cache issued the token. If the cache has already
        moved on to a newer token, that one is kept, so requests that fail
        together cause a single new provider call.
        """
        with self._lock:
            if token not in self._issued:
                return False
            if self._cached is not None and self._cached.token == token:
                self._invalidate_locked()
            return True

    def _invalidate_locked(self) -> None:
        self._cached = None
        self._generation += 1
        self._next_force = True

    def get_token(self) -> str:
        """Return a valid access token, calling the provider if needed."""
        if self._is_async_provider:
            raise RuntimeError("This TokenCache wraps an async provider; use `async_get_token()`.")
        while True:
            step = self._next_step(threading.Event)
            flight = step.flight
            if step.token is not None:
                if flight is not None:
                    self._start_background_flight(flight)
                return step.token
            assert flight is not None
            if step.lead:
                self._fly(flight)
                if flight.token is not None:
                    return flight.token
            else:
                cast(threading.Event, flight.done).wait()
                self._raise_shared_failure(flight)
            # Go again: to read the token a waiter was waiting for, or because
            # the call was cancelled or overtaken by an invalidation.

    async def async_get_token(self) -> str:
        """Async version of `get_token`. A sync provider is run in a worker thread."""
        while True:
            step = self._next_step(anyio.Event)
            flight = step.flight
            if step.token is not None:
                if flight is None or self._start_background_task(flight):
                    return step.token
                # No detached tasks on this async library (trio), so this caller
                # makes the advisory call itself. A failure leaves the cached token.
                try:
                    await self._async_fly(flight)
                except Exception:
                    pass
                continue
            assert flight is not None
            if step.lead:
                await self._async_fly(flight)
                if flight.token is not None:
                    return flight.token
            else:
                await cast(anyio.Event, flight.done).wait()
                self._raise_shared_failure(flight)

    def _raise_shared_failure(self, flight: _Flight) -> None:
        """Raise the failure of a call this caller waited on, unless an invalidation has overtaken that call."""
        if flight.error is None:
            return
        with self._lock:
            overtaken = flight.generation != self._generation
        if not overtaken:
            raise flight.error

    def _next_step(self, new_event: Callable[[], _Event]) -> _Step:
        with self._lock:
            entry = self._cached
            now = self._time_source()
            if entry is not None and now < entry.mandatory_at:
                if (
                    now < entry.advisory_at
                    or self._flight is not None
                    or now - self._advisory_failed_at < ADVISORY_REFRESH_BACKOFF_SECONDS
                ):
                    return _Step(entry.token, None)
                return _Step(entry.token, self._new_flight_locked(new_event(), advisory=True))
            if self._flight is not None:
                return _Step(None, self._flight)
            return _Step(None, self._new_flight_locked(new_event(), advisory=False), lead=True)

    def _new_flight_locked(self, done: _Event, *, advisory: bool) -> _Flight:
        self._flight = _Flight(done, force=self._next_force, generation=self._generation, advisory=advisory)
        return self._flight

    def _land(self, flight: _Flight, fresh: Optional[AccessToken], error: Optional[BaseException]) -> None:
        """Record how a provider call ended and release everyone waiting on it."""
        if isinstance(error, Exception) and flight.advisory:
            log.warning("Background access token refresh failed; still using the cached token: %s", _loggable(error))
        with self._lock:
            now = self._time_source()
            if fresh is not None and flight.generation == self._generation:
                self._cached = self._entry(fresh, now)
                self._issued[fresh.token] = None
                while len(self._issued) > _ISSUED_TOKENS_KEPT:
                    self._issued.popitem(last=False)
                # No invalidation happened since this call started, so none is left to act on.
                self._next_force = False
                flight.token = fresh.token
            elif isinstance(error, Exception):
                flight.error = error
                if flight.advisory:
                    self._advisory_failed_at = now
            if self._flight is flight:
                self._flight = None
        flight.done.set()

    @staticmethod
    def _entry(fresh: AccessToken, now: float) -> _Entry:
        if fresh.expires_at is None:
            return _Entry(token=fresh.token, advisory_at=float("inf"), mandatory_at=float("inf"))
        lifetime = max(fresh.expires_at - now, 0.0)
        return _Entry(
            token=fresh.token,
            advisory_at=fresh.expires_at - min(ADVISORY_REFRESH_SECONDS, ADVISORY_REFRESH_FRACTION * lifetime),
            mandatory_at=fresh.expires_at - min(MANDATORY_REFRESH_SECONDS, MANDATORY_REFRESH_FRACTION * lifetime),
        )

    def _call_provider(self, force: bool) -> object:
        provider = cast("Callable[..., object]", self._provider)
        if not self._accepts_force_refresh:
            return provider()
        return provider(force_refresh=force)

    def _fly(self, flight: _Flight) -> None:
        try:
            fresh = _valid_access_token(self._call_provider(flight.force))
        except BaseException as err:
            self._land(flight, None, err)
            raise
        self._land(flight, fresh, None)

    async def _async_fly(self, flight: _Flight) -> None:
        try:
            if self._is_async_provider:
                result = await cast("Awaitable[object]", self._call_provider(flight.force))
            else:
                result = await asyncify(self._call_provider)(flight.force)
            fresh = _valid_access_token(result)
        except BaseException as err:
            # Includes cancellation: nothing here awaits, so a cancelled call still releases its waiters.
            self._land(flight, None, err)
            raise
        self._land(flight, fresh, None)

    def _fly_quietly(self, flight: _Flight) -> None:
        try:
            self._fly(flight)
        except Exception:
            pass  # Logged by _land; the cached token is still good.

    def _start_background_flight(self, flight: _Flight) -> None:
        thread = threading.Thread(target=self._fly_quietly, args=(flight,), name="kernel-token-refresh", daemon=True)
        try:
            thread.start()
        except RuntimeError:
            # Threads cannot be started while the interpreter shuts down. The
            # cached token is still valid, so skip this refresh.
            self._land(flight, None, None)

    async def _async_fly_quietly(self, flight: _Flight) -> None:
        try:
            await self._async_fly(flight)
        except Exception:
            pass

    def _start_background_task(self, flight: _Flight) -> bool:
        """Run an advisory flight as a detached task. False if this async library has none."""
        if get_async_library() != "asyncio":
            return False
        task = asyncio.get_running_loop().create_task(self._async_fly_quietly(flight))
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)
        return True
