# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import proxy_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.proxy_list_response import ProxyListResponse
from ..types.proxy_check_response import ProxyCheckResponse
from ..types.proxy_create_response import ProxyCreateResponse
from ..types.proxy_retrieve_response import ProxyRetrieveResponse

__all__ = ["ProxiesResource", "AsyncProxiesResource"]


class ProxiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return ProxiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["datacenter", "isp", "residential", "mobile", "custom"],
        config: proxy_create_params.Config | Omit = omit,
        name: str | Omit = omit,
        protocol: Literal["http", "https"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCreateResponse:
        """
        Create a new proxy configuration for the caller's organization.

        Args:
          type: Proxy type to use. In terms of quality for avoiding bot-detection, from best to
              worst: `mobile` > `residential` > `isp` > `datacenter`.

          config: Configuration specific to the selected proxy `type`.

          name: Readable name of the proxy.

          protocol: Protocol to use for the proxy connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/proxies",
            body=maybe_transform(
                {
                    "type": type,
                    "config": config,
                    "name": name,
                    "protocol": protocol,
                },
                proxy_create_params.ProxyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyRetrieveResponse:
        """
        Retrieve a proxy belonging to the caller's organization by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/proxies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListResponse:
        """List proxies owned by the caller's organization."""
        return self._get(
            "/proxies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft delete a proxy.

        Sessions referencing it are not modified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/proxies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCheckResponse:
        """
        Run a health check on the proxy to verify it's working.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/proxies/{id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCheckResponse,
        )


class AsyncProxiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncProxiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["datacenter", "isp", "residential", "mobile", "custom"],
        config: proxy_create_params.Config | Omit = omit,
        name: str | Omit = omit,
        protocol: Literal["http", "https"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCreateResponse:
        """
        Create a new proxy configuration for the caller's organization.

        Args:
          type: Proxy type to use. In terms of quality for avoiding bot-detection, from best to
              worst: `mobile` > `residential` > `isp` > `datacenter`.

          config: Configuration specific to the selected proxy `type`.

          name: Readable name of the proxy.

          protocol: Protocol to use for the proxy connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/proxies",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "config": config,
                    "name": name,
                    "protocol": protocol,
                },
                proxy_create_params.ProxyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyRetrieveResponse:
        """
        Retrieve a proxy belonging to the caller's organization by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/proxies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListResponse:
        """List proxies owned by the caller's organization."""
        return await self._get(
            "/proxies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft delete a proxy.

        Sessions referencing it are not modified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/proxies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCheckResponse:
        """
        Run a health check on the proxy to verify it's working.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/proxies/{id}/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCheckResponse,
        )


class ProxiesResourceWithRawResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.create = to_raw_response_wrapper(
            proxies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            proxies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            proxies.list,
        )
        self.delete = to_raw_response_wrapper(
            proxies.delete,
        )
        self.check = to_raw_response_wrapper(
            proxies.check,
        )


class AsyncProxiesResourceWithRawResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.create = async_to_raw_response_wrapper(
            proxies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            proxies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            proxies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            proxies.delete,
        )
        self.check = async_to_raw_response_wrapper(
            proxies.check,
        )


class ProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.create = to_streamed_response_wrapper(
            proxies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            proxies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            proxies.list,
        )
        self.delete = to_streamed_response_wrapper(
            proxies.delete,
        )
        self.check = to_streamed_response_wrapper(
            proxies.check,
        )


class AsyncProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.create = async_to_streamed_response_wrapper(
            proxies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            proxies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            proxies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            proxies.delete,
        )
        self.check = async_to_streamed_response_wrapper(
            proxies.check,
        )
