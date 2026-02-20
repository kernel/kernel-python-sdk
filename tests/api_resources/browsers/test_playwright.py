# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers import PlaywrightExecuteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlaywright:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: Kernel) -> None:
        playwright = client.browsers.playwright.execute(
            id="id",
            code="code",
        )
        assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Kernel) -> None:
        playwright = client.browsers.playwright.execute(
            id="id",
            code="code",
            timeout_sec=1,
        )
        assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Kernel) -> None:
        response = client.browsers.playwright.with_raw_response.execute(
            id="id",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playwright = response.parse()
        assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Kernel) -> None:
        with client.browsers.playwright.with_streaming_response.execute(
            id="id",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playwright = response.parse()
            assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.playwright.with_raw_response.execute(
                id="",
                code="code",
            )


class TestAsyncPlaywright:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncKernel) -> None:
        playwright = await async_client.browsers.playwright.execute(
            id="id",
            code="code",
        )
        assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncKernel) -> None:
        playwright = await async_client.browsers.playwright.execute(
            id="id",
            code="code",
            timeout_sec=1,
        )
        assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.playwright.with_raw_response.execute(
            id="id",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playwright = await response.parse()
        assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.playwright.with_streaming_response.execute(
            id="id",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playwright = await response.parse()
            assert_matches_type(PlaywrightExecuteResponse, playwright, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.playwright.with_raw_response.execute(
                id="",
                code="code",
            )
