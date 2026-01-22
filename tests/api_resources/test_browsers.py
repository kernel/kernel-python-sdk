# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    BrowserListResponse,
    BrowserCreateResponse,
    BrowserUpdateResponse,
    BrowserRetrieveResponse,
)
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        browser = client.browsers.create()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        browser = client.browsers.create(
            extensions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            headless=False,
            invocation_id="rr33xuugxj9h0bkf1rdt2bet",
            kiosk_mode=True,
            persistence={"id": "my-awesome-browser-for-user-1234"},
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            stealth=True,
            timeout_seconds=10,
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserCreateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        browser = client.browsers.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Kernel) -> None:
        browser = client.browsers.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
            include_deleted=True,
        )
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        browser = client.browsers.update(
            id="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        browser = client.browsers.update(
            id="htzv5orfit78e1m2biiifpbv",
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.update(
            id="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.update(
            id="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        browser = client.browsers.list()
        assert_matches_type(SyncOffsetPagination[BrowserListResponse], browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        browser = client.browsers.list(
            include_deleted=True,
            limit=1,
            offset=0,
            status="active",
        )
        assert_matches_type(SyncOffsetPagination[BrowserListResponse], browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(SyncOffsetPagination[BrowserListResponse], browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(SyncOffsetPagination[BrowserListResponse], browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        with pytest.warns(DeprecationWarning):
            browser = client.browsers.delete(
                persistent_id="persistent_id",
            )

        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.browsers.with_raw_response.delete(
                persistent_id="persistent_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with pytest.warns(DeprecationWarning):
            with client.browsers.with_streaming_response.delete(
                persistent_id="persistent_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                browser = response.parse()
                assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_id(self, client: Kernel) -> None:
        browser = client.browsers.delete_by_id(
            "htzv5orfit78e1m2biiifpbv",
        )
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_by_id(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.delete_by_id(
            "htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_id(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.delete_by_id(
            "htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_by_id(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.with_raw_response.delete_by_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_load_extensions(self, client: Kernel) -> None:
        browser = client.browsers.load_extensions(
            id="id",
            extensions=[
                {
                    "name": "name",
                    "zip_file": b"raw file contents",
                }
            ],
        )
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_load_extensions(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.load_extensions(
            id="id",
            extensions=[
                {
                    "name": "name",
                    "zip_file": b"raw file contents",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_load_extensions(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.load_extensions(
            id="id",
            extensions=[
                {
                    "name": "name",
                    "zip_file": b"raw file contents",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_load_extensions(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.with_raw_response.load_extensions(
                id="",
                extensions=[
                    {
                        "name": "name",
                        "zip_file": b"raw file contents",
                    }
                ],
            )


class TestAsyncBrowsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.create()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.create(
            extensions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            headless=False,
            invocation_id="rr33xuugxj9h0bkf1rdt2bet",
            kiosk_mode=True,
            persistence={"id": "my-awesome-browser-for-user-1234"},
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            stealth=True,
            timeout_seconds=10,
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserCreateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
            include_deleted=True,
        )
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.retrieve(
            id="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.update(
            id="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.update(
            id="htzv5orfit78e1m2biiifpbv",
            profile={
                "id": "id",
                "name": "name",
                "save_changes": True,
            },
            proxy_id="proxy_id",
            viewport={
                "height": 800,
                "width": 1280,
                "refresh_rate": 60,
            },
        )
        assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.update(
            id="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.update(
            id="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserUpdateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.list()
        assert_matches_type(AsyncOffsetPagination[BrowserListResponse], browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.list(
            include_deleted=True,
            limit=1,
            offset=0,
            status="active",
        )
        assert_matches_type(AsyncOffsetPagination[BrowserListResponse], browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(AsyncOffsetPagination[BrowserListResponse], browser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(AsyncOffsetPagination[BrowserListResponse], browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        with pytest.warns(DeprecationWarning):
            browser = await async_client.browsers.delete(
                persistent_id="persistent_id",
            )

        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.browsers.with_raw_response.delete(
                persistent_id="persistent_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.browsers.with_streaming_response.delete(
                persistent_id="persistent_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                browser = await response.parse()
                assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.delete_by_id(
            "htzv5orfit78e1m2biiifpbv",
        )
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.delete_by_id(
            "htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.delete_by_id(
            "htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.with_raw_response.delete_by_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_load_extensions(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.load_extensions(
            id="id",
            extensions=[
                {
                    "name": "name",
                    "zip_file": b"raw file contents",
                }
            ],
        )
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_load_extensions(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.load_extensions(
            id="id",
            extensions=[
                {
                    "name": "name",
                    "zip_file": b"raw file contents",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_load_extensions(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.load_extensions(
            id="id",
            extensions=[
                {
                    "name": "name",
                    "zip_file": b"raw file contents",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_load_extensions(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.with_raw_response.load_extensions(
                id="",
                extensions=[
                    {
                        "name": "name",
                        "zip_file": b"raw file contents",
                    }
                ],
            )
