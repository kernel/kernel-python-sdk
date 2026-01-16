# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.browsers import playwright_execute_params
from ...types.browsers.playwright_execute_response import PlaywrightExecuteResponse

__all__ = ["PlaywrightResource", "AsyncPlaywrightResource"]


class PlaywrightResource(SyncAPIResource):
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
        id: str,
        *,
        code: str,
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
        maximizing throughput. It has access to 'page', 'context', and 'browser'
        variables. It can `return` a value, and this value is returned in the response.

        Args:
          code: TypeScript/JavaScript code to execute. The code has access to 'page', 'context',
              and 'browser' variables. It runs within a function, so you can use a return
              statement at the end to return a value. This value is returned as the `result`
              property in the response. Example: "await page.goto('https://example.com');
              return await page.title();"

          timeout_sec: Maximum execution time in seconds. Default is 60.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/browsers/{id}/playwright/execute",
            body=maybe_transform(
                {
                    "code": code,
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
        id: str,
        *,
        code: str,
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
        maximizing throughput. It has access to 'page', 'context', and 'browser'
        variables. It can `return` a value, and this value is returned in the response.

        Args:
          code: TypeScript/JavaScript code to execute. The code has access to 'page', 'context',
              and 'browser' variables. It runs within a function, so you can use a return
              statement at the end to return a value. This value is returned as the `result`
              property in the response. Example: "await page.goto('https://example.com');
              return await page.title();"

          timeout_sec: Maximum execution time in seconds. Default is 60.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/browsers/{id}/playwright/execute",
            body=await async_maybe_transform(
                {
                    "code": code,
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


class AsyncPlaywrightResourceWithRawResponse:
    def __init__(self, playwright: AsyncPlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = async_to_raw_response_wrapper(
            playwright.execute,
        )


class PlaywrightResourceWithStreamingResponse:
    def __init__(self, playwright: PlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = to_streamed_response_wrapper(
            playwright.execute,
        )


class AsyncPlaywrightResourceWithStreamingResponse:
    def __init__(self, playwright: AsyncPlaywrightResource) -> None:
        self._playwright = playwright

        self.execute = async_to_streamed_response_wrapper(
            playwright.execute,
        )
