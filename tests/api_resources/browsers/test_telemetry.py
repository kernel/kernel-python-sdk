# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination
from kernel.types.browsers import TelemetryEventsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events(self, client: Kernel) -> None:
        telemetry = client.browsers.telemetry.events(
            id="id",
        )
        assert_matches_type(SyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events_with_all_params(self, client: Kernel) -> None:
        telemetry = client.browsers.telemetry.events(
            id="id",
            category=["console"],
            limit=1,
            offset=0,
            since="since",
            until="until",
        )
        assert_matches_type(SyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_events(self, client: Kernel) -> None:
        response = client.browsers.telemetry.with_raw_response.events(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(SyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_events(self, client: Kernel) -> None:
        with client.browsers.telemetry.with_streaming_response.events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(SyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_events(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.telemetry.with_raw_response.events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Kernel) -> None:
        telemetry_stream = client.browsers.telemetry.stream(
            id="id",
        )
        telemetry_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Kernel) -> None:
        telemetry_stream = client.browsers.telemetry.stream(
            id="id",
            replay="replay",
            last_event_id="Last-Event-ID",
        )
        telemetry_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Kernel) -> None:
        response = client.browsers.telemetry.with_raw_response.stream(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Kernel) -> None:
        with client.browsers.telemetry.with_streaming_response.stream(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.telemetry.with_raw_response.stream(
                id="",
            )


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events(self, async_client: AsyncKernel) -> None:
        telemetry = await async_client.browsers.telemetry.events(
            id="id",
        )
        assert_matches_type(AsyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncKernel) -> None:
        telemetry = await async_client.browsers.telemetry.events(
            id="id",
            category=["console"],
            limit=1,
            offset=0,
            since="since",
            until="until",
        )
        assert_matches_type(AsyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.telemetry.with_raw_response.events(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(AsyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.telemetry.with_streaming_response.events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(AsyncOffsetPagination[TelemetryEventsResponse], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_events(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.telemetry.with_raw_response.events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncKernel) -> None:
        telemetry_stream = await async_client.browsers.telemetry.stream(
            id="id",
        )
        await telemetry_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncKernel) -> None:
        telemetry_stream = await async_client.browsers.telemetry.stream(
            id="id",
            replay="replay",
            last_event_id="Last-Event-ID",
        )
        await telemetry_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.telemetry.with_raw_response.stream(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.telemetry.with_streaming_response.stream(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.telemetry.with_raw_response.stream(
                id="",
            )
