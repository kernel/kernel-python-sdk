# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    def test_method_stream(self, client: Kernel) -> None:
        log_stream = client.browsers.logs.stream(
            id="id",
            source="path",
        )
        log_stream.response.close()

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    def test_method_stream_with_all_params(self, client: Kernel) -> None:
        log_stream = client.browsers.logs.stream(
            id="id",
            source="path",
            follow=True,
            path="path",
            supervisor_process="supervisor_process",
        )
        log_stream.response.close()

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_stream(self, client: Kernel) -> None:
        response = client.browsers.logs.with_raw_response.stream(
            id="id",
            source="path",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_stream(self, client: Kernel) -> None:
        with client.browsers.logs.with_streaming_response.stream(
            id="id",
            source="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    def test_path_params_stream(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.logs.with_raw_response.stream(
                id="",
                source="path",
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    async def test_method_stream(self, async_client: AsyncKernel) -> None:
        log_stream = await async_client.browsers.logs.stream(
            id="id",
            source="path",
        )
        await log_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncKernel) -> None:
        log_stream = await async_client.browsers.logs.stream(
            id="id",
            source="path",
            follow=True,
            path="path",
            supervisor_process="supervisor_process",
        )
        await log_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.logs.with_raw_response.stream(
            id="id",
            source="path",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.logs.with_streaming_response.stream(
            id="id",
            source="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support text/event-stream responses")
    @parametrize
    async def test_path_params_stream(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.logs.with_raw_response.stream(
                id="",
                source="path",
            )
