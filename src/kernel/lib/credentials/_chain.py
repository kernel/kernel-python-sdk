from __future__ import annotations

import os
import hashlib
import threading
from typing import Dict, Optional

from ._types import IdentityTokenProvider
from ._errors import WorkloadIdentityError
from ._workload import WorkloadIdentityCredentials
from ._constants import (
    ENV_IDENTITY_TOKEN,
    ENV_FEDERATION_RULE_ID,
    ENV_GITHUB_REQUEST_URL,
    ENV_IDENTITY_TOKEN_FILE,
    ENV_IDENTITY_TOKEN_SOURCE,
)
from ._providers import (
    IdentityTokenFile,
    AWSSTSIdentityToken,
    StaticIdentityToken,
    GCPMetadataIdentityToken,
    GitHubActionsIdentityToken,
)

__all__ = ["default_credentials", "has_federation_env"]

_SOURCES = ("github_actions", "gcp_metadata", "aws_sts", "file", "env")

# One single-use wrapper per literal value, so that every client resolved from
# the same KERNEL_IDENTITY_TOKEN shares its one exchange instead of each
# sending the token again. Keyed by a digest, so the map holds no tokens.
_env_tokens: Dict[str, StaticIdentityToken] = {}
_env_tokens_lock = threading.Lock()


def _static_token_from_env(value: str) -> StaticIdentityToken:
    key = hashlib.sha256(value.strip().encode("utf-8")).hexdigest()
    with _env_tokens_lock:
        provider = _env_tokens.get(key)
        if provider is None:
            provider = _env_tokens[key] = StaticIdentityToken(value)
        return provider


def has_federation_env() -> bool:
    return bool(os.environ.get(ENV_FEDERATION_RULE_ID))


def _require_env(name: str, *, source: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise WorkloadIdentityError(f"{ENV_IDENTITY_TOKEN_SOURCE}={source} needs {name} to be set.")
    return value


def _identity_token_provider_from_env() -> IdentityTokenProvider:
    source = (os.environ.get(ENV_IDENTITY_TOKEN_SOURCE) or "").strip().lower()

    if not source:
        # A file wins over a literal value; GitHub Actions is detected last.
        if os.environ.get(ENV_IDENTITY_TOKEN_FILE):
            source = "file"
        elif os.environ.get(ENV_IDENTITY_TOKEN):
            source = "env"
        elif os.environ.get(ENV_GITHUB_REQUEST_URL):
            source = "github_actions"
        else:
            hint = ""
            if os.environ.get("GITHUB_ACTIONS") == "true":
                hint = " In GitHub Actions, add `permissions: id-token: write` to the workflow or job."
            raise WorkloadIdentityError(
                f"{ENV_FEDERATION_RULE_ID} is set but no identity token source was found. Set "
                f"{ENV_IDENTITY_TOKEN_SOURCE} to one of {', '.join(_SOURCES)}, or set "
                f"{ENV_IDENTITY_TOKEN_FILE} or {ENV_IDENTITY_TOKEN}.{hint}"
            )

    if source == "file":
        return IdentityTokenFile(_require_env(ENV_IDENTITY_TOKEN_FILE, source=source))
    if source == "env":
        return _static_token_from_env(_require_env(ENV_IDENTITY_TOKEN, source=source))
    if source == "github_actions":
        GitHubActionsIdentityToken.require_available()
        return GitHubActionsIdentityToken()
    if source == "gcp_metadata":
        return GCPMetadataIdentityToken()
    if source == "aws_sts":
        return AWSSTSIdentityToken()
    raise WorkloadIdentityError(
        f"{ENV_IDENTITY_TOKEN_SOURCE}={source!r} is not a known identity token source. "
        f"Use one of {', '.join(_SOURCES)}."
    )


def default_credentials() -> Optional[WorkloadIdentityCredentials]:
    """Workload identity credentials from the environment, or `None` when federation is not configured.

    Federation is configured when `KERNEL_FEDERATION_RULE_ID` is set. The
    identity token then comes from `KERNEL_IDENTITY_TOKEN_SOURCE`
    (`github_actions`, `gcp_metadata`, `aws_sts`, `file` or `env`). With no
    source set it is `KERNEL_IDENTITY_TOKEN_FILE`, then `KERNEL_IDENTITY_TOKEN`,
    then GitHub Actions when the job can request an identity token. A rule ID
    with no usable source raises.

    The client does not call this when it has an API key, including one from
    `KERNEL_API_KEY`.
    """
    federation_rule_id = os.environ.get(ENV_FEDERATION_RULE_ID)
    if not federation_rule_id:
        return None
    return WorkloadIdentityCredentials(
        identity_token_provider=_identity_token_provider_from_env(),
        federation_rule_id=federation_rule_id,
    )
