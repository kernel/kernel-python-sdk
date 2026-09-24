# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers import ToolsResponse, InvocationResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebmcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invoke_tool(self, client: Kernel) -> None:
        webmcp = client.browsers.webmcp.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
        )
        assert_matches_type(InvocationResult, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invoke_tool_with_all_params(self, client: Kernel) -> None:
        webmcp = client.browsers.webmcp.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
            timeout_sec=1,
        )
        assert_matches_type(InvocationResult, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_invoke_tool(self, client: Kernel) -> None:
        response = client.browsers.webmcp.with_raw_response.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webmcp = response.parse()
        assert_matches_type(InvocationResult, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_invoke_tool(self, client: Kernel) -> None:
        with client.browsers.webmcp.with_streaming_response.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webmcp = response.parse()
            assert_matches_type(InvocationResult, webmcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_invoke_tool(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.webmcp.with_raw_response.invoke_tool(
                id_or_name="",
                input={"foo": "bar"},
                tool_ref="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_tools(self, client: Kernel) -> None:
        webmcp = client.browsers.webmcp.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(ToolsResponse, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_tools_with_all_params(self, client: Kernel) -> None:
        webmcp = client.browsers.webmcp.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            exclude_custom=True,
        )
        assert_matches_type(ToolsResponse, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_tools(self, client: Kernel) -> None:
        response = client.browsers.webmcp.with_raw_response.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webmcp = response.parse()
        assert_matches_type(ToolsResponse, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_tools(self, client: Kernel) -> None:
        with client.browsers.webmcp.with_streaming_response.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webmcp = response.parse()
            assert_matches_type(ToolsResponse, webmcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_tools(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.browsers.webmcp.with_raw_response.list_tools(
                id_or_name="",
            )


class TestAsyncWebmcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invoke_tool(self, async_client: AsyncKernel) -> None:
        webmcp = await async_client.browsers.webmcp.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
        )
        assert_matches_type(InvocationResult, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invoke_tool_with_all_params(self, async_client: AsyncKernel) -> None:
        webmcp = await async_client.browsers.webmcp.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
            timeout_sec=1,
        )
        assert_matches_type(InvocationResult, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_invoke_tool(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.webmcp.with_raw_response.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webmcp = await response.parse()
        assert_matches_type(InvocationResult, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_invoke_tool(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.webmcp.with_streaming_response.invoke_tool(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            input={"foo": "bar"},
            tool_ref="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webmcp = await response.parse()
            assert_matches_type(InvocationResult, webmcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_invoke_tool(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.webmcp.with_raw_response.invoke_tool(
                id_or_name="",
                input={"foo": "bar"},
                tool_ref="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_tools(self, async_client: AsyncKernel) -> None:
        webmcp = await async_client.browsers.webmcp.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )
        assert_matches_type(ToolsResponse, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_tools_with_all_params(self, async_client: AsyncKernel) -> None:
        webmcp = await async_client.browsers.webmcp.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
            exclude_custom=True,
        )
        assert_matches_type(ToolsResponse, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_tools(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.webmcp.with_raw_response.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webmcp = await response.parse()
        assert_matches_type(ToolsResponse, webmcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_tools(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.webmcp.with_streaming_response.list_tools(
            id_or_name="htzv5orfit78e1m2biiifpbv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webmcp = await response.parse()
            assert_matches_type(ToolsResponse, webmcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_tools(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.browsers.webmcp.with_raw_response.list_tools(
                id_or_name="",
            )
