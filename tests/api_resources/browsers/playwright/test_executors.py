# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers.playwright import ExecutorList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        executor = client.browsers.playwright.executors.list(
            "htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(ExecutorList, executor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.browsers.playwright.executors.with_raw_response.list(
            "htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        executor = response.parse()
        assert_matches_type(ExecutorList, executor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.browsers.playwright.executors.with_streaming_response.list(
            "htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            executor = response.parse()
            assert_matches_type(ExecutorList, executor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.playwright.executors.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        executor = client.browsers.playwright.executors.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )
        assert executor is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Kernel) -> None:
        executor = client.browsers.playwright.executors.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
            close_tab=True,
        )
        assert executor is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.browsers.playwright.executors.with_raw_response.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        executor = response.parse()
        assert executor is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.browsers.playwright.executors.with_streaming_response.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            executor = response.parse()
            assert executor is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.playwright.executors.with_raw_response.delete(
                name="checkout",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.browsers.playwright.executors.with_raw_response.delete(
                name="",
                id_or_name="htzv5orfit78e1m2biiifpbv",
            )


class TestAsyncExecutors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        executor = await async_client.browsers.playwright.executors.list(
            "htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(ExecutorList, executor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.playwright.executors.with_raw_response.list(
            "htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        executor = await response.parse()
        assert_matches_type(ExecutorList, executor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.playwright.executors.with_streaming_response.list(
            "htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            executor = await response.parse()
            assert_matches_type(ExecutorList, executor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.playwright.executors.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        executor = await async_client.browsers.playwright.executors.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )
        assert executor is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKernel) -> None:
        executor = await async_client.browsers.playwright.executors.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
            close_tab=True,
        )
        assert executor is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.playwright.executors.with_raw_response.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        executor = await response.parse()
        assert executor is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.playwright.executors.with_streaming_response.delete(
            name="checkout",
            id_or_name="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            executor = await response.parse()
            assert executor is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.playwright.executors.with_raw_response.delete(
                name="checkout",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.browsers.playwright.executors.with_raw_response.delete(
                name="",
                id_or_name="htzv5orfit78e1m2biiifpbv",
            )
