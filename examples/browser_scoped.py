"""Example: browser-scoped client for metro-backed process and raw HTTP."""

from kernel import Kernel

# After creating or loading a browser session (with base_url + cdp_ws_url from the API):
# browser = client.browsers.create(...)
# scoped = client.for_browser(browser)
# scoped.process.exec(command="uname", args=["-a"])
# r = scoped.request("GET", "https://example.com")
# with scoped.stream("GET", "https://example.com") as resp:
#     print(resp.read())


def main() -> None:
    _ = Kernel


if __name__ == "__main__":
    main()
