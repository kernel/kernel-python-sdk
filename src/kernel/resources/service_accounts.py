# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import service_account_list_params, service_account_create_params, service_account_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.service_account import ServiceAccount

__all__ = ["ServiceAccountsResource", "AsyncServiceAccountsResource"]


class ServiceAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ServiceAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ServiceAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ServiceAccount:
        """Organization credential administrators only.

        No external namespace-ownership or
        staff approval is required. New trust resources default disabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/org/service_accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                service_account_create_params.ServiceAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ServiceAccount,
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
    ) -> ServiceAccount:
        """Any signed-in member of the organization can read this.

        API keys cannot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/org/service_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceAccount,
        )

    def update(
        self,
        id: str,
        *,
        expected_version: int,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ServiceAccount:
        """
        Update a service account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/org/service_accounts/{id}", id=id),
            body=maybe_transform(
                {
                    "expected_version": expected_version,
                    "description": description,
                    "name": name,
                },
                service_account_update_params.ServiceAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ServiceAccount,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        status: Literal["active", "archived", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ServiceAccount]:
        """Any signed-in member of the organization can read this.

        API keys cannot.

        Args:
          query: Case-insensitive substring match against name or description; exact ID match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/org/service_accounts",
            page=SyncOffsetPagination[ServiceAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "status": status,
                    },
                    service_account_list_params.ServiceAccountListParams,
                ),
            ),
            model=ServiceAccount,
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
        idempotency_key: str | None = None,
    ) -> None:
        """
        Retains history and invalidates associated authority within the documented
        status bound. Does not delete created browser resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/org/service_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncServiceAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncServiceAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ServiceAccount:
        """Organization credential administrators only.

        No external namespace-ownership or
        staff approval is required. New trust resources default disabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/org/service_accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                service_account_create_params.ServiceAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ServiceAccount,
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
    ) -> ServiceAccount:
        """Any signed-in member of the organization can read this.

        API keys cannot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/org/service_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceAccount,
        )

    async def update(
        self,
        id: str,
        *,
        expected_version: int,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ServiceAccount:
        """
        Update a service account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/org/service_accounts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "expected_version": expected_version,
                    "description": description,
                    "name": name,
                },
                service_account_update_params.ServiceAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ServiceAccount,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        status: Literal["active", "archived", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ServiceAccount, AsyncOffsetPagination[ServiceAccount]]:
        """Any signed-in member of the organization can read this.

        API keys cannot.

        Args:
          query: Case-insensitive substring match against name or description; exact ID match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/org/service_accounts",
            page=AsyncOffsetPagination[ServiceAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "status": status,
                    },
                    service_account_list_params.ServiceAccountListParams,
                ),
            ),
            model=ServiceAccount,
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
        idempotency_key: str | None = None,
    ) -> None:
        """
        Retains history and invalidates associated authority within the documented
        status bound. Does not delete created browser resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/org/service_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class ServiceAccountsResourceWithRawResponse:
    def __init__(self, service_accounts: ServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = to_raw_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            service_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            service_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            service_accounts.delete,
        )


class AsyncServiceAccountsResourceWithRawResponse:
    def __init__(self, service_accounts: AsyncServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = async_to_raw_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            service_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            service_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service_accounts.delete,
        )


class ServiceAccountsResourceWithStreamingResponse:
    def __init__(self, service_accounts: ServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = to_streamed_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            service_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            service_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            service_accounts.delete,
        )


class AsyncServiceAccountsResourceWithStreamingResponse:
    def __init__(self, service_accounts: AsyncServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = async_to_streamed_response_wrapper(
            service_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            service_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            service_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            service_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_accounts.delete,
        )
