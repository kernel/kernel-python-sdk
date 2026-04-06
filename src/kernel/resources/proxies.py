# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import proxy_check_params, proxy_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
    """Create and manage proxy configurations for routing browser traffic."""

    @cached_property
    def with_raw_response(self) -> ProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ProxiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["datacenter", "isp", "residential", "mobile", "custom"],
        bypass_hosts: SequenceNotStr[str] | Omit = omit,
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

          bypass_hosts: Hostnames that should bypass the parent proxy and connect directly.

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
                    "bypass_hosts": bypass_hosts,
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
            path_template("/proxies/{id}", id=id),
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
            path_template("/proxies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check(
        self,
        id: str,
        *,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCheckResponse:
        """Run a health check on the proxy to verify it's working.

        Optionally specify a URL
        to test reachability against a specific target. For ISP and datacenter proxies,
        this reliably tests whether the target site is reachable from the proxy's stable
        exit IP. For residential and mobile proxies, the exit node varies between
        requests, so this validates proxy configuration and connectivity rather than
        guaranteeing site-specific reachability.

        Args:
          url: An optional URL to test reachability against. If provided, the proxy check will
              test connectivity to this URL instead of the default test URLs. Only HTTP and
              HTTPS schemes are allowed, and the URL must resolve to a public IP address. For
              ISP and datacenter proxies, the exit IP is stable, so a successful check
              reliably indicates that subsequent browser sessions will reach the target site
              with the same IP. For residential and mobile proxies, the exit node changes
              between requests, so a successful check validates proxy configuration but does
              not guarantee that a subsequent browser session will use the same exit IP or
              reach the same site — it is useful for verifying credentials and connectivity,
              not for predicting site-specific behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/proxies/{id}/check", id=id),
            body=maybe_transform({"url": url}, proxy_check_params.ProxyCheckParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCheckResponse,
        )


class AsyncProxiesResource(AsyncAPIResource):
    """Create and manage proxy configurations for routing browser traffic."""

    @cached_property
    def with_raw_response(self) -> AsyncProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncProxiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["datacenter", "isp", "residential", "mobile", "custom"],
        bypass_hosts: SequenceNotStr[str] | Omit = omit,
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

          bypass_hosts: Hostnames that should bypass the parent proxy and connect directly.

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
                    "bypass_hosts": bypass_hosts,
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
            path_template("/proxies/{id}", id=id),
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
            path_template("/proxies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check(
        self,
        id: str,
        *,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCheckResponse:
        """Run a health check on the proxy to verify it's working.

        Optionally specify a URL
        to test reachability against a specific target. For ISP and datacenter proxies,
        this reliably tests whether the target site is reachable from the proxy's stable
        exit IP. For residential and mobile proxies, the exit node varies between
        requests, so this validates proxy configuration and connectivity rather than
        guaranteeing site-specific reachability.

        Args:
          url: An optional URL to test reachability against. If provided, the proxy check will
              test connectivity to this URL instead of the default test URLs. Only HTTP and
              HTTPS schemes are allowed, and the URL must resolve to a public IP address. For
              ISP and datacenter proxies, the exit IP is stable, so a successful check
              reliably indicates that subsequent browser sessions will reach the target site
              with the same IP. For residential and mobile proxies, the exit node changes
              between requests, so a successful check validates proxy configuration but does
              not guarantee that a subsequent browser session will use the same exit IP or
              reach the same site — it is useful for verifying credentials and connectivity,
              not for predicting site-specific behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/proxies/{id}/check", id=id),
            body=await async_maybe_transform({"url": url}, proxy_check_params.ProxyCheckParams),
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
