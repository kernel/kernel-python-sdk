# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from .executors import (
    ExecutorsResource,
    AsyncExecutorsResource,
    ExecutorsResourceWithRawResponse,
    AsyncExecutorsResourceWithRawResponse,
    ExecutorsResourceWithStreamingResponse,
    AsyncExecutorsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.browsers import playwright_execute_params
from ....types.browsers.playwright_execute_response import PlaywrightExecuteResponse

__all__ = ["PlaywrightResource", "AsyncPlaywrightResource"]


class PlaywrightResource(SyncAPIResource):
    """
    Execute Playwright code against the browser instance and manage the executors it runs in.
    """

    @cached_property
    def executors(self) -> ExecutorsResource:
        """
        Execute Playwright code against the browser instance and manage the executors it runs in.
        """
        return ExecutorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PlaywrightResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PlaywrightResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaywrightResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return PlaywrightResourceWithStreamingResponse(self)

    def execute(
        self,
        id_or_name: str,
        *,
        code: str,
        executor: str | Omit = omit,
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaywrightExecuteResponse:
        """
        Execute arbitrary Playwright code in a fresh execution context against the
        browser. The code runs in the same VM as the browser, minimizing latency and
        maximizing throughput. It has access to 'page', 'context', 'browser', and
        'webmcp' variables. Use 'webmcp.listTools()' to discover browser-wide WebMCP
        tools and 'webmcp.invokeTool(toolRef, input?, { timeoutSec? })' to invoke an
        exact registration. It can `return` a value, and this value is returned in the
        response.

        Every call runs in an executor: a dedicated Node.js process with its own browser
        connection. Calls on different executors run concurrently; calls on the same
        executor run one at a time. A timeout, crash, or blocked event loop in one
        executor does not affect other executors. After a timeout the executor keeps its
        process and drops its browser connection, so code abandoned by the timeout
        cannot keep driving the browser. After a crash or a blocked event loop, the next
        call on that executor starts a fresh process.

        Calls without 'executor' run in the executor named 'default', which always
        exists and is the same as passing 'executor: "default"'. In the default
        executor, 'page' is bound to an active tab reported by Chrome. In single-window
        sessions, this is the foreground tab. When multiple browser windows are open,
        Chrome reports one active tab per window and the selected window is unspecified.
        'context' is the BrowserContext that owns the selected page. Use
        'browser.contexts()' to select a context or page explicitly.

        Pass any other name to run the call in a named executor. The first call with a
        new name creates it. Each named executor owns a tab: its first call opens a new
        background tab in the default browser context, and 'page' is bound to that tab
        on every later call while it stays open. Opening it does not change the active
        tab of an existing window. If the tab is closed, the next call opens a new one
        and reports 'tab.created: true'. Executor code can still reach other tabs
        through 'context' and 'browser'; ownership only decides what 'page' is bound to.
        Use named executors to drive several tabs of one browser in parallel.

        A browser can have at most 8 named executors; the default executor does not
        count. A call that would create another returns 409 with the current executors;
        delete one with DELETE /browsers/{id_or_name}/playwright/executors/{name}. Named
        executors are not removed automatically while the browser runs; when it shuts
        down, they are removed and their tabs closed.

        A named call to a browser whose image predates executors fails with 400 instead
        of running on the active tab; calls without 'executor' keep working on every
        image.

        Args:
          code: TypeScript/JavaScript code to execute. The code has access to 'page', 'context',
              and 'browser' variables. It runs within a function, so you can use a return
              statement at the end to return a value. This value is returned as the `result`
              property in the response. Example: "await page.goto('https://example.com');
              return await page.title();"

          executor: Name of a Playwright executor. Calls with the same name run in the same
              executor, one at a time; the first call with a new name creates it. Calls on
              different executors run concurrently. 'default' names the executor that runs
              calls without a name.

          timeout_sec: Maximum execution time in seconds. Default is 60.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._post(
            path_template("/browsers/{id_or_name}/playwright/execute", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "code": code,
                    "executor": executor,
                    "timeout_sec": timeout_sec,
                },
                playwright_execute_params.PlaywrightExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaywrightExecuteResponse,
        )


class AsyncPlaywrightResource(AsyncAPIResource):
    """
    Execute Playwright code against the browser instance and manage the executors it runs in.
    """

    @cached_property
    def executors(self) -> AsyncExecutorsResource:
        """
        Execute Playwright code against the browser instance and manage the executors it runs in.
        """
        return AsyncExecutorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPlaywrightResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaywrightResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaywrightResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncPlaywrightResourceWithStreamingResponse(self)

    async def execute(
        self,
        id_or_name: str,
        *,
        code: str,
        executor: str | Omit = omit,
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaywrightExecuteResponse:
        """
        Execute arbitrary Playwright code in a fresh execution context against the
        browser. The code runs in the same VM as the browser, minimizing latency and
        maximizing throughput. It has access to 'page', 'context', 'browser', and
        'webmcp' variables. Use 'webmcp.listTools()' to discover browser-wide WebMCP
        tools and 'webmcp.invokeTool(toolRef, input?, { timeoutSec? })' to invoke an
        exact registration. It can `return` a value, and this value is returned in the
        response.

        Every call runs in an executor: a dedicated Node.js process with its own browser
        connection. Calls on different executors run concurrently; calls on the same
        executor run one at a time. A timeout, crash, or blocked event loop in one
        executor does not affect other executors. After a timeout the executor keeps its
        process and drops its browser connection, so code abandoned by the timeout
        cannot keep driving the browser. After a crash or a blocked event loop, the next
        call on that executor starts a fresh process.

        Calls without 'executor' run in the executor named 'default', which always
        exists and is the same as passing 'executor: "default"'. In the default
        executor, 'page' is bound to an active tab reported by Chrome. In single-window
        sessions, this is the foreground tab. When multiple browser windows are open,
        Chrome reports one active tab per window and the selected window is unspecified.
        'context' is the BrowserContext that owns the selected page. Use
        'browser.contexts()' to select a context or page explicitly.

        Pass any other name to run the call in a named executor. The first call with a
        new name creates it. Each named executor owns a tab: its first call opens a new
        background tab in the default browser context, and 'page' is bound to that tab
        on every later call while it stays open. Opening it does not change the active
        tab of an existing window. If the tab is closed, the next call opens a new one
        and reports 'tab.created: true'. Executor code can still reach other tabs
        through 'context' and 'browser'; ownership only decides what 'page' is bound to.
        Use named executors to drive several tabs of one browser in parallel.

        A browser can have at most 8 named executors; the default executor does not
        count. A call that would create another returns 409 with the current executors;
        delete one with DELETE /browsers/{id_or_name}/playwright/executors/{name}. Named
        executors are not removed automatically while the browser runs; when it shuts
        down, they are removed and their tabs closed.

        A named call to a browser whose image predates executors fails with 400 instead
        of running on the active tab; calls without 'executor' keep working on every
        image.

        Args:
          code: TypeScript/JavaScript code to execute. The code has access to 'page', 'context',
              and 'browser' variables. It runs within a function, so you can use a return
              statement at the end to return a value. This value is returned as the `result`
              property in the response. Example: "await page.goto('https://example.com');
              return await page.title();"

          executor: Name of a Playwright executor. Calls with the same name run in the same
              executor, one at a time; the first call with a new name creates it. Calls on
              different executors run concurrently. 'default' names the executor that runs
              calls without a name.

          timeout_sec: Maximum execution time in seconds. Default is 60.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._post(
            path_template("/browsers/{id_or_name}/playwright/execute", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "code": code,
                    "executor": executor,
                    "timeout_sec": timeout_sec,
                },
                playwright_execute_params.PlaywrightExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaywrightExecuteResponse,
        )


class PlaywrightResourceWithRawResponse:
    def __init__(self, playwright: PlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = to_raw_response_wrapper(
            playwright.execute,
        )

    @cached_property
    def executors(self) -> ExecutorsResourceWithRawResponse:
        """
        Execute Playwright code against the browser instance and manage the executors it runs in.
        """
        return ExecutorsResourceWithRawResponse(self._playwright.executors)


class AsyncPlaywrightResourceWithRawResponse:
    def __init__(self, playwright: AsyncPlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = async_to_raw_response_wrapper(
            playwright.execute,
        )

    @cached_property
    def executors(self) -> AsyncExecutorsResourceWithRawResponse:
        """
        Execute Playwright code against the browser instance and manage the executors it runs in.
        """
        return AsyncExecutorsResourceWithRawResponse(self._playwright.executors)


class PlaywrightResourceWithStreamingResponse:
    def __init__(self, playwright: PlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = to_streamed_response_wrapper(
            playwright.execute,
        )

    @cached_property
    def executors(self) -> ExecutorsResourceWithStreamingResponse:
        """
        Execute Playwright code against the browser instance and manage the executors it runs in.
        """
        return ExecutorsResourceWithStreamingResponse(self._playwright.executors)


class AsyncPlaywrightResourceWithStreamingResponse:
    def __init__(self, playwright: AsyncPlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = async_to_streamed_response_wrapper(
            playwright.execute,
        )

    @cached_property
    def executors(self) -> AsyncExecutorsResourceWithStreamingResponse:
        """
        Execute Playwright code against the browser instance and manage the executors it runs in.
        """
        return AsyncExecutorsResourceWithStreamingResponse(self._playwright.executors)
