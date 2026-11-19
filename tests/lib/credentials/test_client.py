from __future__ import annotations

import asyncio
import logging
import threading
from typing import Any, List, Iterator, Optional
from pathlib import Path

import httpx
import respx
import pytest
import time_machine

from kernel import (
    Kernel,
    AccessToken,
    AsyncKernel,
    KernelError,
    AuthenticationError,
    StaticIdentityToken,
    WorkloadIdentityError,
    WorkloadIdentityCredentials,
)
from kernel.resources.credentials import CredentialsResource

from .utils import (
    API_URL,
    RULE_ID,
    AUTH_URL,
    TOKEN_URL,
    GITHUB_JWT,
    GOOGLE_JWT,
    KUBERNETES_JWT,
    TokenEndpoint,
    form,
    bearer,
    bearers,
    token_response,
    counting_identity_tokens,
)

GITHUB_REQUEST_URL = (
    "https://run-actions-1-azure-eastus.actions.githubusercontent.com/93//idtoken/abc/def?api-version=2.0"
)
PROFILES_URL = f"{API_URL}/profiles"


def _skip_retry_sleep(_self: object, **_kwargs: object) -> None:
    return None


async def _skip_async_retry_sleep(_self: object, **_kwargs: object) -> None:
    return None


@pytest.fixture(autouse=True)
def no_retry_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(Kernel, "_sleep_for_retry", _skip_retry_sleep)
    monkeypatch.setattr(AsyncKernel, "_sleep_for_retry", _skip_async_retry_sleep)


@pytest.fixture
def token_endpoint(respx_mock: respx.MockRouter) -> TokenEndpoint:
    endpoint = TokenEndpoint()
    respx_mock.post(TOKEN_URL).mock(side_effect=endpoint)
    return endpoint


@pytest.fixture
def profiles(respx_mock: respx.MockRouter) -> respx.Route:
    return respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(200, json=[]))


@pytest.fixture
def frozen_time() -> Iterator[time_machine.Coordinates]:
    with time_machine.travel(1_795_000_000, tick=False) as traveller:
        yield traveller


def workload_credentials(**kwargs: Any) -> WorkloadIdentityCredentials:
    kwargs.setdefault("identity_token_provider", counting_identity_tokens())
    kwargs.setdefault("federation_rule_id", RULE_ID)
    return WorkloadIdentityCredentials(**kwargs)


def list_profiles(client: Kernel) -> httpx.Response:
    return client.get("/profiles", cast_to=httpx.Response)


async def async_list_profiles(client: AsyncKernel) -> httpx.Response:
    return await client.get("/profiles", cast_to=httpx.Response)


