"""Example: direct-to-VM browser routing for raw HTTP."""

import httpx

from kernel import Kernel


def main() -> None:
    client = Kernel()

    browser = client.browsers.create()
    response: httpx.Response = client.browsers.request(browser.session_id, "GET", "https://example.com")
    print("status", response.status_code)

    client.browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
