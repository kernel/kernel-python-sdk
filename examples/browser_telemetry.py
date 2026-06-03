"""Example: stream live browser telemetry events from a session."""

from kernel import Kernel


def main() -> None:
    client = Kernel()

    # Enable telemetry capture when creating the browser.
    browser = client.browsers.create(telemetry={"enabled": True})

    try:
        # Telemetry is a default direct-to-VM routing subresource, so the stream
        # connects straight to the browser VM automatically.
        stream = client.browsers.telemetry.stream(browser.session_id)

        # Make a few browser activity calls to generate events. The "api" telemetry
        # category emits an event per VM API call, so events arrive within ~1s.
        for _ in range(3):
            client.browsers.curl(browser.session_id, url="https://example.com", method="GET")

        # Print a few events, then stop so we don't wait on the 15s keepalive.
        for count, message in enumerate(stream, start=1):
            print(message.seq, message.event.type)
            if count >= 3:
                break
    finally:
        client.browsers.delete_by_id(browser.session_id)


if __name__ == "__main__":
    main()
