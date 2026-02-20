# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers.fs import WatchStartResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events(self, client: Kernel) -> None:
        watch_stream = client.browsers.fs.watch.events(
            watch_id="watch_id",
            id="id",
        )
        watch_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_events(self, client: Kernel) -> None:
        response = client.browsers.fs.watch.with_raw_response.events(
            watch_id="watch_id",
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_events(self, client: Kernel) -> None:
        with client.browsers.fs.watch.with_streaming_response.events(
            watch_id="watch_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_events(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.watch.with_raw_response.events(
                watch_id="watch_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watch_id` but received ''"):
            client.browsers.fs.watch.with_raw_response.events(
                watch_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Kernel) -> None:
        watch = client.browsers.fs.watch.start(
            id="id",
            path="path",
        )
        assert_matches_type(WatchStartResponse, watch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Kernel) -> None:
        watch = client.browsers.fs.watch.start(
            id="id",
            path="path",
            recursive=True,
        )
        assert_matches_type(WatchStartResponse, watch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Kernel) -> None:
        response = client.browsers.fs.watch.with_raw_response.start(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = response.parse()
        assert_matches_type(WatchStartResponse, watch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Kernel) -> None:
        with client.browsers.fs.watch.with_streaming_response.start(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = response.parse()
            assert_matches_type(WatchStartResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.watch.with_raw_response.start(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Kernel) -> None:
        watch = client.browsers.fs.watch.stop(
            watch_id="watch_id",
            id="id",
        )
        assert watch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Kernel) -> None:
        response = client.browsers.fs.watch.with_raw_response.stop(
            watch_id="watch_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = response.parse()
        assert watch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Kernel) -> None:
        with client.browsers.fs.watch.with_streaming_response.stop(
            watch_id="watch_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = response.parse()
            assert watch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.watch.with_raw_response.stop(
                watch_id="watch_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watch_id` but received ''"):
            client.browsers.fs.watch.with_raw_response.stop(
                watch_id="",
                id="id",
            )


class TestAsyncWatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events(self, async_client: AsyncKernel) -> None:
        watch_stream = await async_client.browsers.fs.watch.events(
            watch_id="watch_id",
            id="id",
        )
        await watch_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.watch.with_raw_response.events(
            watch_id="watch_id",
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.watch.with_streaming_response.events(
            watch_id="watch_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_events(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.watch.with_raw_response.events(
                watch_id="watch_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watch_id` but received ''"):
            await async_client.browsers.fs.watch.with_raw_response.events(
                watch_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncKernel) -> None:
        watch = await async_client.browsers.fs.watch.start(
            id="id",
            path="path",
        )
        assert_matches_type(WatchStartResponse, watch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncKernel) -> None:
        watch = await async_client.browsers.fs.watch.start(
            id="id",
            path="path",
            recursive=True,
        )
        assert_matches_type(WatchStartResponse, watch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.watch.with_raw_response.start(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = await response.parse()
        assert_matches_type(WatchStartResponse, watch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.watch.with_streaming_response.start(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = await response.parse()
            assert_matches_type(WatchStartResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.watch.with_raw_response.start(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncKernel) -> None:
        watch = await async_client.browsers.fs.watch.stop(
            watch_id="watch_id",
            id="id",
        )
        assert watch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.watch.with_raw_response.stop(
            watch_id="watch_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = await response.parse()
        assert watch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.watch.with_streaming_response.stop(
            watch_id="watch_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = await response.parse()
            assert watch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.watch.with_raw_response.stop(
                watch_id="watch_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `watch_id` but received ''"):
            await async_client.browsers.fs.watch.with_raw_response.stop(
                watch_id="",
                id="id",
            )
