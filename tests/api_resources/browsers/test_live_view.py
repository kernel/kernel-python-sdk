# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers import BrowserLiveView

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiveView:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        live_view = client.browsers.live_view.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(BrowserLiveView, live_view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        live_view = client.browsers.live_view.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            scope="read",
            ttl_seconds=3600,
        )
        assert_matches_type(BrowserLiveView, live_view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.browsers.live_view.with_raw_response.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_view = response.parse()
        assert_matches_type(BrowserLiveView, live_view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.browsers.live_view.with_streaming_response.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_view = response.parse()
            assert_matches_type(BrowserLiveView, live_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.live_view.with_raw_response.create(
                id_or_name="",
            )


class TestAsyncLiveView:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        live_view = await async_client.browsers.live_view.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(BrowserLiveView, live_view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        live_view = await async_client.browsers.live_view.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            scope="read",
            ttl_seconds=3600,
        )
        assert_matches_type(BrowserLiveView, live_view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.live_view.with_raw_response.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_view = await response.parse()
        assert_matches_type(BrowserLiveView, live_view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.live_view.with_streaming_response.create(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_view = await response.parse()
            assert_matches_type(BrowserLiveView, live_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.live_view.with_raw_response.create(
                id_or_name="",
            )
