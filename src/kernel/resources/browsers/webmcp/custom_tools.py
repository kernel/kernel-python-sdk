# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.browsers.webmcp import custom_tool_add_params
from ....types.browsers.webmcp.custom_tools_response import CustomToolsResponse

__all__ = ["CustomToolsResource", "AsyncCustomToolsResource"]


class CustomToolsResource(SyncAPIResource):
    """Discover and invoke native page tools across the browser instance."""

    @cached_property
    def with_raw_response(self) -> CustomToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CustomToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return CustomToolsResourceWithStreamingResponse(self)

    def list(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomToolsResponse:
        """
        Returns every registered custom tool with its generated ID, namespace, matcher,
        and MCP tool metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            path_template("/browsers/{id_or_name}/webmcp/custom-tools", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomToolsResponse,
        )

    def add(
        self,
        id_or_name: str,
        *,
        namespace: str,
        source: str,
        force_overwrite_namespace: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomToolsResponse:
        """Add a namespaced batch of custom tools.

        A custom tool can be page-backed or
        CDP-backed. Page-backed tools execute in the page via JavaScript. CDP-backed
        tools execute via CDP and can use all browser REPL tools (see `/repl`). The
        source must evaluate to a non-empty array of definitions with URL matchers, tool
        metadata (including an optional output schema), and execute functions. The batch
        is added atomically. Matchers apply to top-level documents and nested frames,
        including out-of-process iframes; each matching tool is exposed once on the
        tab's top-level document and appears in the WebMCP tool snapshot.

        To update one tool, list the tools, delete its ID, and add its replacement. Set
        force_overwrite_namespace to replace every existing tool in the namespace
        atomically; omitted or false adds tools without replacing existing ones.
        Existing invocations continue.

        Args:
          source: JavaScript expression that evaluates to a non-empty array of custom tool
              definitions. Limited to 8,000,000 bytes when UTF-8 encoded, so multi-byte
              characters reduce the allowed character count.

          force_overwrite_namespace: Atomically replace all existing tools in this namespace with this batch when
              true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._post(
            path_template("/browsers/{id_or_name}/webmcp/custom-tools", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "namespace": namespace,
                    "source": source,
                    "force_overwrite_namespace": force_overwrite_namespace,
                },
                custom_tool_add_params.CustomToolAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomToolsResponse,
        )

    def remove(
        self,
        id: str,
        *,
        id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes one custom tool by generated ID.

        An invocation already in progress is
        not canceled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/browsers/{id_or_name}/webmcp/custom-tools/{id}", id_or_name=id_or_name, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCustomToolsResource(AsyncAPIResource):
    """Discover and invoke native page tools across the browser instance."""

    @cached_property
    def with_raw_response(self) -> AsyncCustomToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncCustomToolsResourceWithStreamingResponse(self)

    async def list(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomToolsResponse:
        """
        Returns every registered custom tool with its generated ID, namespace, matcher,
        and MCP tool metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            path_template("/browsers/{id_or_name}/webmcp/custom-tools", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomToolsResponse,
        )

    async def add(
        self,
        id_or_name: str,
        *,
        namespace: str,
        source: str,
        force_overwrite_namespace: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomToolsResponse:
        """Add a namespaced batch of custom tools.

        A custom tool can be page-backed or
        CDP-backed. Page-backed tools execute in the page via JavaScript. CDP-backed
        tools execute via CDP and can use all browser REPL tools (see `/repl`). The
        source must evaluate to a non-empty array of definitions with URL matchers, tool
        metadata (including an optional output schema), and execute functions. The batch
        is added atomically. Matchers apply to top-level documents and nested frames,
        including out-of-process iframes; each matching tool is exposed once on the
        tab's top-level document and appears in the WebMCP tool snapshot.

        To update one tool, list the tools, delete its ID, and add its replacement. Set
        force_overwrite_namespace to replace every existing tool in the namespace
        atomically; omitted or false adds tools without replacing existing ones.
        Existing invocations continue.

        Args:
          source: JavaScript expression that evaluates to a non-empty array of custom tool
              definitions. Limited to 8,000,000 bytes when UTF-8 encoded, so multi-byte
              characters reduce the allowed character count.

          force_overwrite_namespace: Atomically replace all existing tools in this namespace with this batch when
              true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._post(
            path_template("/browsers/{id_or_name}/webmcp/custom-tools", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "namespace": namespace,
                    "source": source,
                    "force_overwrite_namespace": force_overwrite_namespace,
                },
                custom_tool_add_params.CustomToolAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomToolsResponse,
        )

    async def remove(
        self,
        id: str,
        *,
        id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes one custom tool by generated ID.

        An invocation already in progress is
        not canceled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/browsers/{id_or_name}/webmcp/custom-tools/{id}", id_or_name=id_or_name, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CustomToolsResourceWithRawResponse:
    def __init__(self, custom_tools: CustomToolsResource) -> None:
        self._custom_tools = custom_tools

        self.list = to_raw_response_wrapper(
            custom_tools.list,
        )
        self.add = to_raw_response_wrapper(
            custom_tools.add,
        )
        self.remove = to_raw_response_wrapper(
            custom_tools.remove,
        )


class AsyncCustomToolsResourceWithRawResponse:
    def __init__(self, custom_tools: AsyncCustomToolsResource) -> None:
        self._custom_tools = custom_tools

        self.list = async_to_raw_response_wrapper(
            custom_tools.list,
        )
        self.add = async_to_raw_response_wrapper(
            custom_tools.add,
        )
        self.remove = async_to_raw_response_wrapper(
            custom_tools.remove,
        )


class CustomToolsResourceWithStreamingResponse:
    def __init__(self, custom_tools: CustomToolsResource) -> None:
        self._custom_tools = custom_tools

        self.list = to_streamed_response_wrapper(
            custom_tools.list,
        )
        self.add = to_streamed_response_wrapper(
            custom_tools.add,
        )
        self.remove = to_streamed_response_wrapper(
            custom_tools.remove,
        )


class AsyncCustomToolsResourceWithStreamingResponse:
    def __init__(self, custom_tools: AsyncCustomToolsResource) -> None:
        self._custom_tools = custom_tools

        self.list = async_to_streamed_response_wrapper(
            custom_tools.list,
        )
        self.add = async_to_streamed_response_wrapper(
            custom_tools.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            custom_tools.remove,
        )
