# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import config_registry_list_params, config_registry_lookup_params, config_registry_resolve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .analyses import (
    AnalysesResource,
    AsyncAnalysesResource,
    AnalysesResourceWithRawResponse,
    AsyncAnalysesResourceWithRawResponse,
    AnalysesResourceWithStreamingResponse,
    AsyncAnalysesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.lookup_response import LookupResponse
from ...types.recommendation_summary import RecommendationSummary
from ...types.config_registry_response import ConfigRegistryResponse

__all__ = ["ConfigRegistryResource", "AsyncConfigRegistryResource"]


class ConfigRegistryResource(SyncAPIResource):
    """Resolve browser and proxy recommendations for bot-protected sites."""

    @cached_property
    def analyses(self) -> AnalysesResource:
        """Resolve browser and proxy recommendations for bot-protected sites."""
        return AnalysesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigRegistryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigRegistryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ConfigRegistryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["target", "analysis_status", "recommended_config", "last_requested_at", "success_rate"]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[RecommendationSummary]:
        """
        Lists unique exact targets previously analyzed by the selected project with the
        recommendation produced by each target's latest analysis.

        Args:
          search: Case-insensitive substring search over normalized targets, including domain,
              subdomain, and path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/config-registry",
            page=SyncOffsetPagination[RecommendationSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    config_registry_list_params.ConfigRegistryListParams,
                ),
            ),
            model=RecommendationSummary,
        )

    def lookup(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupResponse:
        """
        Returns current global knowledge without resolving DNS, creating an analysis, or
        updating config registry data.

        Args:
          url: Public HTTP(S) URL to look up.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when returning a proxy configuration. When
              omitted, Kernel uses its default country selection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/config-registry/lookup",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                },
                config_registry_lookup_params.ConfigRegistryLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupResponse,
        )

    def resolve(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        intent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRegistryResponse:
        """
        Explicitly starts or retries a project-scoped background analysis while
        preserving current global knowledge when available. Use
        `/config-registry/lookup` for side-effect-free reads.

        Args:
          url: Public HTTP(S) URL to refresh.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when searching for or returning a proxy
              configuration. Kernel may test a subset of allowed countries. When omitted,
              Kernel uses its default country selection.

          intent: Plain-language description of the workload you intend to run against this
              target, in a sentence or two. Requires an https target, because the pass treats
              any non-HTTPS destination as off-site and will not drive an http one. Kernel
              uses it to drive the browser further into the site, where it can observe
              protections that only appear once a session interacts. When this target already
              has a recommended configuration, the run confirms that one instead of
              re-deriving the whole matrix, so supplying an intent narrows what can be
              recommended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/config-registry/resolve",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                    "intent": intent,
                },
                config_registry_resolve_params.ConfigRegistryResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRegistryResponse,
        )


class AsyncConfigRegistryResource(AsyncAPIResource):
    """Resolve browser and proxy recommendations for bot-protected sites."""

    @cached_property
    def analyses(self) -> AsyncAnalysesResource:
        """Resolve browser and proxy recommendations for bot-protected sites."""
        return AsyncAnalysesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigRegistryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigRegistryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncConfigRegistryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["target", "analysis_status", "recommended_config", "last_requested_at", "success_rate"]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RecommendationSummary, AsyncOffsetPagination[RecommendationSummary]]:
        """
        Lists unique exact targets previously analyzed by the selected project with the
        recommendation produced by each target's latest analysis.

        Args:
          search: Case-insensitive substring search over normalized targets, including domain,
              subdomain, and path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/config-registry",
            page=AsyncOffsetPagination[RecommendationSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    config_registry_list_params.ConfigRegistryListParams,
                ),
            ),
            model=RecommendationSummary,
        )

    async def lookup(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupResponse:
        """
        Returns current global knowledge without resolving DNS, creating an analysis, or
        updating config registry data.

        Args:
          url: Public HTTP(S) URL to look up.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when returning a proxy configuration. When
              omitted, Kernel uses its default country selection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/config-registry/lookup",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                },
                config_registry_lookup_params.ConfigRegistryLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupResponse,
        )

    async def resolve(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        intent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRegistryResponse:
        """
        Explicitly starts or retries a project-scoped background analysis while
        preserving current global knowledge when available. Use
        `/config-registry/lookup` for side-effect-free reads.

        Args:
          url: Public HTTP(S) URL to refresh.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when searching for or returning a proxy
              configuration. Kernel may test a subset of allowed countries. When omitted,
              Kernel uses its default country selection.

          intent: Plain-language description of the workload you intend to run against this
              target, in a sentence or two. Requires an https target, because the pass treats
              any non-HTTPS destination as off-site and will not drive an http one. Kernel
              uses it to drive the browser further into the site, where it can observe
              protections that only appear once a session interacts. When this target already
              has a recommended configuration, the run confirms that one instead of
              re-deriving the whole matrix, so supplying an intent narrows what can be
              recommended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/config-registry/resolve",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                    "intent": intent,
                },
                config_registry_resolve_params.ConfigRegistryResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRegistryResponse,
        )


