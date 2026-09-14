# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    LookupResponse,
    RecommendationSummary,
    ConfigRegistryResponse,
)
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigRegistry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        config_registry = client.config_registry.list()
        assert_matches_type(SyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        config_registry = client.config_registry.list(
            limit=1,
            offset=0,
            search="search",
            sort_by="target",
            sort_order="asc",
        )
        assert_matches_type(SyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.config_registry.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_registry = response.parse()
        assert_matches_type(SyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.config_registry.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_registry = response.parse()
            assert_matches_type(SyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: Kernel) -> None:
        config_registry = client.config_registry.lookup(
            url="https://example.com",
        )
        assert_matches_type(LookupResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_with_all_params(self, client: Kernel) -> None:
        config_registry = client.config_registry.lookup(
            url="https://example.com",
            allowed_proxy_countries=["US"],
        )
        assert_matches_type(LookupResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: Kernel) -> None:
        response = client.config_registry.with_raw_response.lookup(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_registry = response.parse()
        assert_matches_type(LookupResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: Kernel) -> None:
        with client.config_registry.with_streaming_response.lookup(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_registry = response.parse()
            assert_matches_type(LookupResponse, config_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve(self, client: Kernel) -> None:
        config_registry = client.config_registry.resolve(
            url="https://example.com",
        )
        assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve_with_all_params(self, client: Kernel) -> None:
        config_registry = client.config_registry.resolve(
            url="https://example.com",
            allowed_proxy_countries=["US"],
            intent="search for a black hoodie and add it to the cart",
        )
        assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resolve(self, client: Kernel) -> None:
        response = client.config_registry.with_raw_response.resolve(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_registry = response.parse()
        assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resolve(self, client: Kernel) -> None:
        with client.config_registry.with_streaming_response.resolve(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_registry = response.parse()
            assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigRegistry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        config_registry = await async_client.config_registry.list()
        assert_matches_type(AsyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        config_registry = await async_client.config_registry.list(
            limit=1,
            offset=0,
            search="search",
            sort_by="target",
            sort_order="asc",
        )
        assert_matches_type(AsyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.config_registry.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_registry = await response.parse()
        assert_matches_type(AsyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.config_registry.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_registry = await response.parse()
            assert_matches_type(AsyncOffsetPagination[RecommendationSummary], config_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncKernel) -> None:
        config_registry = await async_client.config_registry.lookup(
            url="https://example.com",
        )
        assert_matches_type(LookupResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncKernel) -> None:
        config_registry = await async_client.config_registry.lookup(
            url="https://example.com",
            allowed_proxy_countries=["US"],
        )
        assert_matches_type(LookupResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncKernel) -> None:
        response = await async_client.config_registry.with_raw_response.lookup(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_registry = await response.parse()
        assert_matches_type(LookupResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncKernel) -> None:
        async with async_client.config_registry.with_streaming_response.lookup(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_registry = await response.parse()
            assert_matches_type(LookupResponse, config_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve(self, async_client: AsyncKernel) -> None:
        config_registry = await async_client.config_registry.resolve(
            url="https://example.com",
        )
        assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncKernel) -> None:
        config_registry = await async_client.config_registry.resolve(
            url="https://example.com",
            allowed_proxy_countries=["US"],
            intent="search for a black hoodie and add it to the cart",
        )
        assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncKernel) -> None:
        response = await async_client.config_registry.with_raw_response.resolve(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_registry = await response.parse()
        assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncKernel) -> None:
        async with async_client.config_registry.with_streaming_response.resolve(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_registry = await response.parse()
            assert_matches_type(ConfigRegistryResponse, config_registry, path=["response"])

        assert cast(Any, response.is_closed) is True
