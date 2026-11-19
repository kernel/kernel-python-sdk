from __future__ import annotations

import asyncio
import logging
import threading
from typing import Any, List, Optional

import pytest

from kernel.lib.credentials import TokenCache, AccessToken, WorkloadIdentityError


class Clock:
    def __init__(self, now: float = 1000.0) -> None:
        self.now = now

    def __call__(self) -> float:
        return self.now


class Provider:
    """Issues `token-1`, `token-2`, ... each living `lifetime` seconds from the clock's current time."""

    def __init__(self, clock: Clock, *, lifetime: Optional[float] = 300.0) -> None:
        self.clock = clock
        self.lifetime = lifetime
        self.calls: List[bool] = []
        self.error: Optional[Exception] = None
        self.called = threading.Event()

    def __call__(self, *, force_refresh: bool = False) -> AccessToken:
        self.calls.append(force_refresh)
        self.called.set()
        if self.error is not None:
            raise self.error
        expires_at = None if self.lifetime is None else self.clock.now + self.lifetime
        return AccessToken(token=f"token-{len(self.calls)}", expires_at=expires_at)


def wait_for(cache: TokenCache, token: str) -> None:
    for _ in range(500):
        if cache.cached_token() == token and cache._flight is None:
            return
        threading.Event().wait(0.01)
    raise AssertionError(f"cache never held {token}; it holds {cache.cached_token()}")


def wait_for_advisory_to_end(cache: TokenCache) -> None:
    for _ in range(500):
        if cache._flight is None:
            return
        threading.Event().wait(0.01)
    raise AssertionError("advisory refresh never finished")


class TestThresholds:
    @pytest.mark.parametrize(
        "lifetime, advisory",
        [
            (600.0, 120.0),
            (300.0, 120.0),
            # Below 300 s the threshold is 40% of the lifetime.
            (100.0, 40.0),
            (10.0, 4.0),
            (1.0, 0.4),
        ],
    )
    def test_advisory_threshold_scales_with_lifetime(self, lifetime: float, advisory: float) -> None:
        clock = Clock()
        provider = Provider(clock, lifetime=lifetime)
        cache = TokenCache(provider, time_source=clock)
        issued_at = clock.now
        assert cache.get_token() == "token-1"

        # Just outside the advisory window: served from cache, no refresh.
        clock.now = issued_at + lifetime - advisory - 0.01
        assert cache.get_token() == "token-1"
        assert len(provider.calls) == 1

        # Inside the advisory window: the cached token is still served, and a refresh starts.
        clock.now = issued_at + lifetime - advisory + 0.01
        assert cache.get_token() == "token-1"
        wait_for(cache, "token-2")
        assert len(provider.calls) == 2

    @pytest.mark.parametrize("lifetime, mandatory", [(600.0, 30.0), (300.0, 30.0), (100.0, 10.0), (1.0, 0.1)])
    def test_mandatory_threshold_scales_with_lifetime(self, lifetime: float, mandatory: float) -> None:
        clock = Clock()
        provider = Provider(clock, lifetime=lifetime)
        cache = TokenCache(provider, time_source=clock)
        issued_at = clock.now
        cache.get_token()

        # Keep the advisory refresh in its backoff, so only the mandatory path can refresh.
        cache._advisory_failed_at = float("inf")
        clock.now = issued_at + lifetime - mandatory - 0.01
        assert cache.get_token() == "token-1"

        clock.now = issued_at + lifetime - mandatory + 0.01
        assert cache.get_token() == "token-2"

    def test_token_without_expiry_is_never_refreshed(self) -> None:
        clock = Clock()
        provider = Provider(clock, lifetime=None)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()
        clock.now += 10 * 365 * 24 * 3600
        assert cache.get_token() == "token-1"
        assert len(provider.calls) == 1

    def test_expired_token_is_replaced(self) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()
        clock.now += 3600
        assert cache.get_token() == "token-2"


