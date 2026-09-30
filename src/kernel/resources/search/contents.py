# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.search import content_fetch_params
from ...types.search.response import Response

__all__ = ["ContentsResource", "AsyncContentsResource"]


class ContentsResource(SyncAPIResource):
    """Search the web and retrieve content for selected results."""

    @cached_property
    def with_raw_response(self) -> ContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ContentsResourceWithStreamingResponse(self)

    def fetch(
        self,
        id: str,
        *,
        content: content_fetch_params.Content | Omit = omit,
        limit: int | Omit = omit,
        result_ids: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """Retrieves selected results from a retained search.

        Provide exactly one of
        result_ids or limit; the latter fetches the top results. Content defaults to
        source:auto. Responses preserve result_ids order. Unknown result IDs are
        rejected before retrieval starts. Missing, expired, or inaccessible searches
        return 404. Once retrieval begins, return one outcome per selected result,
        including timeout entries for work unfinished at the overall deadline. Browser
        retrievals run sequentially in result order, so later results may time out when
        earlier pages are slow. X-Request-Id identifies this request separately from the
        search resource.

        Args:
          content: Defaults to source:auto when omitted.

          limit: Maximum number of search results to fetch when result_ids is omitted, starting
              from rank 1. Mutually exclusive with result_ids.

          result_ids: Kernel-generated IDs from the referenced retained search, in desired response
              order. They are not provider-standard IDs. Mutually exclusive with limit.

          timeout_ms: Overall deadline across all selected results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/search/{id}/contents", id=id),
            body=maybe_transform(
                {
                    "content": content,
                    "limit": limit,
                    "result_ids": result_ids,
                    "timeout_ms": timeout_ms,
                },
                content_fetch_params.ContentFetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )


class AsyncContentsResource(AsyncAPIResource):
    """Search the web and retrieve content for selected results."""

    @cached_property
    def with_raw_response(self) -> AsyncContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncContentsResourceWithStreamingResponse(self)

    async def fetch(
        self,
        id: str,
        *,
        content: content_fetch_params.Content | Omit = omit,
        limit: int | Omit = omit,
        result_ids: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """Retrieves selected results from a retained search.

        Provide exactly one of
        result_ids or limit; the latter fetches the top results. Content defaults to
        source:auto. Responses preserve result_ids order. Unknown result IDs are
        rejected before retrieval starts. Missing, expired, or inaccessible searches
        return 404. Once retrieval begins, return one outcome per selected result,
        including timeout entries for work unfinished at the overall deadline. Browser
        retrievals run sequentially in result order, so later results may time out when
        earlier pages are slow. X-Request-Id identifies this request separately from the
        search resource.

        Args:
          content: Defaults to source:auto when omitted.

          limit: Maximum number of search results to fetch when result_ids is omitted, starting
              from rank 1. Mutually exclusive with result_ids.

          result_ids: Kernel-generated IDs from the referenced retained search, in desired response
              order. They are not provider-standard IDs. Mutually exclusive with limit.

          timeout_ms: Overall deadline across all selected results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/search/{id}/contents", id=id),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "limit": limit,
                    "result_ids": result_ids,
                    "timeout_ms": timeout_ms,
                },
                content_fetch_params.ContentFetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )


class ContentsResourceWithRawResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.fetch = to_raw_response_wrapper(
            contents.fetch,
        )


class AsyncContentsResourceWithRawResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.fetch = async_to_raw_response_wrapper(
            contents.fetch,
        )


class ContentsResourceWithStreamingResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.fetch = to_streamed_response_wrapper(
            contents.fetch,
        )


class AsyncContentsResourceWithStreamingResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.fetch = async_to_streamed_response_wrapper(
            contents.fetch,
        )
