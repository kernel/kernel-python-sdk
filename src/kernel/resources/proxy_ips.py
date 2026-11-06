# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import proxy_ip_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.proxy_ip import ProxyIP
from ..types.proxy_ip_detail import ProxyIPDetail

__all__ = ["ProxyIPsResource", "AsyncProxyIPsResource"]


class ProxyIPsResource(SyncAPIResource):
    """Create and manage proxy configurations for routing browser traffic."""

    @cached_property
    def with_raw_response(self) -> ProxyIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProxyIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ProxyIPsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ip_address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyIPDetail:
        """
        Retrieve one reserved IP with the ISP proxies using it as their primary exit.
        proxy_count spans the organization; proxies lists only those in the current
        project. Returns 404 when the IP is not in the organization's allocation and 403
        with code reserved_isp_not_enabled when the organization has none. Scoped API
        keys require proxies:read on the whole project or organization, not on
        individual proxies; otherwise the operation returns 403 with code
        insufficient_scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return self._get(
            path_template("/proxy_ips/{ip_address}", ip_address=ip_address),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyIPDetail,
        )

    def list(
        self,
        *,
        country: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["active", "excluded"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ProxyIP]:
        """
        List the IP addresses reserved for the organization's ISP proxies, with each
        IP's country and whether it can currently be assigned. Available only to
        organizations with a reserved ISP allocation; others receive a 403 with code
        reserved_isp_not_enabled. Served from the allocation itself, so IPs appear
        whether or not a proxy uses them. Scoped API keys require proxies:read on the
        whole project or organization, not on individual proxies; otherwise the
        operation returns 403 with code insufficient_scope.

        Args:
          country: ISO 3166 country code to filter by. Must be a country ISP proxies support.

          limit: Limit the number of IPs to return.

          offset: Offset the number of IPs to return.

          status: Filter by whether the IP can currently be assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/proxy_ips",
            page=SyncOffsetPagination[ProxyIP],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    proxy_ip_list_params.ProxyIPListParams,
                ),
            ),
            model=ProxyIP,
        )


class AsyncProxyIPsResource(AsyncAPIResource):
    """Create and manage proxy configurations for routing browser traffic."""

    @cached_property
    def with_raw_response(self) -> AsyncProxyIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProxyIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncProxyIPsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ip_address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyIPDetail:
        """
        Retrieve one reserved IP with the ISP proxies using it as their primary exit.
        proxy_count spans the organization; proxies lists only those in the current
        project. Returns 404 when the IP is not in the organization's allocation and 403
        with code reserved_isp_not_enabled when the organization has none. Scoped API
        keys require proxies:read on the whole project or organization, not on
        individual proxies; otherwise the operation returns 403 with code
        insufficient_scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return await self._get(
            path_template("/proxy_ips/{ip_address}", ip_address=ip_address),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyIPDetail,
        )

    def list(
        self,
        *,
        country: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["active", "excluded"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProxyIP, AsyncOffsetPagination[ProxyIP]]:
        """
        List the IP addresses reserved for the organization's ISP proxies, with each
        IP's country and whether it can currently be assigned. Available only to
        organizations with a reserved ISP allocation; others receive a 403 with code
        reserved_isp_not_enabled. Served from the allocation itself, so IPs appear
        whether or not a proxy uses them. Scoped API keys require proxies:read on the
        whole project or organization, not on individual proxies; otherwise the
        operation returns 403 with code insufficient_scope.

        Args:
          country: ISO 3166 country code to filter by. Must be a country ISP proxies support.

          limit: Limit the number of IPs to return.

          offset: Offset the number of IPs to return.

          status: Filter by whether the IP can currently be assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/proxy_ips",
            page=AsyncOffsetPagination[ProxyIP],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    proxy_ip_list_params.ProxyIPListParams,
                ),
            ),
            model=ProxyIP,
        )


class ProxyIPsResourceWithRawResponse:
    def __init__(self, proxy_ips: ProxyIPsResource) -> None:
        self._proxy_ips = proxy_ips

        self.retrieve = to_raw_response_wrapper(
            proxy_ips.retrieve,
        )
        self.list = to_raw_response_wrapper(
            proxy_ips.list,
        )


class AsyncProxyIPsResourceWithRawResponse:
    def __init__(self, proxy_ips: AsyncProxyIPsResource) -> None:
        self._proxy_ips = proxy_ips

        self.retrieve = async_to_raw_response_wrapper(
            proxy_ips.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            proxy_ips.list,
        )


class ProxyIPsResourceWithStreamingResponse:
    def __init__(self, proxy_ips: ProxyIPsResource) -> None:
        self._proxy_ips = proxy_ips

        self.retrieve = to_streamed_response_wrapper(
            proxy_ips.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            proxy_ips.list,
        )


class AsyncProxyIPsResourceWithStreamingResponse:
    def __init__(self, proxy_ips: AsyncProxyIPsResource) -> None:
        self._proxy_ips = proxy_ips

        self.retrieve = async_to_streamed_response_wrapper(
            proxy_ips.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            proxy_ips.list,
        )
