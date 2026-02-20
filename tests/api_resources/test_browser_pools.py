# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    BrowserPool,
    BrowserPoolListResponse,
    BrowserPoolAcquireResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowserPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.create(
            size=10,
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.create(
            size=10,
            extensions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            fill_rate_per_minute=0,
            headless=False,
            kiosk_mode=True,
            name="my-pool",
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            stealth=True,
            timeout_seconds=60,
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.create(
            size=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.create(
            size=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert_matches_type(BrowserPool, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.retrieve(
            "id_or_name",
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.retrieve(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.retrieve(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert_matches_type(BrowserPool, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browser_pools.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.update(
            id_or_name="id_or_name",
            size=10,
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.update(
            id_or_name="id_or_name",
            size=10,
            discard_all_idle=False,
            extensions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            fill_rate_per_minute=0,
            headless=False,
            kiosk_mode=True,
            name="my-pool",
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            stealth=True,
            timeout_seconds=60,
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.update(
            id_or_name="id_or_name",
            size=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.update(
            id_or_name="id_or_name",
            size=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert_matches_type(BrowserPool, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browser_pools.with_raw_response.update(
                id_or_name="",
                size=10,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.list()
        assert_matches_type(BrowserPoolListResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert_matches_type(BrowserPoolListResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert_matches_type(BrowserPoolListResponse, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.delete(
            id_or_name="id_or_name",
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.delete(
            id_or_name="id_or_name",
            force=True,
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.delete(
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.delete(
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert browser_pool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browser_pools.with_raw_response.delete(
                id_or_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_acquire(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.acquire(
            id_or_name="id_or_name",
        )
        assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_acquire_with_all_params(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.acquire(
            id_or_name="id_or_name",
            acquire_timeout_seconds=0,
        )
        assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_acquire(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.acquire(
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_acquire(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.acquire(
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_acquire(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browser_pools.with_raw_response.acquire(
                id_or_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flush(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.flush(
            "id_or_name",
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_flush(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.flush(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_flush(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.flush(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert browser_pool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_flush(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browser_pools.with_raw_response.flush(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_release(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_release_with_all_params(self, client: Kernel) -> None:
        browser_pool = client.browser_pools.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
            reuse=False,
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_release(self, client: Kernel) -> None:
        response = client.browser_pools.with_raw_response.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = response.parse()
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_release(self, client: Kernel) -> None:
        with client.browser_pools.with_streaming_response.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = response.parse()
            assert browser_pool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_release(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browser_pools.with_raw_response.release(
                id_or_name="",
                session_id="ts8iy3sg25ibheguyni2lg9t",
            )


class TestAsyncBrowserPools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.create(
            size=10,
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.create(
            size=10,
            extensions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            fill_rate_per_minute=0,
            headless=False,
            kiosk_mode=True,
            name="my-pool",
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            stealth=True,
            timeout_seconds=60,
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.create(
            size=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.create(
            size=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert_matches_type(BrowserPool, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.retrieve(
            "id_or_name",
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.retrieve(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.retrieve(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert_matches_type(BrowserPool, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browser_pools.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.update(
            id_or_name="id_or_name",
            size=10,
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.update(
            id_or_name="id_or_name",
            size=10,
            discard_all_idle=False,
            extensions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            fill_rate_per_minute=0,
            headless=False,
            kiosk_mode=True,
            name="my-pool",
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            stealth=True,
            timeout_seconds=60,
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.update(
            id_or_name="id_or_name",
            size=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert_matches_type(BrowserPool, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.update(
            id_or_name="id_or_name",
            size=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert_matches_type(BrowserPool, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browser_pools.with_raw_response.update(
                id_or_name="",
                size=10,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.list()
        assert_matches_type(BrowserPoolListResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert_matches_type(BrowserPoolListResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert_matches_type(BrowserPoolListResponse, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.delete(
            id_or_name="id_or_name",
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.delete(
            id_or_name="id_or_name",
            force=True,
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.delete(
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.delete(
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert browser_pool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browser_pools.with_raw_response.delete(
                id_or_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_acquire(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.acquire(
            id_or_name="id_or_name",
        )
        assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_acquire_with_all_params(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.acquire(
            id_or_name="id_or_name",
            acquire_timeout_seconds=0,
        )
        assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_acquire(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.acquire(
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_acquire(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.acquire(
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert_matches_type(BrowserPoolAcquireResponse, browser_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_acquire(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browser_pools.with_raw_response.acquire(
                id_or_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flush(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.flush(
            "id_or_name",
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_flush(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.flush(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_flush(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.flush(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert browser_pool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_flush(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browser_pools.with_raw_response.flush(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_release(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_release_with_all_params(self, async_client: AsyncKernel) -> None:
        browser_pool = await async_client.browser_pools.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
            reuse=False,
        )
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_release(self, async_client: AsyncKernel) -> None:
        response = await async_client.browser_pools.with_raw_response.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_pool = await response.parse()
        assert browser_pool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncKernel) -> None:
        async with async_client.browser_pools.with_streaming_response.release(
            id_or_name="id_or_name",
            session_id="ts8iy3sg25ibheguyni2lg9t",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_pool = await response.parse()
            assert browser_pool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_release(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browser_pools.with_raw_response.release(
                id_or_name="",
                session_id="ts8iy3sg25ibheguyni2lg9t",
            )
