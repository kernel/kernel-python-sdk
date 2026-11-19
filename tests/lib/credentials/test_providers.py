from __future__ import annotations

import sys
import datetime
import importlib
import threading
from typing import Any, Dict, List
from pathlib import Path

import httpx
import respx
import pytest

from kernel.lib.credentials import (
    IdentityTokenFile,
    AWSSTSIdentityToken,
    StaticIdentityToken,
    WorkloadIdentityError,
    GCPMetadataIdentityToken,
    GitHubActionsIdentityToken,
    WorkloadIdentityCredentials,
)

from .utils import (
    AWS_JWT,
    RULE_ID,
    AUTH_URL,
    TOKEN_URL,
    GITHUB_JWT,
    GOOGLE_JWT,
    KUBERNETES_JWT,
    form,
    token_response,
)

# boto3 ships no type stubs.
boto3: Any = importlib.import_module("boto3")
Stubber: Any = importlib.import_module("botocore.stub").Stubber

GITHUB_REQUEST_URL = (
    "https://run-actions-1-azure-eastus.actions.githubusercontent.com/93//idtoken/abc/def?api-version=2.0"
)
GCP_IDENTITY_URL = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"


class TestIdentityTokenFile:
    def test_rereads_the_file_on_every_call_and_trims_it(self, tmp_path: Path) -> None:
        path = tmp_path / "token"
        path.write_text(f"  {KUBERNETES_JWT}\n")
        provider = IdentityTokenFile(path)
        assert provider() == KUBERNETES_JWT

        path.write_text("rotated-token\n")
        assert provider() == "rotated-token"

    def test_path_from_env(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        path = tmp_path / "token"
        path.write_text("from-env-path")
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_FILE", str(path))
        provider = IdentityTokenFile()
        assert provider.path == path
        assert provider() == "from-env-path"

    def test_no_path(self) -> None:
        with pytest.raises(WorkloadIdentityError, match="KERNEL_IDENTITY_TOKEN_FILE"):
            IdentityTokenFile()

    @pytest.mark.parametrize("content", ["", " \n\t\n"])
    def test_empty_file_is_an_error(self, tmp_path: Path, content: str) -> None:
        path = tmp_path / "token"
        path.write_text(content)
        with pytest.raises(WorkloadIdentityError, match="is empty"):
            IdentityTokenFile(path)()

    def test_missing_file(self, tmp_path: Path) -> None:
        with pytest.raises(WorkloadIdentityError, match="not found"):
            IdentityTokenFile(tmp_path / "missing")()

    def test_directory(self, tmp_path: Path) -> None:
        with pytest.raises(WorkloadIdentityError, match="is a directory"):
            IdentityTokenFile(tmp_path)()

    def test_undecodable_file_does_not_leak_its_contents(self, tmp_path: Path) -> None:
        path = tmp_path / "token"
        path.write_bytes(b"secret-prefix-\xff\xfe")
        with pytest.raises(WorkloadIdentityError, match="could not be read") as exc_info:
            IdentityTokenFile(path)()
        assert "secret-prefix" not in str(exc_info.value)


class TestStaticIdentityToken:
    def test_can_be_used_once(self) -> None:
        provider = StaticIdentityToken(f" {GITHUB_JWT}\n")
        assert provider() == GITHUB_JWT
        with pytest.raises(WorkloadIdentityError) as exc_info:
            provider()
        message = str(exc_info.value)
        assert "already exchanged once" in message
        assert "Every exchange needs a fresh provider token" in message
        assert "KERNEL_IDENTITY_TOKEN_FILE" in message
        assert GITHUB_JWT not in message

    def test_concurrent_callers_get_it_once(self) -> None:
        provider = StaticIdentityToken("only-once")
        results: List[str] = []

        def call() -> None:
            try:
                results.append(provider())
            except WorkloadIdentityError:
                results.append("refused")

        threads = [threading.Thread(target=call) for _ in range(16)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(5)
        assert sorted(results) == ["only-once"] + ["refused"] * 15

    def test_empty(self) -> None:
        with pytest.raises(WorkloadIdentityError, match="empty"):
            StaticIdentityToken("  ")

    def test_is_not_sent_again_after_a_failed_exchange(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(side_effect=httpx.ReadTimeout("timed out"))
        credentials = WorkloadIdentityCredentials(
            identity_token_provider=StaticIdentityToken(GITHUB_JWT), federation_rule_id=RULE_ID
        )
        with pytest.raises(WorkloadIdentityError, match="Failed to reach the token endpoint"):
            credentials()
        # The server may have used the token before the timeout, so it is not sent a second time.
        with pytest.raises(WorkloadIdentityError, match="already exchanged once"):
            credentials()
        assert route.call_count == 1


class TestGitHubActionsIdentityToken:
    @pytest.fixture(autouse=True)
    def github_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", GITHUB_REQUEST_URL)
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "github-request-token")

    def test_requests_a_token_for_the_audience(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT, "count": 1234})
        )
        assert GitHubActionsIdentityToken()() == GITHUB_JWT

        request = route.calls.last.request
        assert str(request.url) == f"{GITHUB_REQUEST_URL}&audience=https%3A%2F%2Fauth.onkernel.com"
        assert request.headers["Authorization"] == "Bearer github-request-token"
        assert request.headers["User-Agent"].startswith("Kernel/Python ")

    def test_request_token_is_trimmed(self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "github-request-token\n")
        route = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )
        GitHubActionsIdentityToken()()
        assert route.calls.last.request.headers["Authorization"] == "Bearer github-request-token"

    def test_request_url_without_a_query(self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", "https://actions.example/idtoken")
        route = respx_mock.get(url__startswith="https://actions.example/idtoken").mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )
        GitHubActionsIdentityToken(audience="my audience&x=1")()
        assert str(route.calls.last.request.url) == "https://actions.example/idtoken?audience=my%20audience%26x%3D1"

    def test_audience_precedence(self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
        route = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )

        def requested_audience() -> str:
            audience: str = route.calls.last.request.url.params["audience"]
            return audience

        source = GitHubActionsIdentityToken()
        # Default: the auth base URL, which is also where the default comes from when a client passes it.
        source()
        assert requested_audience() == AUTH_URL
        source.fetch(default_audience="https://auth.other.example", http_client=None)
        assert requested_audience() == "https://auth.other.example"

        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_AUDIENCE", "audience-from-env")
        source.fetch(default_audience="https://auth.other.example", http_client=None)
        assert requested_audience() == "audience-from-env"

        GitHubActionsIdentityToken(audience="explicit-audience")()
        assert requested_audience() == "explicit-audience"

    def test_http_client_defaults_do_not_leak_into_the_request(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )
        # An API client's default query parameters would otherwise replace the request URL's own.
        with httpx.Client(params={"tenant": "acme"}, headers={"X-Api-Default": "1"}) as http_client:
            GitHubActionsIdentityToken().fetch(default_audience=None, http_client=http_client)

        request = route.calls.last.request
        assert str(request.url) == f"{GITHUB_REQUEST_URL}&audience=https%3A%2F%2Fauth.onkernel.com"
        assert "X-Api-Default" not in request.headers

    @pytest.mark.parametrize("missing", ["ACTIONS_ID_TOKEN_REQUEST_URL", "ACTIONS_ID_TOKEN_REQUEST_TOKEN"])
    def test_missing_variables_point_at_the_permission(self, monkeypatch: pytest.MonkeyPatch, missing: str) -> None:
        monkeypatch.delenv(missing)
        with pytest.raises(WorkloadIdentityError, match="permissions: id-token: write"):
            GitHubActionsIdentityToken()()

    def test_request_url_must_be_https(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", "http://actions.example/idtoken")
        with pytest.raises(WorkloadIdentityError, match="must use https"):
            GitHubActionsIdentityToken()()

    @pytest.mark.parametrize(
        "response",
        [
            httpx.Response(403, json={"message": "forbidden"}),
            httpx.Response(200, json={"count": 1}),
            httpx.Response(200, json={"value": ""}),
            httpx.Response(200, text="not json"),
            httpx.Response(200, json=[GITHUB_JWT]),
        ],
    )
    def test_failed_request(self, respx_mock: respx.MockRouter, response: httpx.Response) -> None:
        respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(return_value=response)
        with pytest.raises(WorkloadIdentityError, match="GitHub Actions identity token"):
            GitHubActionsIdentityToken()()

    async def test_async_fetch(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )
        async with httpx.AsyncClient() as http_client:
            token = await GitHubActionsIdentityToken().async_fetch(default_audience=None, http_client=http_client)
        assert token == GITHUB_JWT
        assert route.calls.last.request.headers["Authorization"] == "Bearer github-request-token"


class TestGCPMetadataIdentityToken:
    def test_requests_a_full_format_token_for_the_audience(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.get(url__startswith=GCP_IDENTITY_URL).mock(
            return_value=httpx.Response(200, text=GOOGLE_JWT + "\n")
        )
        assert GCPMetadataIdentityToken()() == GOOGLE_JWT

        request = route.calls.last.request
        assert str(request.url) == f"{GCP_IDENTITY_URL}?audience=https%3A%2F%2Fauth.onkernel.com&format=full"
        assert request.headers["Metadata-Flavor"] == "Google"

    def test_explicit_audience(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.get(url__startswith=GCP_IDENTITY_URL).mock(return_value=httpx.Response(200, text=GOOGLE_JWT))
        GCPMetadataIdentityToken(audience="https://auth.other.example")()
        assert route.calls.last.request.url.params["audience"] == "https://auth.other.example"

    @pytest.mark.parametrize("response", [httpx.Response(404, text="not found"), httpx.Response(200, text="  ")])
    def test_failed_request(self, respx_mock: respx.MockRouter, response: httpx.Response) -> None:
        respx_mock.get(url__startswith=GCP_IDENTITY_URL).mock(return_value=response)
        with pytest.raises(WorkloadIdentityError, match="Google Cloud metadata server"):
            GCPMetadataIdentityToken()()

    def test_unreachable(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get(url__startswith=GCP_IDENTITY_URL).mock(side_effect=httpx.ConnectError("no route"))
        with pytest.raises(WorkloadIdentityError, match="Failed to reach the Google Cloud metadata server"):
            GCPMetadataIdentityToken()()

    async def test_async_fetch_does_not_use_the_api_http_client(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.get(url__startswith=GCP_IDENTITY_URL).mock(return_value=httpx.Response(200, text=GOOGLE_JWT))

        def unexpected(request: httpx.Request) -> httpx.Response:
            raise AssertionError(f"metadata request went through the API HTTP client: {request.url}")

        # The API client may be configured with a proxy, which cannot reach the metadata server.
        async with httpx.AsyncClient(transport=httpx.MockTransport(unexpected)) as api_http_client:
            token = await GCPMetadataIdentityToken().async_fetch(default_audience=None, http_client=api_http_client)
        assert token == GOOGLE_JWT
        assert route.called


class TestAWSSTSIdentityToken:
    @pytest.fixture(autouse=True)
    def aws_credentials(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("AWS_ACCESS_KEY_ID", "AKIAIOSFODNN7EXAMPLE")
        monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
        monkeypatch.setenv("AWS_EC2_METADATA_DISABLED", "true")

    def stub(self, source: AWSSTSIdentityToken, expected: Dict[str, Any]) -> Any:
        client = source._client()
        stubber = Stubber(client)
        stubber.add_response(
            "get_web_identity_token",
            {"WebIdentityToken": AWS_JWT, "Expiration": datetime.datetime(2026, 11, 19, 0, 5)},
            expected,
        )
        stubber.activate()
        return client

    def test_installed_boto3_has_get_web_identity_token(self) -> None:
        assert hasattr(boto3.client("sts", region_name="us-east-1"), "get_web_identity_token")

    def test_calls_get_web_identity_token(self) -> None:
        source = AWSSTSIdentityToken()
        client = self.stub(source, {"Audience": [AUTH_URL], "SigningAlgorithm": "RS256", "DurationSeconds": 300})
        assert source() == AWS_JWT
        # Defaults to us-east-1, on the regional endpoint.
        assert client.meta.region_name == "us-east-1"
        assert client.meta.endpoint_url == "https://sts.us-east-1.amazonaws.com"

    def test_audience_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("KERNEL_IDENTITY_TOKEN_AUDIENCE", "audience-from-env")
        source = AWSSTSIdentityToken()
        self.stub(source, {"Audience": ["audience-from-env"], "SigningAlgorithm": "RS256", "DurationSeconds": 300})
        assert source() == AWS_JWT

    @pytest.mark.parametrize(
        "env, region",
        [
            ({}, "us-east-1"),
            ({"AWS_DEFAULT_REGION": "ap-southeast-2"}, "ap-southeast-2"),
            ({"AWS_REGION": "eu-west-1", "AWS_DEFAULT_REGION": "ap-southeast-2"}, "eu-west-1"),
        ],
    )
    def test_region_from_env(self, monkeypatch: pytest.MonkeyPatch, env: Dict[str, str], region: str) -> None:
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        client = AWSSTSIdentityToken()._client()
        assert client.meta.region_name == region
        assert client.meta.endpoint_url == f"https://sts.{region}.amazonaws.com"

    def test_explicit_region(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("AWS_REGION", "eu-west-1")
        assert AWSSTSIdentityToken(region="us-west-2")._client().meta.region_name == "us-west-2"

    @pytest.mark.parametrize("region", ["us-east-1", "eu-west-1"])
    def test_never_uses_the_global_endpoint(self, monkeypatch: pytest.MonkeyPatch, region: str) -> None:
        # In legacy mode boto3 would send these regions to sts.amazonaws.com, which does not serve this API.
        monkeypatch.setenv("AWS_STS_REGIONAL_ENDPOINTS", "legacy")
        assert boto3.client("sts", region_name=region).meta.endpoint_url == "https://sts.amazonaws.com"
        client = AWSSTSIdentityToken(region=region)._client()
        assert client.meta.endpoint_url == f"https://sts.{region}.amazonaws.com"

    def test_sts_error_is_wrapped(self) -> None:
        source = AWSSTSIdentityToken()
        stubber = Stubber(source._client())
        stubber.add_client_error(
            "get_web_identity_token",
            service_error_code="OutboundWebIdentityFederationDisabled",
            service_message="Outbound web identity federation is not enabled for this account.",
        )
        stubber.activate()
        with pytest.raises(WorkloadIdentityError, match="AWS STS GetWebIdentityToken failed") as exc_info:
            source()
        assert "not enabled for this account" in str(exc_info.value)

    def test_missing_boto3_error_says_how_to_install_it(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setitem(sys.modules, "boto3", None)
        with pytest.raises(WorkloadIdentityError) as exc_info:
            AWSSTSIdentityToken()()
        assert 'pip install "kernel[aws]"' in str(exc_info.value)
        assert "boto3>=1.41.0" in str(exc_info.value)

    def test_boto3_too_old_error_says_to_upgrade(self, monkeypatch: pytest.MonkeyPatch) -> None:
        class OldClient:
            pass

        class OldBoto3:
            __version__ = "1.40.0"

            @staticmethod
            def client(*_args: object, **_kwargs: object) -> OldClient:
                return OldClient()

        monkeypatch.setitem(sys.modules, "boto3", OldBoto3)
        with pytest.raises(WorkloadIdentityError, match=r"boto3 \(1\.40\.0\) does not support STS GetWebIdentityToken"):
            AWSSTSIdentityToken()()

    async def test_async_fetch_runs_off_the_event_loop(self) -> None:
        source = AWSSTSIdentityToken()
        self.stub(
            source, {"Audience": ["https://auth.other.example"], "SigningAlgorithm": "RS256", "DurationSeconds": 300}
        )
        loop_thread = threading.get_ident()
        fetch_threads: List[int] = []
        fetch = source.fetch

        def recording_fetch(**kwargs: Any) -> str:
            fetch_threads.append(threading.get_ident())
            return fetch(**kwargs)

        source.fetch = recording_fetch  # type: ignore[method-assign]
        token = await source.async_fetch(default_audience="https://auth.other.example", http_client=None)
        assert token == AWS_JWT
        assert fetch_threads and fetch_threads[0] != loop_thread


class TestSourcesInsideAnExchange:
    def test_default_audience_is_the_auth_base_url(
        self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", GITHUB_REQUEST_URL)
        monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "github-request-token")
        github = respx_mock.get(url__startswith=GITHUB_REQUEST_URL).mock(
            return_value=httpx.Response(200, json={"value": GITHUB_JWT})
        )
        token_route = respx_mock.post("https://auth.other.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )

        WorkloadIdentityCredentials(
            identity_token_provider=GitHubActionsIdentityToken(),
            federation_rule_id=RULE_ID,
            auth_base_url="https://auth.other.example",
        )()

        assert github.calls.last.request.url.params["audience"] == "https://auth.other.example"
        assert dict(form(token_route.calls.last.request))["assertion"] == GITHUB_JWT
        # The GitHub request token is for GitHub only.
        assert "Authorization" not in token_route.calls.last.request.headers
