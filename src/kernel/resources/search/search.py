# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import search_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .contents import (
    ContentsResource,
    AsyncContentsResource,
    ContentsResourceWithRawResponse,
    AsyncContentsResourceWithRawResponse,
    ContentsResourceWithStreamingResponse,
    AsyncContentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .providers import (
    ProvidersResource,
    AsyncProvidersResource,
    ProvidersResourceWithRawResponse,
    AsyncProvidersResourceWithRawResponse,
    ProvidersResourceWithStreamingResponse,
    AsyncProvidersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.search.search import Search
from ...types.strategy_param import StrategyParam

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """Search the web and retrieve content for selected results."""

    @cached_property
    def contents(self) -> ContentsResource:
        """Search the web and retrieve content for selected results."""
        return ContentsResource(self._client)

    @cached_property
    def providers(self) -> ProvidersResource:
        """Search the web and retrieve content for selected results."""
        return ProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: str,
        content: search_create_params.Content | Omit = omit,
        country: str | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        include_raw: bool | Omit = omit,
        language: str | Omit = omit,
        max_results: int | Omit = omit,
        recency: Literal["hour", "day", "week", "month", "year"] | Omit = omit,
        safe_search: Literal["off", "moderate", "strict"] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        strategy: StrategyParam | Omit = omit,
        strict_params: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Search:
        """Returns ranked results from one serving provider.

        The default strategy selects a
        provider that supports the requested options. The fallback strategy tries
        providers in the supplied order. Results are not blended across providers.
        Portable filters may be approximated or omitted according to provider
        capabilities; warnings describe those outcomes unless strict_params is true.
        Native options apply only to their selected provider.

        Args:
          query: Primary search query. A provider-native multi-query option applies only to that
              provider; other providers in a fallback chain receive this query.

          content: Optional portable content retrieval. Pass true for defaults or an options
              object. Omission never starts Kernel browser work; provider-supplied content is
              still returned when available, including when requested through native options.
              Both inline and deferred retrieval use the same options schema.

          country: ISO 3166-1 alpha-2 search locale preference.

          end_date: Inclusive publication-date upper bound; must not precede start_date. If recency
              is also supplied, recency takes precedence with a warning. Unsupported or
              approximated filtering is reported, or rejected under strict_params.

          exclude_domains: Hostname exclusions, with the same best-effort/strict behavior as
              include_domains. Provider-specific combinations that cannot be represented are
              reported via warnings or rejected in strict mode.

          include_domains: Hostname inclusion preference, matching a hostname and its subdomains. Empty
              means unrestricted. Translated, emulated, or dropped with a warning according to
              provider capability unless strict_params is true. Native boost modes remain
              advisory and are identified in warnings.

          include_raw: Include untouched per-result payloads and the full serving-provider response in
              raw fields. Off by default; native top-level outputs such as answer remain
              available without it.

          language: BCP 47 search language preference.

          max_results: Requested result count from 1 through 100. The effective count is clamped to the
              serving provider's cap with a warning. Effective native counts are the lower of
              this limit and supplied provider-native count aliases. Strict mode rejects
              unsupported counts.

          recency: Relative search window. Takes precedence over start_date/end_date with a warning
              if both are set. Provider-native recency behavior is retained, including
              documented hour-to-day widening. Unsupported filters are rejected only in strict
              mode.

          safe_search: Optional safety preference. Omit to use provider defaults. Unsupported values
              are dropped with a warning unless strict_params is true. A search filter is not
              an authorization boundary.

          start_date: Inclusive publication-date lower bound. If recency is also supplied, recency
              takes precedence with a warning. Provider date semantics, precision, and
              unsupported filters are reported; unknown source dates are not fabricated or
              universally post-filtered.

          strategy: Omitted strategy defaults to auto.

          strict_params: When false, unsupported portable parameters are omitted and approximations are
              described in warnings. When true, every supplied portable parameter must be
              honored exactly. Requests that cannot be served with those parameters are
              rejected. This does not guarantee identical rankings or document timestamps
              across indexes. Authentication and project isolation are always enforced.

          timeout_ms: Overall deadline across search attempts and inline retrieval. No new attempt
              starts after the deadline. Completed search results survive inline retrieval
              timeouts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search",
            body=maybe_transform(
                {
                    "query": query,
                    "content": content,
                    "country": country,
                    "end_date": end_date,
                    "exclude_domains": exclude_domains,
                    "include_domains": include_domains,
                    "include_raw": include_raw,
                    "language": language,
                    "max_results": max_results,
                    "recency": recency,
                    "safe_search": safe_search,
                    "start_date": start_date,
                    "strategy": strategy,
                    "strict_params": strict_params,
                    "timeout_ms": timeout_ms,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Search,
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
    ) -> Search:
        """
        Returns the retained search resource exactly as it was returned by POST /search:
        results, attempts, warnings, usage, and expires_at. No provider is called and
        nothing is billed. Use it to look up a search by ID for debugging, cost review,
        or to recover result IDs before calling the contents endpoint. Inline content
        fetched at search time is included; content fetched later through the contents
        endpoint is not merged in. Missing, expired, or inaccessible searches
        return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/search/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Search,
        )


