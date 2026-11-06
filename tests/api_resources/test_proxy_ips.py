# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import ProxyIP, ProxyIPDetail
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxyIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        proxy_ip = client.proxy_ips.retrieve(
            "ip_address",
        )
        assert_matches_type(ProxyIPDetail, proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.proxy_ips.with_raw_response.retrieve(
            "ip_address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_ip = response.parse()
        assert_matches_type(ProxyIPDetail, proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.proxy_ips.with_streaming_response.retrieve(
            "ip_address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_ip = response.parse()
            assert_matches_type(ProxyIPDetail, proxy_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            client.proxy_ips.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        proxy_ip = client.proxy_ips.list()
        assert_matches_type(SyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        proxy_ip = client.proxy_ips.list(
            country="country",
            limit=1,
            offset=0,
            status="active",
        )
        assert_matches_type(SyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.proxy_ips.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_ip = response.parse()
        assert_matches_type(SyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.proxy_ips.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_ip = response.parse()
            assert_matches_type(SyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProxyIPs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        proxy_ip = await async_client.proxy_ips.retrieve(
            "ip_address",
        )
        assert_matches_type(ProxyIPDetail, proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxy_ips.with_raw_response.retrieve(
            "ip_address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_ip = await response.parse()
        assert_matches_type(ProxyIPDetail, proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.proxy_ips.with_streaming_response.retrieve(
            "ip_address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_ip = await response.parse()
            assert_matches_type(ProxyIPDetail, proxy_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            await async_client.proxy_ips.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        proxy_ip = await async_client.proxy_ips.list()
        assert_matches_type(AsyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        proxy_ip = await async_client.proxy_ips.list(
            country="country",
            limit=1,
            offset=0,
            status="active",
        )
        assert_matches_type(AsyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.proxy_ips.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_ip = await response.parse()
        assert_matches_type(AsyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.proxy_ips.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_ip = await response.parse()
            assert_matches_type(AsyncOffsetPagination[ProxyIP], proxy_ip, path=["response"])

        assert cast(Any, response.is_closed) is True
