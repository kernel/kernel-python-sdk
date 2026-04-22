"""Example: direct-to-VM browser routing for process exec and raw HTTP."""

from kernel import BrowserRoutingConfig, Kernel


def main() -> None:
    with Kernel(browser_routing=BrowserRoutingConfig(enabled=True, direct_to_vm_subresources=("process",))) as client:
        browser = client.browsers.create(headless=True)
        try:
            client.browsers.process.exec(browser.session_id, command="uname", args=["-a"])

            response = client.browsers.request(browser.session_id, "GET", "https://example.com")
            print("status", response.status_code)

            with client.browsers.stream(browser.session_id, "GET", "https://example.com") as streamed:
                print("streamed-bytes", len(streamed.read()))
        finally:
            client.browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
