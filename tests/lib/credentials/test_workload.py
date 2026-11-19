from __future__ import annotations

import gzip
import time
from typing import Any, Dict, List, Iterator
from pathlib import Path

import httpx
import respx
import pytest

from kernel import KernelError
from kernel.lib.credentials import (
    Principal,
    IdentityTokenFile,
    StaticIdentityToken,
    WorkloadIdentityError,
    WorkloadIdentityCredentials,
    exchange_federation_assertion,
    async_exchange_federation_assertion,
)
from kernel.lib.credentials._constants import api_origin, resolve_auth_base_url

from .utils import (
    API_URL,
    RULE_ID,
    AUTH_URL,
    TOKEN_URL,
    GITHUB_JWT,
    GRANT_TYPE,
    PROVIDER_JWTS,
    form,
    requests,
    token_response,
    counting_identity_tokens,
)


def credentials(**kwargs: Any) -> WorkloadIdentityCredentials:
    kwargs.setdefault("identity_token_provider", counting_identity_tokens())
    kwargs.setdefault("federation_rule_id", RULE_ID)
    return WorkloadIdentityCredentials(**kwargs)


class TestExchangeRequest:
    @pytest.mark.parametrize("provider", sorted(PROVIDER_JWTS))
    def test_sends_exactly_the_four_parameters(self, respx_mock: respx.MockRouter, provider: str) -> None:
        assertion = PROVIDER_JWTS[provider]
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))

        credentials(identity_token_provider=lambda: assertion, resource=API_URL)()

        request = route.calls.last.request
        assert form(request) == [
            ("grant_type", GRANT_TYPE),
            ("assertion", assertion),
            ("federation_rule_id", RULE_ID),
            ("resource", API_URL),
        ]
        assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
        assert request.headers["User-Agent"].startswith("Kernel/Python ")
        assert request.headers["Accept-Encoding"] == "identity"
        # The token endpoint rejects any request that carries client authentication.
        assert "Authorization" not in request.headers

    def test_standalone_exchanges_omit_resource_unless_given(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))

        # There is no client here whose API the token is for, and the parameter is optional.
        exchange_federation_assertion(assertion=GITHUB_JWT, federation_rule_id=RULE_ID)
        assert [name for name, _ in form(route.calls.last.request)] == ["grant_type", "assertion", "federation_rule_id"]
        credentials()()
        assert [name for name, _ in form(route.calls.last.request)] == ["grant_type", "assertion", "federation_rule_id"]

        exchange_federation_assertion(assertion=GITHUB_JWT, federation_rule_id=RULE_ID, resource=API_URL)
        assert dict(form(route.calls.last.request))["resource"] == API_URL

    def test_every_exchange_uses_a_fresh_identity_token(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        creds = credentials()

        creds()
        creds()
        creds(force_refresh=True)

        assertions = [dict(form(request))["assertion"] for request in requests(route)]
        assert assertions == ["identity-token-1", "identity-token-2", "identity-token-3"]

    def test_http_client_defaults_do_not_leak_into_the_request(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(url__startswith=TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        with httpx.Client(
            headers={"Authorization": "Bearer from-client", "Content-Type": "application/json", "X-Api-Default": "1"},
            params={"tenant": "acme"},
            cookies={"session": "abc"},
            auth=("user", "pass"),
        ) as http_client:
            credentials(http_client=http_client)()

        request = route.calls.last.request
        assert str(request.url) == TOKEN_URL
        assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
        for header in ("Authorization", "X-Api-Default", "Cookie"):
            assert header not in request.headers

    def test_does_not_follow_redirects(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(307, headers={"Location": "https://elsewhere.example/token"})
        )
        elsewhere = respx_mock.post("https://elsewhere.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )
        with httpx.Client(follow_redirects=True) as http_client:
            with pytest.raises(WorkloadIdentityError, match=r"HTTP 307") as exc_info:
                credentials(http_client=http_client)()
        assert exc_info.value.status_code == 307
        assert not elsewhere.called

    def test_connection_failure(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(side_effect=httpx.ConnectError("connection refused"))
        with pytest.raises(WorkloadIdentityError, match="Failed to reach the token endpoint") as exc_info:
            credentials()()
        assert exc_info.value.status_code is None

    @pytest.mark.parametrize(
        "error, message",
        [
            # What the HTTP stack raises for a header value it cannot send, such as one with a newline,
            (httpx.LocalProtocolError("Illegal header value b'Bearer secret-token\\n'"), "could not be sent"),
            # and for a response header line it cannot parse.
            (httpx.RemoteProtocolError("illegal header line: bytearray(b'secret-token')"), "was not valid HTTP"),
        ],
    )
    def test_protocol_errors_do_not_quote_headers(
        self, respx_mock: respx.MockRouter, error: httpx.ProtocolError, message: str
    ) -> None:
        respx_mock.post(TOKEN_URL).mock(side_effect=error)
        with pytest.raises(WorkloadIdentityError, match=message) as exc_info:
            credentials()()
        assert "secret-token" not in str(exc_info.value)
        assert exc_info.value.__cause__ is None
        assert exc_info.value.__suppress_context__


class TestExchangeResponse:
    def test_parses_the_token_and_what_it_was_issued_to(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response(expires_in=298)))
        before = time.time()

        token = credentials()()

        assert token.token == "access-token-1"
        assert token.expires_at is not None
        assert before + 298 <= token.expires_at <= time.time() + 298
        assert token.scope == "browsers:create browsers:use browsers:delete"
        assert token.project_id == "proj_456"
        assert token.principal == Principal(type="service_account", id="svc_789")
        assert token.federation_rule_id == RULE_ID
        assert "access-token-1" not in repr(token)

    @pytest.mark.parametrize("expires_in", [1, 0.5, 298, 600])
    def test_expires_in_is_authoritative(self, respx_mock: respx.MockRouter, expires_in: float) -> None:
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response(expires_in=expires_in)))
        before = time.time()
        token = credentials()()
        assert token.expires_at is not None
        assert before + expires_in <= token.expires_at <= time.time() + expires_in

    def test_token_type_is_optional(self, respx_mock: respx.MockRouter) -> None:
        body = token_response()
        del body["token_type"]
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=body))
        assert credentials()().token == "access-token-1"

    @pytest.mark.parametrize(
        "overrides, reason",
        [
            ({"token_type": "MAC"}, "token_type is not Bearer"),
            ({"access_token": ""}, "access_token is missing"),
            ({"access_token": None}, "access_token is missing"),
            ({"expires_in": None}, "expires_in is missing or not a number"),
            ({"expires_in": "298"}, "expires_in is missing or not a number"),
            ({"expires_in": True}, "expires_in is missing or not a number"),
            ({"expires_in": 0}, "expires_in is not a positive number"),
            ({"expires_in": -5}, "expires_in is not a positive number"),
        ],
    )
    def test_unusable_success_response(
        self, respx_mock: respx.MockRouter, overrides: Dict[str, Any], reason: str
    ) -> None:
        body = {**token_response("secret-access-token"), **overrides}
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=body))
        with pytest.raises(WorkloadIdentityError, match=reason) as exc_info:
            credentials()()
        assert "secret-access-token" not in str(exc_info.value)

    @pytest.mark.parametrize("content", [b"<html>gateway</html>", b"[1, 2]", b'"access-token"'])
    def test_success_response_that_is_not_a_json_object(self, respx_mock: respx.MockRouter, content: bytes) -> None:
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, content=content))
        with pytest.raises(WorkloadIdentityError, match="not a JSON object") as exc_info:
            credentials()()
        assert "gateway" not in str(exc_info.value)

    def test_response_over_the_size_limit_is_refused(self, respx_mock: respx.MockRouter) -> None:
        body = token_response(padding="x" * (1 << 20))
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=body))
        with pytest.raises(WorkloadIdentityError, match="larger than 1048576 bytes"):
            credentials()()

    def test_declared_length_over_the_limit_is_refused_before_reading(self, respx_mock: respx.MockRouter) -> None:
        def body() -> Iterator[bytes]:
            raise AssertionError("the body was read")
            yield b""

        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(200, headers={"Content-Length": str((1 << 20) + 1)}, content=body())
        )
        with pytest.raises(WorkloadIdentityError, match="larger than 1048576 bytes"):
            credentials()()

    def test_streamed_response_stops_being_read_at_the_limit(self, respx_mock: respx.MockRouter) -> None:
        chunks_read = 0

        def body() -> Iterator[bytes]:
            nonlocal chunks_read
            for _ in range(1000):
                chunks_read += 1
                yield b"x" * 65536

        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, content=body()))
        with pytest.raises(WorkloadIdentityError, match="larger than 1048576 bytes"):
            credentials()()
        assert chunks_read == 17

    def test_compressed_response_is_refused(self, respx_mock: respx.MockRouter) -> None:
        # A small compressed body can expand far past the limit, so no encoding is accepted.
        compressed = gzip.compress(httpx.Response(200, json=token_response()).content)
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(200, headers={"Content-Encoding": "gzip"}, content=iter([compressed]))
        )
        with pytest.raises(WorkloadIdentityError, match="has a content encoding"):
            credentials()()

    def test_response_at_the_size_limit_is_read(self, respx_mock: respx.MockRouter) -> None:
        body = httpx.Response(200, json=token_response()).content
        padded = body[:-1] + b" " * ((1 << 20) - len(body)) + b"}"
        assert len(padded) == 1 << 20
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, content=padded))
        assert credentials()().token == "access-token-1"


