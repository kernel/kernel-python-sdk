# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import app_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.app_list_response import AppListResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        app_name: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[AppListResponse]:
        """List applications.

        Optionally filter by app name and/or version label.

        Args:
          app_name: Filter results by application name.

          limit: Limit the number of apps to return.

          offset: Offset the number of apps to return.

          version: Filter results by version label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/apps",
            page=SyncOffsetPagination[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_name": app_name,
                        "limit": limit,
                        "offset": offset,
                        "version": version,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=AppListResponse,
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        app_name: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AppListResponse, AsyncOffsetPagination[AppListResponse]]:
        """List applications.

        Optionally filter by app name and/or version label.

        Args:
          app_name: Filter results by application name.

          limit: Limit the number of apps to return.

          offset: Offset the number of apps to return.

          version: Filter results by version label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/apps",
            page=AsyncOffsetPagination[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_name": app_name,
                        "limit": limit,
                        "offset": offset,
                        "version": version,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=AppListResponse,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.list = to_raw_response_wrapper(
            apps.list,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.list = async_to_raw_response_wrapper(
            apps.list,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.list = to_streamed_response_wrapper(
            apps.list,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