class TestConstructor:
    def test_credentials_and_api_key_are_mutually_exclusive(self) -> None:
        with pytest.raises(ValueError, match="mutually exclusive"):
            Kernel(api_key="sk-123", credentials=workload_credentials())
        with pytest.raises(ValueError, match="mutually exclusive"):
            AsyncKernel(api_key="sk-123", credentials=workload_credentials())

    def test_missing_everything_keeps_the_api_key_error_and_mentions_federation(self) -> None:
        for client_class in (Kernel, AsyncKernel):
            with pytest.raises(KernelError) as exc_info:
                client_class()
            message = str(exc_info.value)
            assert message.startswith("The api_key client option must be set")
            assert "KERNEL_API_KEY" in message
            assert "KERNEL_FEDERATION_RULE_ID" in message

    def test_credentials_client_has_no_api_key(self) -> None:
        client = Kernel(credentials=workload_credentials())
        assert client.api_key is None

    def test_credentials_resource_is_still_reachable(self) -> None:
        # `credentials=` is a constructor option; `client.credentials` stays the API resource.
        client = Kernel(credentials=workload_credentials())
        assert isinstance(client.credentials, CredentialsResource)

    def test_sync_client_rejects_async_providers(self) -> None:
        async def access_tokens(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            return AccessToken(token="token")

        async def identity_tokens() -> str:
            return GITHUB_JWT

        with pytest.raises(TypeError, match="use `AsyncKernel` instead"):
            Kernel(credentials=access_tokens)  # type: ignore[arg-type]
        with pytest.raises(TypeError, match="use `AsyncKernel` instead"):
            Kernel(credentials=workload_credentials(identity_token_provider=identity_tokens))


class TestRequests:
    def test_requests_carry_the_exchanged_token(self, token_endpoint: TokenEndpoint, profiles: respx.Route) -> None:
        client = Kernel(credentials=workload_credentials())

        list_profiles(client)
        list_profiles(client)

        # One exchange, reused for both requests.
        assert token_endpoint.assertions == ["identity-token-1"]
        assert bearers(profiles) == ["Bearer access-token-1"] * 2

    def test_nothing_is_exchanged_until_the_first_request(self, token_endpoint: TokenEndpoint) -> None:
        Kernel(credentials=workload_credentials())
        assert token_endpoint.assertions == []

    def test_resource_defaults_to_the_api_origin(self, respx_mock: respx.MockRouter) -> None:
        token_route = respx_mock.post("https://auth.other.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )
        api = respx_mock.get("https://api.other.example/profiles").mock(return_value=httpx.Response(200, json=[]))
        client = Kernel(
            base_url="https://api.other.example/",
            credentials=workload_credentials(auth_base_url="https://auth.other.example"),
        )

        list_profiles(client)

        assert dict(form(token_route.calls.last.request))["resource"] == "https://api.other.example"
        assert bearer(api.calls.last.request) == "Bearer access-token-1"

    def test_custom_base_url_without_auth_base_url_fails_at_construction(self, token_endpoint: TokenEndpoint) -> None:
        with pytest.raises(WorkloadIdentityError, match="auth base URL cannot be inferred"):
            Kernel(base_url="https://api.other.example", credentials=workload_credentials())
        with pytest.raises(WorkloadIdentityError, match="auth base URL cannot be inferred"):
            Kernel(environment="development", credentials=workload_credentials())
        assert token_endpoint.assertions == []

    def test_auth_base_url_from_env(self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("KERNEL_BASE_URL", "https://api.other.example")
        monkeypatch.setenv("KERNEL_AUTH_BASE_URL", "https://auth.other.example")
        token_route = respx_mock.post("https://auth.other.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )
        respx_mock.get("https://api.other.example/profiles").mock(return_value=httpx.Response(200, json=[]))

        list_profiles(Kernel(credentials=workload_credentials()))

        assert token_route.call_count == 1

    def test_exchange_goes_through_the_clients_http_client(self) -> None:
        seen: List[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(f"{request.method} {request.url}")
            if request.url.host == "auth.onkernel.com":
                return httpx.Response(200, json=token_response())
            return httpx.Response(200, json=[])

        with httpx.Client(transport=httpx.MockTransport(handler)) as http_client:
            list_profiles(Kernel(credentials=workload_credentials(), http_client=http_client))

        assert seen == [f"POST {TOKEN_URL}", f"GET {PROFILES_URL}"]

    def test_exchange_failure_is_raised_as_is(self, respx_mock: respx.MockRouter, profiles: respx.Route) -> None:
        token_route = respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_grant", "error_description": "Credential is invalid, expired, or revoked"}
            )
        )
        client = Kernel(credentials=workload_credentials())
        with pytest.raises(WorkloadIdentityError) as exc_info:
            list_profiles(client)
        assert exc_info.value.error == "invalid_grant"
        # Not retried, and the API is never called without a token.
        assert token_route.call_count == 1
        assert not profiles.called

    def test_custom_access_token_provider(self, profiles: respx.Route) -> None:
        calls: List[bool] = []

        def provider(*, force_refresh: bool = False) -> AccessToken:
            calls.append(force_refresh)
            return AccessToken(token=f"custom-{len(calls)}")

        client = Kernel(credentials=provider)
        list_profiles(client)
        list_profiles(client)
        assert calls == [False]
        assert bearer(profiles.calls.last.request) == "Bearer custom-1"

    def test_concurrent_requests_share_one_exchange(self, respx_mock: respx.MockRouter, profiles: respx.Route) -> None:
        entered = threading.Event()
        release = threading.Event()
        exchanges: List[str] = []

        def slow_exchange(request: httpx.Request) -> httpx.Response:
            exchanges.append(dict(form(request))["assertion"])
            entered.set()
            assert release.wait(5)
            return httpx.Response(200, json=token_response())

        respx_mock.post(TOKEN_URL).mock(side_effect=slow_exchange)
        client = Kernel(credentials=workload_credentials())

        threads = [threading.Thread(target=list_profiles, args=(client,)) for _ in range(8)]
        for thread in threads:
            thread.start()
        assert entered.wait(5)
        release.set()
        for thread in threads:
            thread.join(5)

        assert exchanges == ["identity-token-1"]
        assert bearers(profiles) == ["Bearer access-token-1"] * 8


class TestRefresh:
    def test_refreshes_with_a_fresh_identity_token_before_expiry(
        self, token_endpoint: TokenEndpoint, profiles: respx.Route, frozen_time: time_machine.Coordinates
    ) -> None:
        client = Kernel(credentials=workload_credentials())
        list_profiles(client)

        frozen_time.shift(150)  # 148 s left of 298: still fresh
        list_profiles(client)
        assert token_endpoint.assertions == ["identity-token-1"]

        frozen_time.shift(130)  # 18 s left: must refresh before sending
        list_profiles(client)
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]
        assert bearer(profiles.calls.last.request) == "Bearer access-token-2"

    def test_static_token_fails_clearly_once_the_access_token_expires(
        self, token_endpoint: TokenEndpoint, profiles: respx.Route, frozen_time: time_machine.Coordinates
    ) -> None:
        client = Kernel(credentials=workload_credentials(identity_token_provider=StaticIdentityToken(GITHUB_JWT)))
        list_profiles(client)
        list_profiles(client)

        frozen_time.shift(400)
        with pytest.raises(WorkloadIdentityError) as exc_info:
            list_profiles(client)

        assert "already exchanged once" in str(exc_info.value)
        assert "Every exchange needs a fresh provider token" in str(exc_info.value)
        # The token was sent exactly once.
        assert token_endpoint.assertions == [GITHUB_JWT]
        assert profiles.call_count == 2


class TestUnauthorizedRetry:
    def test_401_is_retried_once_with_a_fresh_assertion(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[httpx.Response(401, json={"message": "revoked"}), httpx.Response(200, json=[])]
        )
        client = Kernel(credentials=workload_credentials())

        assert list_profiles(client).status_code == 200

        # The retry exchanged again, with a new identity token rather than the first one.
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]
        assert bearers(api) == ["Bearer access-token-1", "Bearer access-token-2"]

    def test_second_401_is_raised(self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter) -> None:
        api = respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={"message": "revoked"}))
        client = Kernel(credentials=workload_credentials())

        with pytest.raises(AuthenticationError):
            list_profiles(client)

        assert api.call_count == 2
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]

    def test_401_after_another_failure_still_gets_its_retry(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[httpx.Response(503, json={}), httpx.Response(401, json={}), httpx.Response(200, json=[])]
        )
        client = Kernel(credentials=workload_credentials())

        assert list_profiles(client).status_code == 200

        assert bearers(api) == ["Bearer access-token-1", "Bearer access-token-1", "Bearer access-token-2"]
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]

    def test_only_one_401_retry_per_request(self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter) -> None:
        api = respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={}))
        client = Kernel(credentials=workload_credentials(), max_retries=5)

        with pytest.raises(AuthenticationError):
            list_profiles(client)
        assert api.call_count == 2

        # A new request is entitled to its own retry.
        with pytest.raises(AuthenticationError):
            list_profiles(client)
        assert api.call_count == 4
        assert len(token_endpoint.assertions) == 4

    def test_one_401_retry_even_with_other_failures_in_between(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[
                httpx.Response(401, json={}),
                httpx.Response(503, json={}),
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
            ]
        )
        client = Kernel(credentials=workload_credentials(), max_retries=5)

        with pytest.raises(AuthenticationError):
            list_profiles(client)
        assert api.call_count == 3
        assert len(token_endpoint.assertions) == 2

    def test_request_after_a_retried_one_gets_its_own_retry(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[
                # First request: rejected, then fine with a new token.
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
                # Second request, sent with that new token: a server error, then rejected, then fine.
                httpx.Response(503, json={}),
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
            ]
        )
        client = Kernel(credentials=workload_credentials())

        assert list_profiles(client).status_code == 200
        assert list_profiles(client).status_code == 200

        assert bearers(api) == [
            "Bearer access-token-1",
            "Bearer access-token-2",
            "Bearer access-token-2",
            "Bearer access-token-2",
            "Bearer access-token-3",
        ]
        assert len(token_endpoint.assertions) == 3

    def test_retry_is_not_withheld_because_of_an_earlier_request(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[
                # First request: rejected, then fine with a new token.
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
                # Second request to the same URL: a timeout, then rejected, then fine.
                httpx.ReadTimeout("timed out"),
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
            ]
        )
        client = Kernel(credentials=workload_credentials())

        assert list_profiles(client).status_code == 200
        assert list_profiles(client).status_code == 200

        assert api.call_count == 5
        assert len(token_endpoint.assertions) == 3

    def test_one_401_retry_when_the_token_was_already_refreshed(
        self,
        token_endpoint: TokenEndpoint,
        profiles: respx.Route,
        respx_mock: respx.MockRouter,
        frozen_time: time_machine.Coordinates,
    ) -> None:
        client = Kernel(credentials=workload_credentials())
        sent: List[Optional[str]] = []

        def proxies(request: httpx.Request) -> httpx.Response:
            sent.append(bearer(request))
            if len(sent) == 1:
                # While this request is in flight, its token expires and another request replaces it.
                frozen_time.shift(400)
                list_profiles(client)
            return httpx.Response(401, json={})

        respx_mock.get(f"{API_URL}/proxies").mock(side_effect=proxies)

        # The 401 for token 1 arrives when the cache already holds token 2. The retry uses
        # token 2 and is rejected too; that second 401 is raised, not retried once more.
        with pytest.raises(AuthenticationError):
            client.get("/proxies", cast_to=httpx.Response)

        assert sent == ["Bearer access-token-1", "Bearer access-token-2"]
        assert bearers(profiles) == ["Bearer access-token-2"]
        assert len(token_endpoint.assertions) == 2

    def test_callers_own_bearer_token_is_not_retried(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={}))
        client = Kernel(credentials=workload_credentials())

        with pytest.raises(AuthenticationError):
            client.get(
                "/profiles", cast_to=httpx.Response, options={"headers": {"Authorization": "Bearer callers-own-token"}}
            )

        assert bearers(api) == ["Bearer callers-own-token"]
        # The cache still holds the token it exchanged for; the 401 was not about it.
        assert token_endpoint.assertions == ["identity-token-1"]
        assert client._token_cache is not None and client._token_cache.cached_token() == "access-token-1"

    def test_401_is_retried_with_a_single_retry_allowed(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[httpx.Response(401, json={}), httpx.Response(200, json=[])]
        )
        client = Kernel(credentials=workload_credentials(), max_retries=1)
        assert list_profiles(client).status_code == 200
        assert api.call_count == 2
        assert len(token_endpoint.assertions) == 2

    def test_401_after_the_retry_fails_to_exchange(self, respx_mock: respx.MockRouter) -> None:
        token_route = respx_mock.post(TOKEN_URL).mock(
            side_effect=[
                httpx.Response(200, json=token_response()),
                httpx.Response(
                    400,
                    json={"error": "invalid_grant", "error_description": "Credential is invalid, expired, or revoked"},
                ),
            ]
        )
        api = respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={}))
        client = Kernel(credentials=workload_credentials())

        # The rule was disabled: the 401 leads to a new exchange, and its failure is what the caller sees.
        with pytest.raises(WorkloadIdentityError, match="invalid_grant"):
            list_profiles(client)
        assert token_route.call_count == 2
        assert api.call_count == 1

    def test_unreplayable_body_is_not_retried(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.post(f"{API_URL}/upload").mock(return_value=httpx.Response(401, json={}))
        client = Kernel(credentials=workload_credentials())

        def chunks() -> Iterator[bytes]:
            yield b"data"

        with pytest.raises(AuthenticationError):
            client.post("/upload", content=chunks(), cast_to=httpx.Response)

        assert api.call_count == 1
        # The rejected token is dropped all the same, so the next request exchanges again.
        api.mock(return_value=httpx.Response(200, json={}))
        client.post("/upload", content=b"data", cast_to=httpx.Response)
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]

    def test_api_key_client_does_not_retry_401(self, respx_mock: respx.MockRouter) -> None:
        api = respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={}))
        with pytest.raises(AuthenticationError):
            list_profiles(Kernel(api_key="sk-123"))
        assert api.call_count == 1