class TestExchangeErrors:
    def test_invalid_grant(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400,
                json={"error": "invalid_grant", "error_description": "Credential is invalid, expired, or revoked"},
                headers={"x-request-id": "req_abc"},
            )
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials()()

        err = exc_info.value
        assert isinstance(err, KernelError)
        assert err.status_code == 400
        assert err.error == "invalid_grant"
        assert err.error_description == "Credential is invalid, expired, or revoked"
        assert err.request_id == "req_abc"
        assert str(err) == (
            "Token exchange failed (HTTP 400): invalid_grant: Credential is invalid, expired, or revoked "
            "[request_id=req_abc]"
        )

    @pytest.fixture
    def replayed(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_grant", "error_description": "Credential was already used"}
            )
        )

    REPLAYED = (
        "Token exchange failed (HTTP 400): invalid_grant: Credential was already used. Every exchange needs a "
        "fresh provider token: most identity providers' tokens can be exchanged only once"
    )

    @pytest.mark.usefixtures("replayed")
    def test_replayed_static_token_hint(self) -> None:
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials(identity_token_provider=StaticIdentityToken(GITHUB_JWT))()
        assert str(exc_info.value) == f"{self.REPLAYED}, so a static KERNEL_IDENTITY_TOKEN works for a single exchange."

    @pytest.mark.usefixtures("replayed")
    def test_replayed_file_token_hint(self, tmp_path: Path) -> None:
        path = tmp_path / "token"
        path.write_text(GITHUB_JWT)
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials(identity_token_provider=IdentityTokenFile(path))()
        # A file that was not rotated is not a static token, and for some issuers reuse can be allowed.
        assert str(exc_info.value) == (
            f"{self.REPLAYED}. The file at {path} still held a token that had already been exchanged, so whatever "
            "writes that file must rotate it before each refresh. For Kubernetes projected service-account tokens, "
            "the issuer can be configured to allow reuse instead."
        )

    @pytest.mark.usefixtures("replayed")
    def test_replayed_callback_token_hint(self) -> None:
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials(identity_token_provider=lambda: GITHUB_JWT)()
        assert str(exc_info.value) == (
            f"{self.REPLAYED}, so the identity token provider must return a newly issued token on every call."
        )
        assert "KERNEL_IDENTITY_TOKEN" not in str(exc_info.value)

    @pytest.mark.usefixtures("replayed")
    def test_replayed_one_shot_assertion_hint(self) -> None:
        with pytest.raises(WorkloadIdentityError) as exc_info:
            exchange_federation_assertion(assertion=GITHUB_JWT, federation_rule_id=RULE_ID)
        assert str(exc_info.value) == f"{self.REPLAYED}, so the same assertion cannot be exchanged again."

    @pytest.mark.parametrize("resource", ["https://api.onkernel.com/", "https://not-the-api.example"])
    def test_rejected_resource_gets_a_hint(self, respx_mock: respx.MockRouter, resource: str) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_target", "error_description": "Invalid resource parameter"}
            )
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials(resource=resource)()
        assert exc_info.value.error == "invalid_target"
        assert str(exc_info.value) == (
            "Token exchange failed (HTTP 400): invalid_target: Invalid resource parameter. "
            "Set resource to the Kernel API origin with no trailing slash."
        )

    @pytest.mark.parametrize(
        "status, error, description",
        [
            (400, "invalid_grant", "Credential is invalid, expired, or revoked"),
            (400, "invalid_request", "Missing required parameter: federation_rule_id"),
            (503, "temporarily_unavailable", "Try again"),
        ],
    )
    def test_other_oauth_errors_have_no_hint(
        self, respx_mock: respx.MockRouter, status: int, error: str, description: str
    ) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(status, json={"error": error, "error_description": description})
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials()()
        assert exc_info.value.status_code == status
        assert exc_info.value.error == error
        assert str(exc_info.value) == f"Token exchange failed (HTTP {status}): {error}: {description}"

    def test_error_body_is_reduced_to_the_oauth_fields(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400,
                json={
                    "error": "invalid_grant",
                    "error_description": "nope",
                    "error_uri": "https://docs.example/errors",
                    "access_token": "leaked-access-token",
                    "debug": {"assertion": "leaked-assertion"},
                },
            )
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials()()
        assert exc_info.value.body == {
            "error": "invalid_grant",
            "error_description": "nope",
            "error_uri": "https://docs.example/errors",
        }
        assert "leaked" not in str(exc_info.value)

    def test_assertion_echoed_in_an_error_is_redacted(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_grant", "error_description": f"could not verify {GITHUB_JWT}"}
            )
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials(identity_token_provider=lambda: GITHUB_JWT)()
        err = exc_info.value
        assert GITHUB_JWT not in str(err)
        assert GITHUB_JWT not in repr(err)
        assert GITHUB_JWT not in str(err.body)
        assert err.error_description == "could not verify [REDACTED]"

    def test_assertion_echoed_in_the_request_id_is_redacted(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(400, json={"error": "invalid_grant"}, headers={"x-request-id": GITHUB_JWT})
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials(identity_token_provider=lambda: GITHUB_JWT)()
        assert exc_info.value.request_id == "[REDACTED]"
        assert GITHUB_JWT not in str(exc_info.value)

    def test_long_error_description_is_cut(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(
            return_value=httpx.Response(400, json={"error": "invalid_grant", "error_description": "x" * 5000})
        )
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials()()
        assert exc_info.value.error_description == "x" * 256 + "..."

    def test_non_json_error_body_is_not_included(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(502, text="<html>upstream said: hunter2</html>"))
        with pytest.raises(WorkloadIdentityError) as exc_info:
            credentials()()
        assert str(exc_info.value) == "Token exchange failed (HTTP 502)"
        assert exc_info.value.body == {}


class TestAssertionChecks:
    def test_assertion_over_16_kib_is_rejected_before_sending(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        oversized = "a" * (16 * 1024 + 1)
        with pytest.raises(WorkloadIdentityError, match="over the 16384-byte limit") as exc_info:
            credentials(identity_token_provider=lambda: oversized)()
        assert not route.called
        assert oversized[:64] not in str(exc_info.value)

    def test_assertion_of_exactly_16_kib_is_sent(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        credentials(identity_token_provider=lambda: "a" * (16 * 1024))()
        assert route.called

    @pytest.mark.parametrize("token", ["", "   \n"])
    def test_empty_assertion_is_rejected(self, respx_mock: respx.MockRouter, token: str) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        with pytest.raises(WorkloadIdentityError, match="empty token"):
            credentials(identity_token_provider=lambda: token)()
        assert not route.called

    def test_sync_exchange_rejects_an_async_identity_token_provider(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))

        async def provider() -> str:
            return GITHUB_JWT

        with pytest.raises(TypeError, match="use `AsyncKernel` instead"):
            credentials(identity_token_provider=provider)()
        assert not route.called


class TestEndpoints:
    @pytest.mark.parametrize(
        "auth_base_url",
        ["http://auth.onkernel.com", "http://localhost.evil.example", "ftp://auth.onkernel.com", "auth.onkernel.com"],
    )
    def test_token_endpoint_must_be_https(self, auth_base_url: str) -> None:
        with pytest.raises(WorkloadIdentityError, match="must use https"):
            credentials(auth_base_url=auth_base_url)

    def test_token_endpoint_must_not_carry_credentials(self) -> None:
        # httpx would send them as Basic auth, and the token endpoint rejects any Authorization header.
        with pytest.raises(WorkloadIdentityError, match="must not contain a username or password") as exc_info:
            credentials(auth_base_url="https://user:hunter2@auth.onkernel.com")
        assert "hunter2" not in str(exc_info.value)

    @pytest.mark.parametrize(
        "auth_base_url", ["http://localhost:8787", "http://127.0.0.1:8787", "http://[::1]:8787", "http://localhost"]
    )
    def test_http_is_allowed_for_loopback(self, respx_mock: respx.MockRouter, auth_base_url: str) -> None:
        route = respx_mock.post(f"{auth_base_url}/token").mock(return_value=httpx.Response(200, json=token_response()))
        credentials(auth_base_url=auth_base_url)()
        assert route.called

    def test_auth_base_url_env_must_be_https(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("KERNEL_AUTH_BASE_URL", "http://auth.other.example")
        with pytest.raises(WorkloadIdentityError, match="KERNEL_AUTH_BASE_URL must use https"):
            credentials()()

    def test_auth_base_url_precedence(self, monkeypatch: pytest.MonkeyPatch) -> None:
        assert resolve_auth_base_url(None, api_base_url=API_URL) == AUTH_URL
        assert resolve_auth_base_url(None, api_base_url=API_URL + "/") == AUTH_URL

        monkeypatch.setenv("KERNEL_AUTH_BASE_URL", "https://auth.other.example/")
        assert resolve_auth_base_url(None, api_base_url=API_URL) == "https://auth.other.example"
        assert (
            resolve_auth_base_url("https://auth.explicit.example", api_base_url=API_URL)
            == "https://auth.explicit.example"
        )

    def test_custom_api_base_url_needs_an_auth_base_url(self) -> None:
        with pytest.raises(WorkloadIdentityError, match="auth base URL cannot be inferred") as exc_info:
            resolve_auth_base_url(None, api_base_url="https://api.other.example/")
        assert "KERNEL_AUTH_BASE_URL" in str(exc_info.value)

    def test_standalone_exchange_does_not_use_production_for_a_custom_api(
        self, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        production = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        monkeypatch.setenv("KERNEL_BASE_URL", "https://api.other.example")

        with pytest.raises(WorkloadIdentityError, match="auth base URL cannot be inferred"):
            exchange_federation_assertion(assertion=GITHUB_JWT, federation_rule_id=RULE_ID)
        with pytest.raises(WorkloadIdentityError, match="auth base URL cannot be inferred"):
            credentials()()
        assert not production.called

        other = respx_mock.post("https://auth.other.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )
        monkeypatch.setenv("KERNEL_AUTH_BASE_URL", "https://auth.other.example")
        credentials()()
        assert other.call_count == 1

    @pytest.mark.parametrize(
        "base_url, origin",
        [
            ("https://api.onkernel.com/", "https://api.onkernel.com"),
            ("https://api.other.example", "https://api.other.example"),
            ("https://api.example.com/v1/", "https://api.example.com"),
            ("http://localhost:3001/", "http://localhost:3001"),
            ("https://user:hunter2@api.example.com/v1", "https://api.example.com"),
        ],
    )
    def test_resource_is_the_api_origin(self, base_url: str, origin: str) -> None:
        assert api_origin(base_url) == origin

    def test_explicit_resource(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL).mock(return_value=httpx.Response(200, json=token_response()))
        credentials(resource="https://mcp.onkernel.com")()
        assert dict(form(route.calls.last.request))["resource"] == "https://mcp.onkernel.com"

    def test_empty_federation_rule_id(self) -> None:
        with pytest.raises(WorkloadIdentityError, match="federation_rule_id must not be empty"):
            credentials(federation_rule_id="")


class TestAsyncExchange:
    async def test_one_shot(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post("https://auth.other.example/token").mock(
            return_value=httpx.Response(200, json=token_response())
        )
        token = await async_exchange_federation_assertion(
            assertion=GITHUB_JWT,
            federation_rule_id=RULE_ID,
            resource="https://api.other.example",
            auth_base_url="https://auth.other.example",
        )
        assert token.token == "access-token-1"
        assert token.principal == Principal(type="service_account", id="svc_789")
        assert form(route.calls.last.request) == [
            ("grant_type", GRANT_TYPE),
            ("assertion", GITHUB_JWT),
            ("federation_rule_id", RULE_ID),
            ("resource", "https://api.other.example"),
        ]
        assert "Authorization" not in route.calls.last.request.headers

    async def test_error_and_size_limit(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post(TOKEN_URL)
        route.mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_grant", "error_description": "Credential was already used"}
            )
        )
        with pytest.raises(WorkloadIdentityError, match="Every exchange needs a fresh provider token"):
            await async_exchange_federation_assertion(assertion=GITHUB_JWT, federation_rule_id=RULE_ID)

        route.mock(return_value=httpx.Response(200, json=token_response(padding="x" * (1 << 20))))
        with pytest.raises(WorkloadIdentityError, match="larger than 1048576 bytes"):
            await async_exchange_federation_assertion(assertion=GITHUB_JWT, federation_rule_id=RULE_ID)

    async def test_uses_the_given_http_client(self) -> None:
        seen: List[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(request)
            return httpx.Response(200, json=token_response())

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http_client:
            await async_exchange_federation_assertion(
                assertion=GITHUB_JWT, federation_rule_id=RULE_ID, http_client=http_client
            )
        assert [str(request.url) for request in seen] == [TOKEN_URL]
