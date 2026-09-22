# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.search import ProviderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        provider = client.search.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        provider = client.search.providers.list(
            slug="brave",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.search.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.search.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        provider = await async_client.search.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        provider = await async_client.search.providers.list(
            slug="brave",
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.search.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.search.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True
