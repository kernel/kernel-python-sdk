"""Example: authenticate with workload identity federation instead of an API key.

The workload trades a token from its own identity provider for a short-lived
Kernel access token. Each way of supplying that identity token is shown below;
pick the one that matches where the code runs.
"""

import os

import httpx

from kernel import (
    Kernel,
    IdentityTokenFile,
    WorkloadIdentityCredentials,
    exchange_federation_assertion,
)

FEDERATION_RULE_ID = os.environ.get("KERNEL_FEDERATION_RULE_ID", "wifr_...")


def from_environment() -> Kernel:
    # With KERNEL_FEDERATION_RULE_ID set and no KERNEL_API_KEY, the client finds
    # the identity token itself: KERNEL_IDENTITY_TOKEN_SOURCE (github_actions,
    # gcp_metadata, aws_sts, file or env), or KERNEL_IDENTITY_TOKEN_FILE, or a
    # GitHub Actions job with `permissions: id-token: write`.
    return Kernel()


def from_token_file() -> Kernel:
    # A Kubernetes projected service-account token. The file is read again for every exchange.
    return Kernel(
        credentials=WorkloadIdentityCredentials(
            identity_token_provider=IdentityTokenFile("/var/run/secrets/kernel/token"),
            federation_rule_id=FEDERATION_RULE_ID,
        )
    )


def from_callback() -> Kernel:
    def fetch_identity_token() -> str:
        # Called once per exchange. It has to return a newly issued token each
        # time, because most identity providers' tokens can be exchanged only once.
        response = httpx.post("https://idp.internal.example/token", data={"audience": "https://auth.onkernel.com"})
        response.raise_for_status()
        return response.text

    return Kernel(
        credentials=WorkloadIdentityCredentials(
            identity_token_provider=fetch_identity_token,
            federation_rule_id=FEDERATION_RULE_ID,
        )
    )


def one_shot_exchange(identity_token: str) -> None:
    # For callers that want the access token itself. Nothing is cached or refreshed.
    token = exchange_federation_assertion(assertion=identity_token, federation_rule_id=FEDERATION_RULE_ID)
    print("issued to", token.principal, "for project", token.project_id, "until", token.expires_at)


def main() -> None:
    client = from_environment()
    browser = client.browsers.create()
    print("created", browser.session_id)
    client.browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
