from __future__ import annotations

import json
import base64
from typing import Any, Dict, List, Callable, Optional, cast
from urllib.parse import parse_qsl

import httpx
import respx

API_URL = "https://api.onkernel.com"
AUTH_URL = "https://auth.onkernel.com"
TOKEN_URL = f"{AUTH_URL}/token"
RULE_ID = "wifr_01jz8k3m5n7p9q"
GRANT_TYPE = "urn:ietf:params:oauth:grant-type:jwt-bearer"

FEDERATION_ENV_VARS = (
    "KERNEL_API_KEY",
    "KERNEL_BASE_URL",
    "KERNEL_AUTH_BASE_URL",
    "KERNEL_FEDERATION_RULE_ID",
    "KERNEL_IDENTITY_TOKEN_SOURCE",
    "KERNEL_IDENTITY_TOKEN_AUDIENCE",
    "KERNEL_IDENTITY_TOKEN_FILE",
    "KERNEL_IDENTITY_TOKEN",
    "ACTIONS_ID_TOKEN_REQUEST_URL",
    "ACTIONS_ID_TOKEN_REQUEST_TOKEN",
    "GITHUB_ACTIONS",
    "GCE_METADATA_HOST",
    "AWS_REGION",
    "AWS_DEFAULT_REGION",
    "AWS_STS_REGIONAL_ENDPOINTS",
)


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def make_jwt(header: Dict[str, Any], claims: Dict[str, Any]) -> str:
    """An unsigned token with the given header and claims. The SDK never inspects it."""
    return ".".join(
        (
            _b64url(json.dumps(header, separators=(",", ":")).encode()),
            _b64url(json.dumps(claims, separators=(",", ":")).encode()),
            _b64url(b"signature"),
        )
    )


# Tokens shaped like the ones each identity provider issues. All values are made up.
_IAT = 1_795_000_000

GITHUB_JWT = make_jwt(
    {"alg": "RS256", "kid": "38826b17-6a30-5f9b-b169-8beb8202f723", "typ": "JWT", "x5t": "ykNaY4qM_ta4k2TgZOCEYLkcYlA"},
    {
        "iss": "https://token.actions.githubusercontent.com",
        "aud": AUTH_URL,
        "sub": "repo:acme@123/widgets@456:ref:refs/heads/main",
        "repository": "acme/widgets",
        "repository_id": "456",
        "repository_owner_id": "123",
        "jti": "1e4b7c1c-5a60-4c5e-9d0b-0f8a4a1f2b3c",
        "iat": _IAT,
        "nbf": _IAT - 300,
        "exp": _IAT + 300,
    },
)

AWS_JWT = make_jwt(
    {"alg": "RS256", "kid": "RSA_0", "typ": "JWT"},
    {
        "iss": "https://a1b2c3d4-5678-90ab-cdef-111122223333.tokens.sts.global.api.aws",
        "aud": AUTH_URL,
        "sub": "arn:aws:iam::123456789012:role/service/deploy/kernel-runner",
        "jti": "6f1d2c3b-4a59-4e8d-9c7b-a1b2c3d4e5f6",
        "iat": _IAT,
        "exp": _IAT + 300,
        "https://sts.amazonaws.com/": {
            "aws_account": "123456789012",
            "source_region": "us-east-1",
            "principal_id": "arn:aws:iam::123456789012:role/service/deploy/kernel-runner",
        },
    },
)

GOOGLE_JWT = make_jwt(
    {"alg": "RS256", "kid": "c8ab71530972bba20b49f78a09c9852c43ff9118", "typ": "JWT"},
    {
        "iss": "https://accounts.google.com",
        "aud": AUTH_URL,
        "azp": "104212345678901234567",
        "sub": "104212345678901234567",
        "email": "runner@acme-prod.iam.gserviceaccount.com",
        "email_verified": True,
        "iat": _IAT,
        "exp": _IAT + 3600,
    },
)

KUBERNETES_JWT = make_jwt(
    {"alg": "RS256", "kid": "Zq3xk0d5m1v8n2b7c4"},
    {
        "iss": "https://kubernetes.default.svc.cluster.local",
        "aud": [AUTH_URL],
        "sub": "system:serviceaccount:agents:kernel-runner",
        "jti": "0b7e6f5d-4c3b-4a29-8170-f6e5d4c3b2a1",
        "iat": _IAT,
        "nbf": _IAT,
        "exp": _IAT + 3600,
        "kubernetes.io": {"namespace": "agents", "serviceaccount": {"name": "kernel-runner", "uid": "5d6e7f80"}},
    },
)

PROVIDER_JWTS = {
    "github": GITHUB_JWT,
    "aws": AWS_JWT,
    "google": GOOGLE_JWT,
    "kubernetes": KUBERNETES_JWT,
}


def token_response(
    access_token: str = "access-token-1", *, expires_in: float = 298, **overrides: Any
) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "token_type": "Bearer",
        "access_token": access_token,
        "expires_in": expires_in,
        "scope": "browsers:create browsers:use browsers:delete",
        "org_id": "org_123",
        "access_scope": "project",
        "project_id": "proj_456",
        "principal": {"type": "service_account", "id": "svc_789"},
        "federation_rule_id": RULE_ID,
    }
    body.update(overrides)
    return body


def form(request: httpx.Request) -> List[tuple[str, str]]:
    """The form parameters of a token request, in order and with repeats kept."""
    return parse_qsl(request.content.decode(), keep_blank_values=True, strict_parsing=True)


class TokenEndpoint:
    """A respx side effect that issues `access-token-1`, `access-token-2`, ... and records each assertion."""

    def __init__(self, *, expires_in: float = 298) -> None:
        self.expires_in = expires_in
        self.assertions: List[str] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.assertions.append(dict(form(request))["assertion"])
        return httpx.Response(
            200, json=token_response(f"access-token-{len(self.assertions)}", expires_in=self.expires_in)
        )


def counting_identity_tokens(prefix: str = "identity-token") -> Callable[[], str]:
    """An identity token provider that returns a different token on every call."""
    count = 0

    def provider() -> str:
        nonlocal count
        count += 1
        return f"{prefix}-{count}"

    return provider


def bearer(request: httpx.Request) -> Optional[str]:
    value: Optional[str] = request.headers.get("Authorization")
    return value


def requests(route: respx.Route) -> List[httpx.Request]:
    """Every request the route received, oldest first."""
    return [cast(httpx.Request, call.request) for call in cast(Any, route.calls)]


def bearers(route: respx.Route) -> List[Optional[str]]:
    return [bearer(request) for request in requests(route)]