class TestCopy:
    def test_copy_shares_the_token_cache(self, token_endpoint: TokenEndpoint, profiles: respx.Route) -> None:
        client = Kernel(credentials=workload_credentials(identity_token_provider=StaticIdentityToken(GITHUB_JWT)))

        list_profiles(client)
        list_profiles(client.with_options(timeout=5))
        list_profiles(client.copy(max_retries=0))

        # A single-use token survives with_options because the copies reuse the first exchange.
        assert token_endpoint.assertions == [GITHUB_JWT]
        assert profiles.call_count == 3

    def test_copy_to_another_base_url_exchanges_separately(self, respx_mock: respx.MockRouter) -> None:
        production = TokenEndpoint()
        respx_mock.post(TOKEN_URL).mock(side_effect=production)
        other_endpoint = TokenEndpoint()
        respx_mock.post("https://auth.other.example/token").mock(side_effect=other_endpoint)
        respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(200, json=[]))
        respx_mock.get("https://api.other.example/profiles").mock(return_value=httpx.Response(200, json=[]))

        client = Kernel(credentials=workload_credentials(auth_base_url=AUTH_URL))
        list_profiles(client)
        with pytest.raises(WorkloadIdentityError, match="auth base URL cannot be inferred"):
            Kernel(credentials=workload_credentials()).copy(base_url="https://api.other.example")

        other = Kernel(
            base_url="https://api.other.example",
            credentials=workload_credentials(auth_base_url="https://auth.other.example"),
        )
        list_profiles(other.copy(base_url="https://api.other.example/"))
        list_profiles(other)
        assert len(production.assertions) == 1
        assert len(other_endpoint.assertions) == 1

    def test_copy_with_api_key_drops_the_credentials(
        self, token_endpoint: TokenEndpoint, profiles: respx.Route
    ) -> None:
        client = Kernel(credentials=workload_credentials())
        copied = client.copy(api_key="sk-123")

        list_profiles(copied)

        assert copied.api_key == "sk-123"
        assert bearer(profiles.calls.last.request) == "Bearer sk-123"
        assert token_endpoint.assertions == []

    @pytest.mark.usefixtures("token_endpoint")
    def test_copy_with_credentials_drops_the_api_key(self, profiles: respx.Route) -> None:
        client = Kernel(api_key="sk-123")
        copied = client.copy(credentials=workload_credentials())

        list_profiles(copied)
        list_profiles(client)

        assert copied.api_key is None
        assert bearers(profiles) == ["Bearer access-token-1", "Bearer sk-123"]

    def test_copy_with_both_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="mutually exclusive"):
            Kernel(api_key="sk-123").copy(api_key="sk-456", credentials=workload_credentials())

    def test_api_key_copy_is_unchanged(self, profiles: respx.Route) -> None:
        client = Kernel(api_key="sk-123")
        list_profiles(client.copy())
        list_profiles(client.copy(api_key="sk-456"))
        assert bearers(profiles) == ["Bearer sk-123", "Bearer sk-456"]


