# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from kernel.types.browsers import ReplayListResponse, ReplayStartResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReplays:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        replay = client.browsers.replays.list(
            "id",
        )
        assert_matches_type(ReplayListResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.browsers.replays.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = response.parse()
        assert_matches_type(ReplayListResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.browsers.replays.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = response.parse()
            assert_matches_type(ReplayListResponse, replay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.replays.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/replays/replay_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        replay = client.browsers.replays.download(
            replay_id="replay_id",
            id="id",
        )
        assert replay.is_closed
        assert replay.json() == {"foo": "bar"}
        assert cast(Any, replay.is_closed) is True
        assert isinstance(replay, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/replays/replay_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        replay = client.browsers.replays.with_raw_response.download(
            replay_id="replay_id",
            id="id",
        )

        assert replay.is_closed is True
        assert replay.http_request.headers.get("X-Stainless-Lang") == "python"
        assert replay.json() == {"foo": "bar"}
        assert isinstance(replay, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/replays/replay_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.browsers.replays.with_streaming_response.download(
            replay_id="replay_id",
            id="id",
        ) as replay:
            assert not replay.is_closed
            assert replay.http_request.headers.get("X-Stainless-Lang") == "python"

            assert replay.json() == {"foo": "bar"}
            assert cast(Any, replay.is_closed) is True
            assert isinstance(replay, StreamedBinaryAPIResponse)

        assert cast(Any, replay.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.replays.with_raw_response.download(
                replay_id="replay_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `replay_id` but received ''"):
            client.browsers.replays.with_raw_response.download(
                replay_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Kernel) -> None:
        replay = client.browsers.replays.start(
            id="id",
        )
        assert_matches_type(ReplayStartResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Kernel) -> None:
        replay = client.browsers.replays.start(
            id="id",
            framerate=1,
            max_duration_in_seconds=1,
        )
        assert_matches_type(ReplayStartResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Kernel) -> None:
        response = client.browsers.replays.with_raw_response.start(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = response.parse()
        assert_matches_type(ReplayStartResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Kernel) -> None:
        with client.browsers.replays.with_streaming_response.start(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = response.parse()
            assert_matches_type(ReplayStartResponse, replay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.replays.with_raw_response.start(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Kernel) -> None:
        replay = client.browsers.replays.stop(
            replay_id="replay_id",
            id="id",
        )
        assert replay is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Kernel) -> None:
        response = client.browsers.replays.with_raw_response.stop(
            replay_id="replay_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = response.parse()
        assert replay is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Kernel) -> None:
        with client.browsers.replays.with_streaming_response.stop(
            replay_id="replay_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = response.parse()
            assert replay is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.replays.with_raw_response.stop(
                replay_id="replay_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `replay_id` but received ''"):
            client.browsers.replays.with_raw_response.stop(
                replay_id="",
                id="id",
            )


class TestAsyncReplays:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        replay = await async_client.browsers.replays.list(
            "id",
        )
        assert_matches_type(ReplayListResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.replays.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = await response.parse()
        assert_matches_type(ReplayListResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.replays.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = await response.parse()
            assert_matches_type(ReplayListResponse, replay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.replays.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/replays/replay_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        replay = await async_client.browsers.replays.download(
            replay_id="replay_id",
            id="id",
        )
        assert replay.is_closed
        assert await replay.json() == {"foo": "bar"}
        assert cast(Any, replay.is_closed) is True
        assert isinstance(replay, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/replays/replay_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        replay = await async_client.browsers.replays.with_raw_response.download(
            replay_id="replay_id",
            id="id",
        )

        assert replay.is_closed is True
        assert replay.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await replay.json() == {"foo": "bar"}
        assert isinstance(replay, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/replays/replay_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.browsers.replays.with_streaming_response.download(
            replay_id="replay_id",
            id="id",
        ) as replay:
            assert not replay.is_closed
            assert replay.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await replay.json() == {"foo": "bar"}
            assert cast(Any, replay.is_closed) is True
            assert isinstance(replay, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, replay.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.replays.with_raw_response.download(
                replay_id="replay_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `replay_id` but received ''"):
            await async_client.browsers.replays.with_raw_response.download(
                replay_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncKernel) -> None:
        replay = await async_client.browsers.replays.start(
            id="id",
        )
        assert_matches_type(ReplayStartResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncKernel) -> None:
        replay = await async_client.browsers.replays.start(
            id="id",
            framerate=1,
            max_duration_in_seconds=1,
        )
        assert_matches_type(ReplayStartResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.replays.with_raw_response.start(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = await response.parse()
        assert_matches_type(ReplayStartResponse, replay, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.replays.with_streaming_response.start(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = await response.parse()
            assert_matches_type(ReplayStartResponse, replay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.replays.with_raw_response.start(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncKernel) -> None:
        replay = await async_client.browsers.replays.stop(
            replay_id="replay_id",
            id="id",
        )
        assert replay is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.replays.with_raw_response.stop(
            replay_id="replay_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replay = await response.parse()
        assert replay is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.replays.with_streaming_response.stop(
            replay_id="replay_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replay = await response.parse()
            assert replay is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.replays.with_raw_response.stop(
                replay_id="replay_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `replay_id` but received ''"):
            await async_client.browsers.replays.with_raw_response.stop(
                replay_id="",
                id="id",
            )
