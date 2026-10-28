# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.telemetry import destination_list_params, destination_create_params, destination_update_params
from ...types.telemetry.otlp_destination import OtlpDestination

__all__ = ["DestinationsResource", "AsyncDestinationsResource"]


class DestinationsResource(SyncAPIResource):
    """
    Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
    """

    @cached_property
    def with_raw_response(self) -> DestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return DestinationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        endpoint: str,
        name: str,
        description: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OtlpDestination:
        """Create an OTLP export destination in the authenticated organization.

        Names must
        be unique within the organization. Requires an organization-scoped credential or
        dashboard authentication; project-scoped credentials receive a 403.

        Args:
          endpoint: Base endpoint of the OTLP/HTTP collector, without a signal path. Kernel appends
              the signal path itself, so pass `https://api.honeycomb.io` rather than
              `https://api.honeycomb.io/v1/logs`. If your provider's docs give you a
              signal-specific URL, drop the trailing `/v1/logs`, `/v1/traces`, or
              `/v1/metrics` — an endpoint that already carries one is rejected.

              Must be http or https, must resolve to a public address, and must carry no query
              string or fragment. Examples: `https://api.honeycomb.io`,
              `https://otlp-gateway-prod-us-east-0.grafana.net/otlp`,
              `https://otlp.datadoghq.com` (Datadog's OTLP intake for US1, not its logs
              intake).

          name: Unique within the organization.

          headers: Headers sent with each export request, typically an ingestion key. Encrypted at
              rest and returned redacted. Names and values must be valid HTTP header tokens,
              and the names and values together cannot exceed 8192 bytes. Names are matched
              case-insensitively and stored canonicalized, so supplying two spellings of one
              header is rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/telemetry/destinations",
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "name": name,
                    "description": description,
                    "headers": headers,
                },
                destination_create_params.DestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OtlpDestination,
        )

    def retrieve(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtlpDestination:
        """
        Retrieve a customer-visible OTLP destination in the authenticated organization
        by its ID or name. Project-scoped credentials can retrieve these destinations
        for selection by workloads in their project. Non-dashboard reads return header
        values redacted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            path_template("/telemetry/destinations/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtlpDestination,
        )

    def update(
        self,
        id_or_name: str,
        *,
        description: str | Omit = omit,
        endpoint: str | Omit = omit,
        headers: Dict[str, Optional[str]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OtlpDestination:
        """Update an OTLP destination.

        Sessions already exporting to it pick up the new
        values without restarting, which makes this the way to rotate credentials
        without interrupting export.

        Names must be unique within the organization. Renaming is refused with a 409
        while a managed auth connection selects this destination by name, since that
        connection resolves the name on every login. Every other field, including
        `headers`, stays editable. Requires an organization-scoped credential or
        dashboard authentication; project-scoped credentials receive a 403.

        Args:
          endpoint: Base endpoint of the OTLP/HTTP collector, without a signal path. Same rules as
              on create.

          headers: Edits stored headers key by key rather than replacing the map. A string value
              adds or replaces that header, `null` deletes it, and any key you omit is left as
              it is. Names are matched case-insensitively, so `authorization` replaces a
              stored `Authorization` rather than adding a second entry. This is the credential
              rotation path; sessions already exporting pick up the new values without
              restarting. Names and values must be valid HTTP header tokens, and the names and
              values together cannot exceed 8192 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._patch(
            path_template("/telemetry/destinations/{id_or_name}", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "description": description,
                    "endpoint": endpoint,
                    "headers": headers,
                    "name": name,
                },
                destination_update_params.DestinationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OtlpDestination,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[OtlpDestination]:
        """List customer-visible OTLP export destinations in the authenticated
        organization.

        Project-scoped credentials can list these destinations for
        selection by workloads in their project. Non-dashboard reads return header
        values redacted.

        Args:
          limit: Limit the number of destinations to return.

          name: Exact-match filter on destination name using the database collation. In
              production, matching is case- and accent-insensitive.

          offset: Offset the number of destinations to return.

          query: Case-insensitive substring match against destination name or endpoint. IDs match
              by exact value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/telemetry/destinations",
            page=SyncOffsetPagination[OtlpDestination],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "query": query,
                    },
                    destination_list_params.DestinationListParams,
                ),
            ),
            model=OtlpDestination,
        )

    def delete(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Delete an OTLP destination.

        Sessions bound to it are still exporting, so the
        delete is refused with a 409 while any exist; either wait for those sessions to
        end or delete them first. It is refused the same way while a managed auth
        connection still selects it, because that connection re-resolves the destination
        on every login, and while a managed auth login using it is still in progress.
        Requires an organization-scoped credential or dashboard authentication;
        project-scoped credentials receive a 403.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/telemetry/destinations/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncDestinationsResource(AsyncAPIResource):
    """
    Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncDestinationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        endpoint: str,
        name: str,
        description: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OtlpDestination:
        """Create an OTLP export destination in the authenticated organization.

        Names must
        be unique within the organization. Requires an organization-scoped credential or
        dashboard authentication; project-scoped credentials receive a 403.

        Args:
          endpoint: Base endpoint of the OTLP/HTTP collector, without a signal path. Kernel appends
              the signal path itself, so pass `https://api.honeycomb.io` rather than
              `https://api.honeycomb.io/v1/logs`. If your provider's docs give you a
              signal-specific URL, drop the trailing `/v1/logs`, `/v1/traces`, or
              `/v1/metrics` — an endpoint that already carries one is rejected.

              Must be http or https, must resolve to a public address, and must carry no query
              string or fragment. Examples: `https://api.honeycomb.io`,
              `https://otlp-gateway-prod-us-east-0.grafana.net/otlp`,
              `https://otlp.datadoghq.com` (Datadog's OTLP intake for US1, not its logs
              intake).

          name: Unique within the organization.

          headers: Headers sent with each export request, typically an ingestion key. Encrypted at
              rest and returned redacted. Names and values must be valid HTTP header tokens,
              and the names and values together cannot exceed 8192 bytes. Names are matched
              case-insensitively and stored canonicalized, so supplying two spellings of one
              header is rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/telemetry/destinations",
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "name": name,
                    "description": description,
                    "headers": headers,
                },
                destination_create_params.DestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OtlpDestination,
        )

    async def retrieve(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtlpDestination:
        """
        Retrieve a customer-visible OTLP destination in the authenticated organization
        by its ID or name. Project-scoped credentials can retrieve these destinations
        for selection by workloads in their project. Non-dashboard reads return header
        values redacted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            path_template("/telemetry/destinations/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtlpDestination,
        )

    async def update(
        self,
        id_or_name: str,
        *,
        description: str | Omit = omit,
        endpoint: str | Omit = omit,
        headers: Dict[str, Optional[str]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OtlpDestination:
        """Update an OTLP destination.

        Sessions already exporting to it pick up the new
        values without restarting, which makes this the way to rotate credentials
        without interrupting export.

        Names must be unique within the organization. Renaming is refused with a 409
        while a managed auth connection selects this destination by name, since that
        connection resolves the name on every login. Every other field, including
        `headers`, stays editable. Requires an organization-scoped credential or
        dashboard authentication; project-scoped credentials receive a 403.

        Args:
          endpoint: Base endpoint of the OTLP/HTTP collector, without a signal path. Same rules as
              on create.

          headers: Edits stored headers key by key rather than replacing the map. A string value
              adds or replaces that header, `null` deletes it, and any key you omit is left as
              it is. Names are matched case-insensitively, so `authorization` replaces a
              stored `Authorization` rather than adding a second entry. This is the credential
              rotation path; sessions already exporting pick up the new values without
              restarting. Names and values must be valid HTTP header tokens, and the names and
              values together cannot exceed 8192 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._patch(
            path_template("/telemetry/destinations/{id_or_name}", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "endpoint": endpoint,
                    "headers": headers,
                    "name": name,
                },
                destination_update_params.DestinationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OtlpDestination,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OtlpDestination, AsyncOffsetPagination[OtlpDestination]]:
        """List customer-visible OTLP export destinations in the authenticated
        organization.

        Project-scoped credentials can list these destinations for
        selection by workloads in their project. Non-dashboard reads return header
        values redacted.

        Args:
          limit: Limit the number of destinations to return.

          name: Exact-match filter on destination name using the database collation. In
              production, matching is case- and accent-insensitive.

          offset: Offset the number of destinations to return.

          query: Case-insensitive substring match against destination name or endpoint. IDs match
              by exact value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/telemetry/destinations",
            page=AsyncOffsetPagination[OtlpDestination],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "query": query,
                    },
                    destination_list_params.DestinationListParams,
                ),
            ),
            model=OtlpDestination,
        )

    async def delete(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Delete an OTLP destination.

        Sessions bound to it are still exporting, so the
        delete is refused with a 409 while any exist; either wait for those sessions to
        end or delete them first. It is refused the same way while a managed auth
        connection still selects it, because that connection re-resolves the destination
        on every login, and while a managed auth login using it is still in progress.
        Requires an organization-scoped credential or dashboard authentication;
        project-scoped credentials receive a 403.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/telemetry/destinations/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class DestinationsResourceWithRawResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

        self.create = to_raw_response_wrapper(
            destinations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            destinations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            destinations.update,
        )
        self.list = to_raw_response_wrapper(
            destinations.list,
        )
        self.delete = to_raw_response_wrapper(
            destinations.delete,
        )


class AsyncDestinationsResourceWithRawResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

        self.create = async_to_raw_response_wrapper(
            destinations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            destinations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            destinations.update,
        )
        self.list = async_to_raw_response_wrapper(
            destinations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            destinations.delete,
        )


class DestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

        self.create = to_streamed_response_wrapper(
            destinations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            destinations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            destinations.update,
        )
        self.list = to_streamed_response_wrapper(
            destinations.list,
        )
        self.delete = to_streamed_response_wrapper(
            destinations.delete,
        )


class AsyncDestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

        self.create = async_to_streamed_response_wrapper(
            destinations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            destinations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            destinations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            destinations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            destinations.delete,
        )
