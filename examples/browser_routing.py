"""Example: direct-to-VM browser routing for process exec and raw HTTP."""

from typing import Any, cast

import httpx

from kernel import Kernel


def main() -> None:
    with Kernel() as client:
        browsers = cast(Any, client.browsers)
        browser = browsers.create(headless=True)
        try:
            response = cast(httpx.Response, browsers.request(browser.session_id, "GET", "https://example.com"))
            print("status", response.status_code)

            with browsers.stream(browser.session_id, "GET", "https://example.com") as streamed:
                print("streamed-bytes", len(streamed.read()))
        finally:
            browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