class TestAdvisoryRefresh:
    def test_failure_is_swallowed_and_backs_off(self, caplog: pytest.LogCaptureFixture) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        clock.now += 200  # 100 s left: advisory window
        provider.error = RuntimeError("token endpoint is down")
        provider.called.clear()
        with caplog.at_level(logging.WARNING, logger="kernel.lib.credentials._cache"):
            assert cache.get_token() == "token-1"
            assert provider.called.wait(5)
            wait_for_advisory_to_end(cache)
        assert len(provider.calls) == 2
        assert "Background access token refresh failed; still using the cached token: RuntimeError" in caplog.text

        # Within the backoff, requests keep the cached token and do not call the provider.
        clock.now += 4
        assert cache.get_token() == "token-1"
        assert cache.get_token() == "token-1"
        wait_for_advisory_to_end(cache)
        assert len(provider.calls) == 2

        # After the backoff the refresh is tried again.
        clock.now += 2
        provider.error = None
        assert cache.get_token() == "token-1"
        wait_for(cache, "token-3")

    def test_log_does_not_repeat_what_a_callers_provider_raised(self, caplog: pytest.LogCaptureFixture) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        class UpstreamError(Exception):
            pass

        clock.now += 200
        # A provider written by the caller can put anything in its exception, including a credential.
        provider.error = UpstreamError("exchange rejected for token eyJhbGciOiJSUzI1NiJ9.fake-identity-token.sig")
        with caplog.at_level(logging.WARNING, logger="kernel.lib.credentials._cache"):
            assert cache.get_token() == "token-1"
            wait_for_advisory_to_end(cache)

        assert len(provider.calls) == 2
        assert "fake-identity-token" not in caplog.text
        assert "exchange rejected" not in caplog.text
        assert [record.getMessage() for record in caplog.records] == [
            "Background access token refresh failed; still using the cached token: UpstreamError"
        ]

    def test_log_keeps_the_message_of_this_packages_own_error(self, caplog: pytest.LogCaptureFixture) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        clock.now += 200
        provider.error = WorkloadIdentityError(
            "Token exchange failed (HTTP 503): temporarily_unavailable", status_code=503, request_id="req_abc"
        )
        with caplog.at_level(logging.WARNING, logger="kernel.lib.credentials._cache"):
            assert cache.get_token() == "token-1"
            wait_for_advisory_to_end(cache)

        # These messages are written by the SDK without credentials, and say what to look up.
        assert [record.getMessage() for record in caplog.records] == [
            "Background access token refresh failed; still using the cached token: "
            "Token exchange failed (HTTP 503): temporarily_unavailable [request_id=req_abc]"
        ]

    def test_only_one_background_refresh_runs(self) -> None:
        clock = Clock()
        release = threading.Event()
        calls: List[int] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            if len(calls) > 1:
                assert release.wait(5)
            return AccessToken(token=f"token-{len(calls)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        cache.get_token()
        clock.now += 200
        for _ in range(20):
            assert cache.get_token() == "token-1"
        release.set()
        wait_for(cache, "token-2")
        assert len(calls) == 2


class TestMandatoryRefresh:
    def test_failure_raises_and_the_next_call_tries_again(self) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        clock.now += 290  # 10 s left: mandatory window
        provider.error = RuntimeError("token endpoint is down")
        with pytest.raises(RuntimeError, match="token endpoint is down"):
            cache.get_token()

        provider.error = None
        assert cache.get_token() == "token-3"

    def test_first_call_failure_raises(self) -> None:
        clock = Clock()
        provider = Provider(clock)
        provider.error = RuntimeError("no identity")
        cache = TokenCache(provider, time_source=clock)
        with pytest.raises(RuntimeError, match="no identity"):
            cache.get_token()
        assert cache.cached_token() is None


class TestSingleFlight:
    def test_sync_callers_share_one_provider_call(self) -> None:
        clock = Clock()
        entered = threading.Event()
        release = threading.Event()
        calls: List[int] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            entered.set()
            assert release.wait(5)
            return AccessToken(token="token-1", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        results: List[str] = []
        threads = [threading.Thread(target=lambda: results.append(cache.get_token())) for _ in range(16)]
        for thread in threads:
            thread.start()
        assert entered.wait(5)
        release.set()
        for thread in threads:
            thread.join(5)

        assert results == ["token-1"] * 16
        assert len(calls) == 1

    async def test_async_callers_share_one_provider_call(self) -> None:
        clock = Clock()
        release = asyncio.Event()
        calls: List[int] = []

        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            await release.wait()
            return AccessToken(token="token-1", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        tasks = [asyncio.ensure_future(cache.async_get_token()) for _ in range(16)]
        await asyncio.sleep(0.01)
        release.set()

        assert await asyncio.gather(*tasks) == ["token-1"] * 16
        assert len(calls) == 1

    def test_sync_waiters_share_a_failed_call(self) -> None:
        clock = Clock()
        entered = threading.Event()
        release = threading.Event()
        calls: List[int] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            entered.set()
            assert release.wait(5)
            if len(calls) == 1:
                raise RuntimeError("token endpoint is down")
            return AccessToken(token=f"token-{len(calls)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        results: List[str] = []

        def call() -> None:
            try:
                results.append(cache.get_token())
            except RuntimeError as err:
                results.append(str(err))

        # Count the callers that have decided what to do, to release the provider once all 8 are in.
        decided: List[int] = []
        next_step = cache._next_step

        def counting_next_step(new_event: Any) -> Any:
            step = next_step(new_event)
            decided.append(1)
            return step

        cache._next_step = counting_next_step  # type: ignore[method-assign]
        threads = [threading.Thread(target=call) for _ in range(8)]
        for thread in threads:
            thread.start()
        assert entered.wait(5)
        for _ in range(500):
            if len(decided) == 8:
                break
            threading.Event().wait(0.01)
        release.set()
        for thread in threads:
            thread.join(5)

        # Every caller that was waiting gets the one failure; none of them tries again in turn.
        assert results == ["token endpoint is down"] * 8
        assert len(calls) == 1
        # A later call is a new attempt.
        assert cache.get_token() == "token-2"

    async def test_async_waiters_share_a_failed_call(self) -> None:
        clock = Clock()
        calls: List[int] = []

        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            await asyncio.sleep(0.01)
            if len(calls) == 1:
                raise RuntimeError("token endpoint is down")
            return AccessToken(token=f"token-{len(calls)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        results = await asyncio.gather(*[cache.async_get_token() for _ in range(8)], return_exceptions=True)

        assert [str(result) for result in results] == ["token endpoint is down"] * 8
        assert len(calls) == 1
        assert await cache.async_get_token() == "token-2"

    async def test_async_waiters_start_over_when_the_caller_fetching_is_cancelled(self) -> None:
        clock = Clock()
        started = asyncio.Event()
        calls: List[int] = []

        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            started.set()
            await asyncio.sleep(0.05 if len(calls) > 1 else 3600)
            return AccessToken(token=f"token-{len(calls)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        leader = asyncio.ensure_future(cache.async_get_token())
        await started.wait()
        waiters = [asyncio.ensure_future(cache.async_get_token()) for _ in range(3)]
        await asyncio.sleep(0)
        leader.cancel()

        # The cancellation belongs to the first caller only; the others fetch for themselves, once.
        assert await asyncio.gather(*waiters) == ["token-2"] * 3
        assert leader.cancelled()
        assert len(calls) == 2


class TestAsync:
    async def test_advisory_refresh_runs_in_the_background(self) -> None:
        clock = Clock()
        release = asyncio.Event()
        calls: List[int] = []

        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            if len(calls) > 1:
                await release.wait()
            return AccessToken(token=f"token-{len(calls)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        assert await cache.async_get_token() == "token-1"

        clock.now += 200
        # Returns the cached token although the refresh it started is still blocked.
        assert await cache.async_get_token() == "token-1"
        assert await cache.async_get_token() == "token-1"
        release.set()
        await asyncio.gather(*cache._background_tasks)
        assert await cache.async_get_token() == "token-2"
        assert len(calls) == 2

    async def test_advisory_failure_is_swallowed(self, caplog: pytest.LogCaptureFixture) -> None:
        clock = Clock()
        calls: List[int] = []

        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            if len(calls) > 1:
                raise RuntimeError("token endpoint is down")
            return AccessToken(token="token-1", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        await cache.async_get_token()
        clock.now += 200
        with caplog.at_level(logging.WARNING, logger="kernel.lib.credentials._cache"):
            assert await cache.async_get_token() == "token-1"
            await asyncio.gather(*cache._background_tasks)
        assert "still using the cached token: RuntimeError" in caplog.text
        assert await cache.async_get_token() == "token-1"
        assert len(calls) == 2

    async def test_advisory_refresh_is_awaited_where_tasks_cannot_be_detached(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Under trio there is no detached task, so the caller waits for the refresh instead.
        monkeypatch.setattr("kernel.lib.credentials._cache.get_async_library", lambda: "trio")
        clock = Clock()
        calls: List[int] = []

        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            calls.append(1)
            if len(calls) == 3:
                raise RuntimeError("token endpoint is down")
            return AccessToken(token=f"token-{len(calls)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        assert await cache.async_get_token() == "token-1"
        clock.now += 200
        assert await cache.async_get_token() == "token-2"
        assert not cache._background_tasks

        # A failed refresh still leaves the caller the cached token.
        clock.now += 200
        assert await cache.async_get_token() == "token-2"
        assert len(calls) == 3

    async def test_sync_provider_runs_off_the_event_loop(self) -> None:
        loop_thread = threading.get_ident()
        provider_threads: List[int] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            provider_threads.append(threading.get_ident())
            return AccessToken(token="token-1", expires_at=None)

        cache = TokenCache(provider)
        assert await cache.async_get_token() == "token-1"
        assert provider_threads and provider_threads[0] != loop_thread

    def test_get_token_rejects_an_async_provider(self) -> None:
        async def provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            return AccessToken(token="token-1")

        with pytest.raises(RuntimeError, match="async_get_token"):
            TokenCache(provider).get_token()


class TestInvalidate:
    def test_forces_the_next_call_to_fetch_with_force_refresh(self) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        cache.invalidate()
        assert cache.cached_token() is None
        assert cache.get_token() == "token-2"
        assert cache.get_token() == "token-2"
        cache.invalidate()
        cache.get_token()
        # force_refresh is passed only for the call that follows an invalidate().
        assert provider.calls == [False, True, True]
        clock.now += 3600
        cache.get_token()
        assert provider.calls == [False, True, True, False]

    def test_call_that_started_before_an_invalidation_is_not_cached(self) -> None:
        clock = Clock()
        entered = threading.Event()
        release = threading.Event()
        forced: List[bool] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            forced.append(force_refresh)
            if len(forced) == 2:
                entered.set()
                assert release.wait(5)
            return AccessToken(token=f"token-{len(forced)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        cache.get_token()
        clock.now += 200
        assert cache.get_token() == "token-1"  # starts the background refresh, which blocks
        assert entered.wait(5)

        cache.invalidate()
        release.set()

        # The background call began before the invalidation, so its token is
        # discarded and the next caller gets one fetched with force_refresh=True.
        assert cache.get_token() == "token-3"
        assert forced == [False, False, True]

    def test_waiter_does_not_inherit_the_failure_of_a_call_from_before_the_invalidation(self) -> None:
        clock = Clock()
        entered = threading.Event()
        release = threading.Event()
        forced: List[bool] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            forced.append(force_refresh)
            if len(forced) == 2:
                entered.set()
                assert release.wait(5)
                raise RuntimeError("token endpoint is down")
            return AccessToken(token=f"token-{len(forced)}", expires_at=clock.now + 300)

        cache = TokenCache(provider, time_source=clock)
        cache.get_token()
        clock.now += 200
        cache.get_token()  # starts the background refresh, which blocks and will fail
        assert entered.wait(5)
        cache.invalidate()

        results: List[str] = []
        waiter = threading.Thread(target=lambda: results.append(cache.get_token()))
        waiter.start()
        threading.Event().wait(0.05)
        release.set()
        waiter.join(5)

        # The caller came after the invalidation, so it is owed a forced call of its own.
        assert results == ["token-3"]
        assert forced == [False, False, True]


class TestReject:
    def test_drops_only_the_rejected_token(self) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        assert cache.reject("token-1") is True
        assert cache.get_token() == "token-2"
        # A late 401 for the old token must not discard the token that replaced it.
        assert cache.reject("token-1") is True
        assert cache.get_token() == "token-2"
        assert provider.calls == [False, True]

    def test_ignores_a_token_it_did_not_issue(self) -> None:
        clock = Clock()
        provider = Provider(clock)
        cache = TokenCache(provider, time_source=clock)
        cache.get_token()

        assert cache.reject("callers-own-token") is False
        assert cache.cached_token() == "token-1"


class TestProviderContract:
    def test_provider_without_force_refresh_argument(self) -> None:
        cache = TokenCache(lambda: AccessToken(token="plain"))  # type: ignore[arg-type]
        assert cache.get_token() == "plain"
        cache.invalidate()
        assert cache.get_token() == "plain"

    def test_provider_returning_the_wrong_type(self) -> None:
        cache = TokenCache(lambda: "not-an-access-token")  # type: ignore[arg-type, return-value]
        with pytest.raises(TypeError, match="instead of an AccessToken"):
            cache.get_token()

    def test_access_token_repr_masks_the_token(self) -> None:
        token = AccessToken(token="super-secret-access-token", expires_at=12.0)
        assert "super-secret" not in repr(token)
        assert repr(token) == "AccessToken(token='...oken', expires_at=12.0)"
        assert repr(AccessToken(token="short")) == "AccessToken(token='**********', expires_at=None)"
