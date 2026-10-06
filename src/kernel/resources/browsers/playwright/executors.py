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
from ....types.browsers.playwright import executor_delete_params
from ....types.browsers.playwright.executor_list import ExecutorList

__all__ = ["ExecutorsResource", "AsyncExecutorsResource"]


class ExecutorsResource(SyncAPIResource):
    """
    Execute Playwright code against the browser instance and manage the executors it runs in.
    """

    @cached_property
    def with_raw_response(self) -> ExecutorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExecutorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ExecutorsResourceWithStreamingResponse(self)

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
    ) -> ExecutorList:
        """
        Lists the default executor first, then the named executors created by POST
        /browsers/{id_or_name}/playwright/execute. Each entry reports whether a call is
        running on it and, for named executors, the target ID and URL of the tab it
        owns. Returns 404 for a browser whose image predates executors.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            path_template("/browsers/{id_or_name}/playwright/executors", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutorList,
        )

    def delete(
        self,
        name: str,
        *,
        id_or_name: str,
        close_tab: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Stops the executor's process.

        A call running on it fails with an error saying
        the executor was deleted. By default the executor's tab is closed too. The name
        can be reused; the next call with it creates a new executor and tab.

        The default executor is restarted instead of removed: its process is stopped, a
        call running on it fails with an error saying the executor was restarted, and
        queued and later calls run on a new process. It owns no tab, so 'close_tab' has
        no effect on it.

        Args:
          name: Name of a Playwright executor. Calls with the same name run in the same
              executor, one at a time; the first call with a new name creates it. Calls on
              different executors run concurrently. 'default' names the executor that runs
              calls without a name.

          close_tab: Close the executor's tab. Defaults to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/browsers/{id_or_name}/playwright/executors/{name}", id_or_name=id_or_name, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"close_tab": close_tab}, executor_delete_params.ExecutorDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncExecutorsResource(AsyncAPIResource):
    """
    Execute Playwright code against the browser instance and manage the executors it runs in.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExecutorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncExecutorsResourceWithStreamingResponse(self)

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
    ) -> ExecutorList:
        """
        Lists the default executor first, then the named executors created by POST
        /browsers/{id_or_name}/playwright/execute. Each entry reports whether a call is
        running on it and, for named executors, the target ID and URL of the tab it
        owns. Returns 404 for a browser whose image predates executors.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            path_template("/browsers/{id_or_name}/playwright/executors", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutorList,
        )

    async def delete(
        self,
        name: str,
        *,
        id_or_name: str,
        close_tab: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Stops the executor's process.

        A call running on it fails with an error saying
        the executor was deleted. By default the executor's tab is closed too. The name
        can be reused; the next call with it creates a new executor and tab.

        The default executor is restarted instead of removed: its process is stopped, a
        call running on it fails with an error saying the executor was restarted, and
        queued and later calls run on a new process. It owns no tab, so 'close_tab' has
        no effect on it.

        Args:
          name: Name of a Playwright executor. Calls with the same name run in the same
              executor, one at a time; the first call with a new name creates it. Calls on
              different executors run concurrently. 'default' names the executor that runs
              calls without a name.

          close_tab: Close the executor's tab. Defaults to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/browsers/{id_or_name}/playwright/executors/{name}", id_or_name=id_or_name, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"close_tab": close_tab}, executor_delete_params.ExecutorDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class ExecutorsResourceWithRawResponse:
    def __init__(self, executors: ExecutorsResource) -> None:
        self._executors = executors

        self.list = to_raw_response_wrapper(
            executors.list,
        )
        self.delete = to_raw_response_wrapper(
            executors.delete,
        )


class AsyncExecutorsResourceWithRawResponse:
    def __init__(self, executors: AsyncExecutorsResource) -> None:
        self._executors = executors

        self.list = async_to_raw_response_wrapper(
            executors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            executors.delete,
        )


class ExecutorsResourceWithStreamingResponse:
    def __init__(self, executors: ExecutorsResource) -> None:
        self._executors = executors

        self.list = to_streamed_response_wrapper(
            executors.list,
        )
        self.delete = to_streamed_response_wrapper(
            executors.delete,
        )


class AsyncExecutorsResourceWithStreamingResponse:
    def __init__(self, executors: AsyncExecutorsResource) -> None:
        self._executors = executors

        self.list = async_to_streamed_response_wrapper(
            executors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            executors.delete,
        )
