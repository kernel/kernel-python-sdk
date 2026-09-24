# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .custom_tools import (
    CustomToolsResource,
    AsyncCustomToolsResource,
    CustomToolsResourceWithRawResponse,
    AsyncCustomToolsResourceWithRawResponse,
    CustomToolsResourceWithStreamingResponse,
    AsyncCustomToolsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.browsers import webmcp_list_tools_params, webmcp_invoke_tool_params
from ....types.browsers.tools_response import ToolsResponse
from ....types.browsers.invocation_result import InvocationResult

__all__ = ["WebmcpResource", "AsyncWebmcpResource"]


class WebmcpResource(SyncAPIResource):
    """Discover and invoke native page tools across the browser instance."""

    @cached_property
    def custom_tools(self) -> CustomToolsResource:
        """Discover and invoke native page tools across the browser instance."""
        return CustomToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebmcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebmcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebmcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return WebmcpResourceWithStreamingResponse(self)

    def invoke_tool(
        self,
        id_or_name: str,
        *,
        input: Dict[str, object],
        tool_ref: str,
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationResult:
        """Invokes the exact live registration identified by tool_ref.

        Non-autosubmit
        declarative form tools return after their fields are populated with an
        awaiting_submission status. Other tools wait for a terminal result, including
        across navigation. Inspect a populated form, obtain any required confirmation,
        then submit through Playwright or computer interaction without invoking the tool
        again. If the tab or embedded frame disappears, or the request times out after
        invocation begins, the response reports outcome_unknown and the tool is not
        retried. CDP-backed custom tool outputs above 240 KiB return an error rather
        than a truncated result.

        Args:
          input: Tool input, limited to 1 MiB after JSON serialization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._post(
            path_template("/browsers/{id_or_name}/webmcp/invoke", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "input": input,
                    "tool_ref": tool_ref,
                    "timeout_sec": timeout_sec,
                },
                webmcp_invoke_tool_params.WebmcpInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationResult,
        )

    def list_tools(
        self,
        id_or_name: str,
        *,
        exclude_custom: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolsResponse:
        """
        Returns a snapshot of native and custom WebMCP tools available across every open
        tab and embedded frame in the browser. Each tool includes an opaque tool_ref for
        invoking that exact live registration, nested tool metadata, and source
        information. Custom tools include their generated ID, namespace, and CDP
        target_id in source. Tools disappear when their document closes or navigates
        away. Use exclude_custom to return only page-provided tools.

        Args:
          exclude_custom: Exclude custom tools when true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            path_template("/browsers/{id_or_name}/webmcp/tools", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"exclude_custom": exclude_custom}, webmcp_list_tools_params.WebmcpListToolsParams
                ),
            ),
            cast_to=ToolsResponse,
        )


class AsyncWebmcpResource(AsyncAPIResource):
    """Discover and invoke native page tools across the browser instance."""

    @cached_property
    def custom_tools(self) -> AsyncCustomToolsResource:
        """Discover and invoke native page tools across the browser instance."""
        return AsyncCustomToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebmcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebmcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebmcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncWebmcpResourceWithStreamingResponse(self)

    async def invoke_tool(
        self,
        id_or_name: str,
        *,
        input: Dict[str, object],
        tool_ref: str,
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationResult:
        """Invokes the exact live registration identified by tool_ref.

        Non-autosubmit
        declarative form tools return after their fields are populated with an
        awaiting_submission status. Other tools wait for a terminal result, including
        across navigation. Inspect a populated form, obtain any required confirmation,
        then submit through Playwright or computer interaction without invoking the tool
        again. If the tab or embedded frame disappears, or the request times out after
        invocation begins, the response reports outcome_unknown and the tool is not
        retried. CDP-backed custom tool outputs above 240 KiB return an error rather
        than a truncated result.

        Args:
          input: Tool input, limited to 1 MiB after JSON serialization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._post(
            path_template("/browsers/{id_or_name}/webmcp/invoke", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "input": input,
                    "tool_ref": tool_ref,
                    "timeout_sec": timeout_sec,
                },
                webmcp_invoke_tool_params.WebmcpInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationResult,
        )

    async def list_tools(
        self,
        id_or_name: str,
        *,
        exclude_custom: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolsResponse:
        """
        Returns a snapshot of native and custom WebMCP tools available across every open
        tab and embedded frame in the browser. Each tool includes an opaque tool_ref for
        invoking that exact live registration, nested tool metadata, and source
        information. Custom tools include their generated ID, namespace, and CDP
        target_id in source. Tools disappear when their document closes or navigates
        away. Use exclude_custom to return only page-provided tools.

        Args:
          exclude_custom: Exclude custom tools when true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            path_template("/browsers/{id_or_name}/webmcp/tools", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"exclude_custom": exclude_custom}, webmcp_list_tools_params.WebmcpListToolsParams
                ),
            ),
            cast_to=ToolsResponse,
        )


class WebmcpResourceWithRawResponse:
    def __init__(self, webmcp: WebmcpResource) -> None:
        self._webmcp = webmcp

        self.invoke_tool = to_raw_response_wrapper(
            webmcp.invoke_tool,
        )
        self.list_tools = to_raw_response_wrapper(
            webmcp.list_tools,
        )

    @cached_property
    def custom_tools(self) -> CustomToolsResourceWithRawResponse:
        """Discover and invoke native page tools across the browser instance."""
        return CustomToolsResourceWithRawResponse(self._webmcp.custom_tools)


class AsyncWebmcpResourceWithRawResponse:
    def __init__(self, webmcp: AsyncWebmcpResource) -> None:
        self._webmcp = webmcp

        self.invoke_tool = async_to_raw_response_wrapper(
            webmcp.invoke_tool,
        )
        self.list_tools = async_to_raw_response_wrapper(
            webmcp.list_tools,
        )

    @cached_property
    def custom_tools(self) -> AsyncCustomToolsResourceWithRawResponse:
        """Discover and invoke native page tools across the browser instance."""
        return AsyncCustomToolsResourceWithRawResponse(self._webmcp.custom_tools)


class WebmcpResourceWithStreamingResponse:
    def __init__(self, webmcp: WebmcpResource) -> None:
        self._webmcp = webmcp

        self.invoke_tool = to_streamed_response_wrapper(
            webmcp.invoke_tool,
        )
        self.list_tools = to_streamed_response_wrapper(
            webmcp.list_tools,
        )

    @cached_property
    def custom_tools(self) -> CustomToolsResourceWithStreamingResponse:
        """Discover and invoke native page tools across the browser instance."""
        return CustomToolsResourceWithStreamingResponse(self._webmcp.custom_tools)


class AsyncWebmcpResourceWithStreamingResponse:
    def __init__(self, webmcp: AsyncWebmcpResource) -> None:
        self._webmcp = webmcp

        self.invoke_tool = async_to_streamed_response_wrapper(
            webmcp.invoke_tool,
        )
        self.list_tools = async_to_streamed_response_wrapper(
            webmcp.list_tools,
        )

    @cached_property
    def custom_tools(self) -> AsyncCustomToolsResourceWithStreamingResponse:
        """Discover and invoke native page tools across the browser instance."""
        return AsyncCustomToolsResourceWithStreamingResponse(self._webmcp.custom_tools)