class TestEnvironment:
    @pytest.fixture
    def github_env(self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> respx.Route:
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", GITHUB_REQUEST_URL)
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "github-request-token")
        issued = 0

        def issue(_request: httpx.Request) -> httpx.Response:
            nonlocal issued
            issued += 1
            return httpx.Response(200, json={"value": f"{GITHUB_JWT}.{issued}"})

        return respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(side_effect=issue)

    def test_github_actions_is_detected_with_only_the_rule_id(
        self,
        github_env: respx.Route,
        token_endpoint: TokenEndpoint,
        profiles: respx.Route,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)

        client = Kernel()
        list_profiles(client)

        assert client.api_key is None
        assert github_env.calls.last.request.url.params["audience"] == AUTH_URL
        assert github_env.calls.last.request.headers["Authorization"] == "Bearer github-request-token"
        assert token_endpoint.assertions == [f"{GITHUB_JWT}.1"]
        assert bearer(profiles.calls.last.request) == "Bearer access-token-1"

    def test_github_actions_long_job_requests_a_new_token_for_each_exchange(
        self,
        github_env: respx.Route,
        token_endpoint: TokenEndpoint,
        profiles: respx.Route,
        monkeypatch: pytest.MonkeyPatch,
        frozen_time: time_machine.Coordinates,
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        client = Kernel()
        for _ in range(3):
            list_profiles(client)
            frozen_time.shift(3600)

        assert github_env.call_count == 3
        assert token_endpoint.assertions == [f"{GITHUB_JWT}.1", f"{GITHUB_JWT}.2", f"{GITHUB_JWT}.3"]
        assert profiles.call_count == 3

    def test_api_key_env_wins_over_federation_and_warns_once(
        self,
        token_endpoint: TokenEndpoint,
        profiles: respx.Route,
        monkeypatch: pytest.MonkeyPatch,
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        monkeypatch.setenv("KERNEL_API_KEY", "sk-env")
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)

        with caplog.at_level(logging.WARNING, logger="kernel"):
            client = Kernel()
            Kernel()
            AsyncKernel()
        list_profiles(client)

        assert client.api_key == "sk-env"
        assert bearer(profiles.calls.last.request) == "Bearer sk-env"
        assert token_endpoint.assertions == []
        warnings = [
            record.getMessage() for record in caplog.records if "KERNEL_FEDERATION_RULE_ID" in record.getMessage()
        ]
        assert warnings == [
            "KERNEL_API_KEY and KERNEL_FEDERATION_RULE_ID are both set. Using the API key; "
            "unset KERNEL_API_KEY to use workload identity federation."
        ]

    def test_api_key_env_alone_does_not_warn(
        self, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
    ) -> None:
        monkeypatch.setenv("KERNEL_API_KEY", "sk-env")
        with caplog.at_level(logging.WARNING, logger="kernel"):
            Kernel()
        assert caplog.records == []

    def test_explicit_api_key_wins_over_everything(
        self, token_endpoint: TokenEndpoint, profiles: respx.Route, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("KERNEL_API_KEY", "sk-env")
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)

        list_profiles(Kernel(api_key="sk-explicit"))

        assert bearer(profiles.calls.last.request) == "Bearer sk-explicit"
        assert token_endpoint.assertions == []

    @pytest.mark.usefixtures("token_endpoint")
    def test_explicit_credentials_win_over_the_api_key_env(
        self, profiles: respx.Route, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("KERNEL_API_KEY", "sk-env")

        client = Kernel(credentials=workload_credentials())
        list_profiles(client)

        assert client.api_key is None
        assert bearer(profiles.calls.last.request) == "Bearer access-token-1"

    @pytest.mark.usefixtures("token_endpoint")
    def test_empty_api_key_env_does_not_shadow_federation(
        self, profiles: respx.Route, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # An unset CI secret arrives as an empty string.
        monkeypatch.setenv("KERNEL_API_KEY", "")
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)

        list_profiles(Kernel())

        assert bearer(profiles.calls.last.request) == "Bearer access-token-1"

    @pytest.mark.usefixtures("profiles")
    def test_identity_token_file(
        self, token_endpoint: TokenEndpoint, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        path = tmp_path / "token"
        path.write_text(KUBERNETES_JWT + "\n")
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_FILE", str(path))
        # The file wins over a literal value.
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", "literal-token")

        client = Kernel()
        list_profiles(client)
        path.write_text("rotated-token")
        client._token_cache.invalidate()  # type: ignore[union-attr]
        list_profiles(client)

        assert token_endpoint.assertions == [KUBERNETES_JWT, "rotated-token"]

    def test_unrotated_token_file_after_a_401_says_the_file_must_rotate(
        self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        path = tmp_path / "token"
        path.write_text(GITHUB_JWT)
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_FILE", str(path))
        token_route = respx_mock.post(TOKEN_URL).mock(
            side_effect=[
                httpx.Response(200, json=token_response()),
                httpx.Response(
                    400, json={"error": "invalid_grant", "error_description": "Credential was already used"}
                ),
            ]
        )
        respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={}))

        # The retry after the 401 reads the file again, and it has not been rotated yet.
        with pytest.raises(WorkloadIdentityError) as exc_info:
            list_profiles(Kernel())

        assert token_route.call_count == 2
        message = str(exc_info.value)
        assert f"The file at {path} still held a token that had already been exchanged" in message
        assert "must rotate it before each refresh" in message
        assert "static KERNEL_IDENTITY_TOKEN" not in message

    @pytest.mark.usefixtures("profiles")
    def test_identity_token_value_is_single_use(
        self,
        token_endpoint: TokenEndpoint,
        monkeypatch: pytest.MonkeyPatch,
        frozen_time: time_machine.Coordinates,
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)

        client = Kernel()
        list_profiles(client)
        frozen_time.shift(3600)
        with pytest.raises(WorkloadIdentityError, match="already exchanged once"):
            list_profiles(client)
        assert token_endpoint.assertions == [GITHUB_JWT]

    @pytest.mark.usefixtures("profiles")
    def test_identity_token_value_is_single_use_across_clients(
        self, token_endpoint: TokenEndpoint, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)

        list_profiles(Kernel())
        # A second client resolved from the same variable must not send the token again.
        with pytest.raises(WorkloadIdentityError, match="already exchanged once"):
            list_profiles(Kernel())
        assert token_endpoint.assertions == [GITHUB_JWT]

    @pytest.mark.usefixtures("profiles")
    def test_identity_token_value_with_stray_whitespace_is_the_same_token(
        self, token_endpoint: TokenEndpoint, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)
        list_profiles(Kernel())

        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT + "\n")
        with pytest.raises(WorkloadIdentityError, match="already exchanged once"):
            list_profiles(Kernel())
        assert token_endpoint.assertions == [GITHUB_JWT]

    @pytest.mark.usefixtures("github_env", "profiles")
    def test_explicit_source_overrides_detection(
        self,
        token_endpoint: TokenEndpoint,
        respx_mock: respx.MockRouter,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        path = tmp_path / "token"
        path.write_text("file-token")
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_FILE", str(path))
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", "literal-token")
        metadata = respx_mock.get(url__startswith="http://metadata.google.internal/").mock(
            return_value=httpx.Response(200, text=GOOGLE_JWT)
        )

        for source in ("gcp_metadata", "github_actions", "env", "file", " FILE "):
            monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_SOURCE", source)
            list_profiles(Kernel())

        assert token_endpoint.assertions == [GOOGLE_JWT, f"{GITHUB_JWT}.1", "literal-token", "file-token", "file-token"]
        assert metadata.calls.last.request.url.params["audience"] == AUTH_URL

    def test_aws_sts_source(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from kernel.lib.credentials import AWSSTSIdentityToken

        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_SOURCE", "aws_sts")
        client = Kernel()
        assert isinstance(client._credentials, WorkloadIdentityCredentials)
        assert isinstance(client._credentials._identity_token_provider, AWSSTSIdentityToken)

    @pytest.mark.usefixtures("token_endpoint", "profiles")
    def test_identity_token_audience_env(
        self,
        github_env: respx.Route,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_AUDIENCE", "kernel-prod")
        list_profiles(Kernel())
        assert github_env.calls.last.request.url.params["audience"] == "kernel-prod"

    def test_another_deployment_from_the_environment(
        self, github_env: respx.Route, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_BASE_URL", "https://api.other.example")
        monkeypatch.setenv("KERNEL_AUTH_BASE_URL", "https://auth.other.example")
        token_route = respx_mock.post("https://auth.other.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )
        respx_mock.get("https://api.other.example/profiles").mock(return_value=httpx.Response(200, json=[]))

        list_profiles(Kernel())

        # The identity token audience follows the auth base URL, and the resource follows the API.
        assert github_env.calls.last.request.url.params["audience"] == "https://auth.other.example"
        assert dict(form(token_route.calls.last.request))["resource"] == "https://api.other.example"

    def test_custom_base_url_without_auth_base_url_does_not_use_production(
        self, token_endpoint: TokenEndpoint, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)
        monkeypatch.setenv("KERNEL_BASE_URL", "https://api.other.example")
        with pytest.raises(WorkloadIdentityError, match="KERNEL_AUTH_BASE_URL"):
            Kernel()
        assert token_endpoint.assertions == []

    def test_rule_id_without_a_source(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        with pytest.raises(KernelError, match="no identity token source was found") as exc_info:
            Kernel()
        # Still the missing-API-key error, with why federation did not apply.
        assert str(exc_info.value).startswith(
            "The api_key client option must be set either by passing api_key to the client or by setting the "
            "KERNEL_API_KEY environment variable. Workload identity federation cannot be used instead: "
            "KERNEL_FEDERATION_RULE_ID is set but no identity token source was found."
        )
        assert "id-token: write" not in str(exc_info.value)

        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        with pytest.raises(WorkloadIdentityError, match="permissions: id-token: write"):
            Kernel()

    def test_github_actions_source_without_the_permission(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_SOURCE", "github_actions")
        with pytest.raises(WorkloadIdentityError, match="permissions: id-token: write"):
            Kernel()

    @pytest.mark.parametrize(
        "source, message",
        [
            ("file", "KERNEL_IDENTITY_TOKEN_SOURCE=file needs KERNEL_IDENTITY_TOKEN_FILE"),
            ("env", "KERNEL_IDENTITY_TOKEN_SOURCE=env needs KERNEL_IDENTITY_TOKEN"),
            ("azure", "is not a known identity token source"),
        ],
    )
    def test_misconfigured_source(self, monkeypatch: pytest.MonkeyPatch, source: str, message: str) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_SOURCE", source)
        with pytest.raises(WorkloadIdentityError, match=message):
            Kernel()

    def test_source_without_a_rule_id_is_not_federation(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN", GITHUB_JWT)
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_SOURCE", "env")
        with pytest.raises(KernelError, match="The api_key client option must be set"):
            Kernel()


class TestAsyncClient:
    async def test_requests_carry_the_exchanged_token(
        self, token_endpoint: TokenEndpoint, profiles: respx.Route
    ) -> None:
        client = AsyncKernel(credentials=workload_credentials())

        await async_list_profiles(client)
        await async_list_profiles(client)

        assert token_endpoint.assertions == ["identity-token-1"]
        assert bearers(profiles) == ["Bearer access-token-1"] * 2

    async def test_concurrent_requests_share_one_exchange(
        self, token_endpoint: TokenEndpoint, profiles: respx.Route
    ) -> None:
        client = AsyncKernel(credentials=workload_credentials())

        await asyncio.gather(*[async_list_profiles(client) for _ in range(16)])

        assert token_endpoint.assertions == ["identity-token-1"]
        assert bearers(profiles) == ["Bearer access-token-1"] * 16

    @pytest.mark.usefixtures("profiles")
    async def test_async_identity_token_provider(
        self,
        token_endpoint: TokenEndpoint,
    ) -> None:
        async def identity_tokens() -> str:
            await asyncio.sleep(0)
            return GITHUB_JWT

        client = AsyncKernel(credentials=workload_credentials(identity_token_provider=identity_tokens))
        await async_list_profiles(client)
        assert token_endpoint.assertions == [GITHUB_JWT]

    @pytest.mark.usefixtures("profiles")
    async def test_sync_identity_token_provider_runs_off_the_event_loop(
        self,
        token_endpoint: TokenEndpoint,
    ) -> None:
        loop_thread = threading.get_ident()
        provider_threads: List[int] = []

        def identity_tokens() -> str:
            provider_threads.append(threading.get_ident())
            return GITHUB_JWT

        client = AsyncKernel(credentials=workload_credentials(identity_token_provider=identity_tokens))
        await async_list_profiles(client)
        assert provider_threads and provider_threads[0] != loop_thread
        assert token_endpoint.assertions == [GITHUB_JWT]

    async def test_async_and_sync_access_token_providers(self, profiles: respx.Route) -> None:
        async def async_provider(*, force_refresh: bool = False) -> AccessToken:
            del force_refresh
            return AccessToken(token="from-async-provider")

        def sync_provider() -> AccessToken:
            return AccessToken(token="from-sync-provider")

        await async_list_profiles(AsyncKernel(credentials=async_provider))
        # A provider that takes no `force_refresh` argument is called without one.
        await async_list_profiles(AsyncKernel(credentials=sync_provider))  # type: ignore[arg-type]
        assert bearers(profiles) == [
            "Bearer from-async-provider",
            "Bearer from-sync-provider",
        ]

    async def test_exchange_goes_through_the_clients_http_client(self) -> None:
        seen: List[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(f"{request.method} {request.url}")
            if request.url.host == "auth.onkernel.com":
                return httpx.Response(200, json=token_response())
            return httpx.Response(200, json=[])

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http_client:
            await async_list_profiles(AsyncKernel(credentials=workload_credentials(), http_client=http_client))

        assert seen == [f"POST {TOKEN_URL}", f"GET {PROFILES_URL}"]

    async def test_401_is_retried_once_with_a_fresh_assertion(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[httpx.Response(401, json={}), httpx.Response(200, json=[])]
        )
        client = AsyncKernel(credentials=workload_credentials())

        assert (await async_list_profiles(client)).status_code == 200

        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]
        assert bearers(api) == ["Bearer access-token-1", "Bearer access-token-2"]

    async def test_each_request_gets_one_401_retry(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        api = respx_mock.get(PROFILES_URL).mock(
            side_effect=[
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
                # Same task, same URL: the earlier retry must not count against this request.
                httpx.ReadTimeout("timed out"),
                httpx.Response(401, json={}),
                httpx.Response(200, json=[]),
                # And one request never gets two, whatever happens in between.
                httpx.Response(401, json={}),
                httpx.Response(503, json={}),
                httpx.Response(401, json={}),
            ]
        )
        client = AsyncKernel(credentials=workload_credentials(), max_retries=5)

        assert (await async_list_profiles(client)).status_code == 200
        assert (await async_list_profiles(client)).status_code == 200
        with pytest.raises(AuthenticationError):
            await async_list_profiles(client)

        assert api.call_count == 8
        assert len(token_endpoint.assertions) == 4

    async def test_second_401_is_raised(self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter) -> None:
        api = respx_mock.get(PROFILES_URL).mock(return_value=httpx.Response(401, json={}))
        client = AsyncKernel(credentials=workload_credentials())

        with pytest.raises(AuthenticationError):
            await async_list_profiles(client)

        assert api.call_count == 2
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]

    async def test_concurrent_401s_cause_one_new_exchange(
        self, token_endpoint: TokenEndpoint, respx_mock: respx.MockRouter
    ) -> None:
        def api(request: httpx.Request) -> httpx.Response:
            if bearer(request) == "Bearer access-token-1":
                return httpx.Response(401, json={})
            return httpx.Response(200, json=[])

        respx_mock.get(PROFILES_URL).mock(side_effect=api)
        client = AsyncKernel(credentials=workload_credentials())

        responses = await asyncio.gather(*[async_list_profiles(client) for _ in range(8)])

        assert [response.status_code for response in responses] == [200] * 8
        assert token_endpoint.assertions == ["identity-token-1", "identity-token-2"]

    @pytest.mark.usefixtures("profiles")
    async def test_static_token_fails_clearly_once_the_access_token_expires(
        self, token_endpoint: TokenEndpoint, frozen_time: time_machine.Coordinates
    ) -> None:
        client = AsyncKernel(credentials=workload_credentials(identity_token_provider=StaticIdentityToken(GITHUB_JWT)))
        await async_list_profiles(client)
        await async_list_profiles(client.with_options(timeout=5))

        frozen_time.shift(400)
        with pytest.raises(WorkloadIdentityError, match="already exchanged once"):
            await async_list_profiles(client)
        assert token_endpoint.assertions == [GITHUB_JWT]

    async def test_environment_chain(
        self,
        token_endpoint: TokenEndpoint,
        profiles: respx.Route,
        respx_mock: respx.MockRouter,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("KERNEL_FEDERATION_RULE_ID", RULE_ID)
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", GITHUB_REQUEST_URL)
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "github-request-token")
        github = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )

        client = AsyncKernel()
        await async_list_profiles(client)

        assert github.calls.last.request.url.params["audience"] == AUTH_URL
        assert token_endpoint.assertions == [GITHUB_JWT]
        assert bearer(profiles.calls.last.request) == "Bearer access-token-1"

    async def test_exchange_failure_is_raised_as_is(self, respx_mock: respx.MockRouter, profiles: respx.Route) -> None:
        token_route = respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_grant", "error_description": "Credential was already used"}
            )
        )
        client = AsyncKernel(credentials=workload_credentials())
        with pytest.raises(WorkloadIdentityError, match="Every exchange needs a fresh provider token"):
            await async_list_profiles(client)
        assert token_route.call_count == 1
        assert not profiles.called
