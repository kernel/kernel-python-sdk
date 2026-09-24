# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers.webmcp import CustomToolsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        custom_tool = client.browsers.webmcp.custom_tools.list(
            "id_or_name",
        )
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.browsers.webmcp.custom_tools.with_raw_response.list(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_tool = response.parse()
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.browsers.webmcp.custom_tools.with_streaming_response.list(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_tool = response.parse()
            assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.webmcp.custom_tools.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Kernel) -> None:
        custom_tool = client.browsers.webmcp.custom_tools.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
        )
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Kernel) -> None:
        custom_tool = client.browsers.webmcp.custom_tools.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
            force_overwrite_namespace=True,
        )
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Kernel) -> None:
        response = client.browsers.webmcp.custom_tools.with_raw_response.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_tool = response.parse()
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Kernel) -> None:
        with client.browsers.webmcp.custom_tools.with_streaming_response.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_tool = response.parse()
            assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.webmcp.custom_tools.with_raw_response.add(
                id_or_name="",
                namespace="namespace",
                source="source",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Kernel) -> None:
        custom_tool = client.browsers.webmcp.custom_tools.remove(
            id="ct_n10b9798ad53ecc4y69z31e1",
            id_or_name="id_or_name",
        )
        assert custom_tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Kernel) -> None:
        response = client.browsers.webmcp.custom_tools.with_raw_response.remove(
            id="ct_n10b9798ad53ecc4y69z31e1",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_tool = response.parse()
        assert custom_tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Kernel) -> None:
        with client.browsers.webmcp.custom_tools.with_streaming_response.remove(
            id="ct_n10b9798ad53ecc4y69z31e1",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_tool = response.parse()
            assert custom_tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.webmcp.custom_tools.with_raw_response.remove(
                id="ct_n10b9798ad53ecc4y69z31e1",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.webmcp.custom_tools.with_raw_response.remove(
                id="",
                id_or_name="id_or_name",
            )


class TestAsyncCustomTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        custom_tool = await async_client.browsers.webmcp.custom_tools.list(
            "id_or_name",
        )
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.webmcp.custom_tools.with_raw_response.list(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_tool = await response.parse()
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.webmcp.custom_tools.with_streaming_response.list(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_tool = await response.parse()
            assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.webmcp.custom_tools.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncKernel) -> None:
        custom_tool = await async_client.browsers.webmcp.custom_tools.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
        )
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncKernel) -> None:
        custom_tool = await async_client.browsers.webmcp.custom_tools.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
            force_overwrite_namespace=True,
        )
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.webmcp.custom_tools.with_raw_response.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_tool = await response.parse()
        assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.webmcp.custom_tools.with_streaming_response.add(
            id_or_name="id_or_name",
            namespace="namespace",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_tool = await response.parse()
            assert_matches_type(CustomToolsResponse, custom_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.webmcp.custom_tools.with_raw_response.add(
                id_or_name="",
                namespace="namespace",
                source="source",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncKernel) -> None:
        custom_tool = await async_client.browsers.webmcp.custom_tools.remove(
            id="ct_n10b9798ad53ecc4y69z31e1",
            id_or_name="id_or_name",
        )
        assert custom_tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.webmcp.custom_tools.with_raw_response.remove(
            id="ct_n10b9798ad53ecc4y69z31e1",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_tool = await response.parse()
        assert custom_tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.webmcp.custom_tools.with_streaming_response.remove(
            id="ct_n10b9798ad53ecc4y69z31e1",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_tool = await response.parse()
            assert custom_tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.webmcp.custom_tools.with_raw_response.remove(
                id="ct_n10b9798ad53ecc4y69z31e1",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.webmcp.custom_tools.with_raw_response.remove(
                id="",
                id_or_name="id_or_name",
            )