class AsyncSearchResource(AsyncAPIResource):
    """Search the web and retrieve content for selected results."""

    @cached_property
    def contents(self) -> AsyncContentsResource:
        """Search the web and retrieve content for selected results."""
        return AsyncContentsResource(self._client)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        """Search the web and retrieve content for selected results."""
        return AsyncProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: str,
        content: search_create_params.Content | Omit = omit,
        country: str | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        include_raw: bool | Omit = omit,
        language: str | Omit = omit,
        max_results: int | Omit = omit,
        recency: Literal["hour", "day", "week", "month", "year"] | Omit = omit,
        safe_search: Literal["off", "moderate", "strict"] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        strategy: StrategyParam | Omit = omit,
        strict_params: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Search:
        """Returns ranked results from one serving provider.

        The default strategy selects a
        provider that supports the requested options. The fallback strategy tries
        providers in the supplied order. Results are not blended across providers.
        Portable filters may be approximated or omitted according to provider
        capabilities; warnings describe those outcomes unless strict_params is true.
        Native options apply only to their selected provider.

        Args:
          query: Primary search query. A provider-native multi-query option applies only to that
              provider; other providers in a fallback chain receive this query.

          content: Optional portable content retrieval. Pass true for defaults or an options
              object. Omission never starts Kernel browser work; provider-supplied content is
              still returned when available, including when requested through native options.
              Both inline and deferred retrieval use the same options schema.

          country: ISO 3166-1 alpha-2 search locale preference.

          end_date: Inclusive publication-date upper bound; must not precede start_date. If recency
              is also supplied, recency takes precedence with a warning. Unsupported or
              approximated filtering is reported, or rejected under strict_params.

          exclude_domains: Hostname exclusions, with the same best-effort/strict behavior as
              include_domains. Provider-specific combinations that cannot be represented are
              reported via warnings or rejected in strict mode.

          include_domains: Hostname inclusion preference, matching a hostname and its subdomains. Empty
              means unrestricted. Translated, emulated, or dropped with a warning according to
              provider capability unless strict_params is true. Native boost modes remain
              advisory and are identified in warnings.

          include_raw: Include untouched per-result payloads and the full serving-provider response in
              raw fields. Off by default; native top-level outputs such as answer remain
              available without it.

          language: BCP 47 search language preference.

          max_results: Requested result count from 1 through 100. The effective count is clamped to the
              serving provider's cap with a warning. Effective native counts are the lower of
              this limit and supplied provider-native count aliases. Strict mode rejects
              unsupported counts.

          recency: Relative search window. Takes precedence over start_date/end_date with a warning
              if both are set. Provider-native recency behavior is retained, including
              documented hour-to-day widening. Unsupported filters are rejected only in strict
              mode.

          safe_search: Optional safety preference. Omit to use provider defaults. Unsupported values
              are dropped with a warning unless strict_params is true. A search filter is not
              an authorization boundary.

          start_date: Inclusive publication-date lower bound. If recency is also supplied, recency
              takes precedence with a warning. Provider date semantics, precision, and
              unsupported filters are reported; unknown source dates are not fabricated or
              universally post-filtered.

          strategy: Omitted strategy defaults to auto.

          strict_params: When false, unsupported portable parameters are omitted and approximations are
              described in warnings. When true, every supplied portable parameter must be
              honored exactly. Requests that cannot be served with those parameters are
              rejected. This does not guarantee identical rankings or document timestamps
              across indexes. Authentication and project isolation are always enforced.

          timeout_ms: Overall deadline across search attempts and inline retrieval. No new attempt
              starts after the deadline. Completed search results survive inline retrieval
              timeouts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "content": content,
                    "country": country,
                    "end_date": end_date,
                    "exclude_domains": exclude_domains,
                    "include_domains": include_domains,
                    "include_raw": include_raw,
                    "language": language,
                    "max_results": max_results,
                    "recency": recency,
                    "safe_search": safe_search,
                    "start_date": start_date,
                    "strategy": strategy,
                    "strict_params": strict_params,
                    "timeout_ms": timeout_ms,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Search,
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
    ) -> Search:
        """
        Returns the retained search resource exactly as it was returned by POST /search:
        results, attempts, warnings, usage, and expires_at. No provider is called and
        nothing is billed. Use it to look up a search by ID for debugging, cost review,
        or to recover result IDs before calling the contents endpoint. Inline content
        fetched at search time is included; content fetched later through the contents
        endpoint is not merged in. Missing, expired, or inaccessible searches
        return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/search/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Search,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_raw_response_wrapper(
            search.create,
        )
        self.retrieve = to_raw_response_wrapper(
            search.retrieve,
        )

    @cached_property
    def contents(self) -> ContentsResourceWithRawResponse:
        """Search the web and retrieve content for selected results."""
        return ContentsResourceWithRawResponse(self._search.contents)

    @cached_property
    def providers(self) -> ProvidersResourceWithRawResponse:
        """Search the web and retrieve content for selected results."""
        return ProvidersResourceWithRawResponse(self._search.providers)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_raw_response_wrapper(
            search.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            search.retrieve,
        )

    @cached_property
    def contents(self) -> AsyncContentsResourceWithRawResponse:
        """Search the web and retrieve content for selected results."""
        return AsyncContentsResourceWithRawResponse(self._search.contents)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithRawResponse:
        """Search the web and retrieve content for selected results."""
        return AsyncProvidersResourceWithRawResponse(self._search.providers)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_streamed_response_wrapper(
            search.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            search.retrieve,
        )

    @cached_property
    def contents(self) -> ContentsResourceWithStreamingResponse:
        """Search the web and retrieve content for selected results."""
        return ContentsResourceWithStreamingResponse(self._search.contents)

    @cached_property
    def providers(self) -> ProvidersResourceWithStreamingResponse:
        """Search the web and retrieve content for selected results."""
        return ProvidersResourceWithStreamingResponse(self._search.providers)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_streamed_response_wrapper(
            search.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            search.retrieve,
        )

    @cached_property
    def contents(self) -> AsyncContentsResourceWithStreamingResponse:
        """Search the web and retrieve content for selected results."""
        return AsyncContentsResourceWithStreamingResponse(self._search.contents)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithStreamingResponse:
        """Search the web and retrieve content for selected results."""
        return AsyncProvidersResourceWithStreamingResponse(self._search.providers)