class ConfigRegistryResourceWithRawResponse:
    def __init__(self, config_registry: ConfigRegistryResource) -> None:
        self._config_registry = config_registry

        self.list = to_raw_response_wrapper(
            config_registry.list,
        )
        self.lookup = to_raw_response_wrapper(
            config_registry.lookup,
        )
        self.resolve = to_raw_response_wrapper(
            config_registry.resolve,
        )

    @cached_property
    def analyses(self) -> AnalysesResourceWithRawResponse:
        """Resolve browser and proxy recommendations for bot-protected sites."""
        return AnalysesResourceWithRawResponse(self._config_registry.analyses)


class AsyncConfigRegistryResourceWithRawResponse:
    def __init__(self, config_registry: AsyncConfigRegistryResource) -> None:
        self._config_registry = config_registry

        self.list = async_to_raw_response_wrapper(
            config_registry.list,
        )
        self.lookup = async_to_raw_response_wrapper(
            config_registry.lookup,
        )
        self.resolve = async_to_raw_response_wrapper(
            config_registry.resolve,
        )

    @cached_property
    def analyses(self) -> AsyncAnalysesResourceWithRawResponse:
        """Resolve browser and proxy recommendations for bot-protected sites."""
        return AsyncAnalysesResourceWithRawResponse(self._config_registry.analyses)


class ConfigRegistryResourceWithStreamingResponse:
    def __init__(self, config_registry: ConfigRegistryResource) -> None:
        self._config_registry = config_registry

        self.list = to_streamed_response_wrapper(
            config_registry.list,
        )
        self.lookup = to_streamed_response_wrapper(
            config_registry.lookup,
        )
        self.resolve = to_streamed_response_wrapper(
            config_registry.resolve,
        )

    @cached_property
    def analyses(self) -> AnalysesResourceWithStreamingResponse:
        """Resolve browser and proxy recommendations for bot-protected sites."""
        return AnalysesResourceWithStreamingResponse(self._config_registry.analyses)


class AsyncConfigRegistryResourceWithStreamingResponse:
    def __init__(self, config_registry: AsyncConfigRegistryResource) -> None:
        self._config_registry = config_registry

        self.list = async_to_streamed_response_wrapper(
            config_registry.list,
        )
        self.lookup = async_to_streamed_response_wrapper(
            config_registry.lookup,
        )
        self.resolve = async_to_streamed_response_wrapper(
            config_registry.resolve,
        )

    @cached_property
    def analyses(self) -> AsyncAnalysesResourceWithStreamingResponse:
        """Resolve browser and proxy recommendations for bot-protected sites."""
        return AsyncAnalysesResourceWithStreamingResponse(self._config_registry.analyses)
