"""Example: browser-scoped client for browser VM process exec and raw HTTP."""

from kernel import Kernel


def main() -> None:
    with Kernel() as client:
        browser = client.browsers.create(headless=True)
        try:
            scoped = client.for_browser(browser)

            scoped.process.exec(command="uname", args=["-a"])

            response = scoped.request("GET", "https://example.com")
            print("status", response.status_code)

            with scoped.stream("GET", "https://example.com") as streamed:
                print("streamed-bytes", len(streamed.read()))
        finally:
            client.browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
