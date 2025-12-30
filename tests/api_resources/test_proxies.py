# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    ProxyListResponse,
    ProxyCheckResponse,
    ProxyCreateResponse,
    ProxyRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        proxy = client.proxies.create(
            type="datacenter",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        proxy = client.proxies.create(
            type="datacenter",
            config={"country": "US"},
            name="name",
            protocol="http",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.proxies.with_raw_response.create(
            type="datacenter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.proxies.with_streaming_response.create(
            type="datacenter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        proxy = client.proxies.retrieve(
            "id",
        )
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.proxies.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.proxies.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.proxies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        proxy = client.proxies.list()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyListResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        proxy = client.proxies.delete(
            "id",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.proxies.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.proxies.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.proxies.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check(self, client: Kernel) -> None:
        proxy = client.proxies.check(
            "id",
        )
        assert_matches_type(ProxyCheckResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: Kernel) -> None:
        response = client.proxies.with_raw_response.check(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyCheckResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: Kernel) -> None:
        with client.proxies.with_streaming_response.check(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyCheckResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_check(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.proxies.with_raw_response.check(
                "",
            )


class TestAsyncProxies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        proxy = await async_client.proxies.create(
            type="datacenter",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        proxy = await async_client.proxies.create(
            type="datacenter",
            config={"country": "US"},
            name="name",
            protocol="http",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxies.with_raw_response.create(
            type="datacenter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.proxies.with_streaming_response.create(
            type="datacenter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        proxy = await async_client.proxies.retrieve(
            "id",
        )
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxies.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.proxies.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.proxies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        proxy = await async_client.proxies.list()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyListResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        proxy = await async_client.proxies.delete(
            "id",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxies.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.proxies.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.proxies.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncKernel) -> None:
        proxy = await async_client.proxies.check(
            "id",
        )
        assert_matches_type(ProxyCheckResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxies.with_raw_response.check(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyCheckResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncKernel) -> None:
        async with async_client.proxies.with_streaming_response.check(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyCheckResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_check(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.proxies.with_raw_response.check(
                "",
            )
