# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fetch(self, client: Kernel) -> None:
        content = client.search.contents.fetch(
            id="srch_abc123",
        )
        assert content is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fetch_with_all_params(self, client: Kernel) -> None:
        content = client.search.contents.fetch(
            id="srch_abc123",
            content={
                "browser": {
                    "browser_id": "browser_id",
                    "mode": "curl",
                },
                "format": "markdown",
                "max_age_hours": 0,
                "max_chars": 100,
                "source": "auto",
                "timeout_ms": 1000,
            },
            limit=1,
            result_ids=["string"],
            timeout_ms=1000,
        )
        assert content is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fetch(self, client: Kernel) -> None:
        response = client.search.contents.with_raw_response.fetch(
            id="srch_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert content is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fetch(self, client: Kernel) -> None:
        with client.search.contents.with_streaming_response.fetch(
            id="srch_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert content is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fetch(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.search.contents.with_raw_response.fetch(
                id="",
            )


class TestAsyncContents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fetch(self, async_client: AsyncKernel) -> None:
        content = await async_client.search.contents.fetch(
            id="srch_abc123",
        )
        assert content is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncKernel) -> None:
        content = await async_client.search.contents.fetch(
            id="srch_abc123",
            content={
                "browser": {
                    "browser_id": "browser_id",
                    "mode": "curl",
                },
                "format": "markdown",
                "max_age_hours": 0,
                "max_chars": 100,
                "source": "auto",
                "timeout_ms": 1000,
            },
            limit=1,
            result_ids=["string"],
            timeout_ms=1000,
        )
        assert content is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncKernel) -> None:
        response = await async_client.search.contents.with_raw_response.fetch(
            id="srch_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert content is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncKernel) -> None:
        async with async_client.search.contents.with_streaming_response.fetch(
            id="srch_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert content is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.search.contents.with_raw_response.fetch(
                id="",
            )
