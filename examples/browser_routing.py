"""Example: direct-to-VM browser routing for raw HTTP."""

import httpx

from kernel import Kernel


def main() -> None:
    client = Kernel()

    browser = client.browsers.create()

    # Raw browser curl: streams the response. Use for large responses, when you want to stream,
    # or when you want httpx.Response semantics.
    response: httpx.Response = client.browsers.request(browser.session_id, "GET", "https://example.com")
    print("status", response.status_code)

    # Buffered browser curl: returns the full response in a JSON envelope. Use for small responses.
    buffered = client.browsers.curl(browser.session_id, url="https://example.com", method="GET")
    print("body", buffered.body)

    client.browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
