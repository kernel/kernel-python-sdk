# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    WorkloadIdentityPresetType,
    workload_identity_issuer_list_params,
    workload_identity_issuer_create_params,
    workload_identity_issuer_update_params,
)
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
from ..types.workload_identity_issuer import WorkloadIdentityIssuer
from ..types.workload_identity_preset_type import WorkloadIdentityPresetType
from ..types.workload_identity_issuer_key_check import WorkloadIdentityIssuerKeyCheck
from ..types.workload_identity_key_source_param import WorkloadIdentityKeySourceParam
from ..types.workload_identity_token_validation_param import WorkloadIdentityTokenValidationParam

__all__ = ["WorkloadIdentityIssuersResource", "AsyncWorkloadIdentityIssuersResource"]


class WorkloadIdentityIssuersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkloadIdentityIssuersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WorkloadIdentityIssuersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkloadIdentityIssuersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return WorkloadIdentityIssuersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        issuer_url: str | Omit = omit,
        jwks: WorkloadIdentityKeySourceParam | Omit = omit,
        preset_type: WorkloadIdentityPresetType | Omit = omit,
        token_validation: WorkloadIdentityTokenValidationParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityIssuer:
        """Organization credential administrators only.

        No external namespace-ownership or
        staff approval is required. New trust resources default disabled.

        Args:
          issuer_url: Exact expected signed issuer. Optional for github_actions and google_cloud,
              which each have one fixed issuer.

          preset_type: The kind of identity provider. GitHub Actions, Google Cloud and Microsoft Entra
              issuers are recognized by their issuer URL and must use their own type. Defaults
              to the type the issuer URL belongs to, or custom_oidc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/org/workload_identity_issuers",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "enabled": enabled,
                    "issuer_url": issuer_url,
                    "jwks": jwks,
                    "preset_type": preset_type,
                    "token_validation": token_validation,
                },
                workload_identity_issuer_create_params.WorkloadIdentityIssuerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityIssuer,
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
    ) -> WorkloadIdentityIssuer:
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
            path_template("/org/workload_identity_issuers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkloadIdentityIssuer,
        )

    def update(
        self,
        id: str,
        *,
        expected_version: int,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        issuer_url: str | Omit = omit,
        jwks: WorkloadIdentityKeySourceParam | Omit = omit,
        name: str | Omit = omit,
        preset_type: WorkloadIdentityPresetType | Omit = omit,
        token_validation: WorkloadIdentityTokenValidationParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityIssuer:
        """
        Update a workload identity issuer

        Args:
          issuer_url: Exact expected signed issuer. Optional for github_actions and google_cloud,
              which each have one fixed issuer.

          preset_type: The kind of identity provider. GitHub Actions, Google Cloud and Microsoft Entra
              issuers are recognized by their issuer URL and must use their own type. Defaults
              to the type the issuer URL belongs to, or custom_oidc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/org/workload_identity_issuers/{id}", id=id),
            body=maybe_transform(
                {
                    "expected_version": expected_version,
                    "description": description,
                    "enabled": enabled,
                    "issuer_url": issuer_url,
                    "jwks": jwks,
                    "name": name,
                    "preset_type": preset_type,
                    "token_validation": token_validation,
                },
                workload_identity_issuer_update_params.WorkloadIdentityIssuerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityIssuer,
        )

    def list(
        self,
        *,
        enabled: bool | Omit = omit,
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
    ) -> SyncOffsetPagination[WorkloadIdentityIssuer]:
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
            "/org/workload_identity_issuers",
            page=SyncOffsetPagination[WorkloadIdentityIssuer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "status": status,
                    },
                    workload_identity_issuer_list_params.WorkloadIdentityIssuerListParams,
                ),
            ),
            model=WorkloadIdentityIssuer,
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
            path_template("/org/workload_identity_issuers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def verify(
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
    ) -> WorkloadIdentityIssuerKeyCheck:
        """Read-only.

        Does not enable trust, approve namespace ownership, create a grant or
        issue credentials.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/org/workload_identity_issuers/{id}/verify", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityIssuerKeyCheck,
        )


class AsyncWorkloadIdentityIssuersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkloadIdentityIssuersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkloadIdentityIssuersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkloadIdentityIssuersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncWorkloadIdentityIssuersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        issuer_url: str | Omit = omit,
        jwks: WorkloadIdentityKeySourceParam | Omit = omit,
        preset_type: WorkloadIdentityPresetType | Omit = omit,
        token_validation: WorkloadIdentityTokenValidationParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityIssuer:
        """Organization credential administrators only.

        No external namespace-ownership or
        staff approval is required. New trust resources default disabled.

        Args:
          issuer_url: Exact expected signed issuer. Optional for github_actions and google_cloud,
              which each have one fixed issuer.

          preset_type: The kind of identity provider. GitHub Actions, Google Cloud and Microsoft Entra
              issuers are recognized by their issuer URL and must use their own type. Defaults
              to the type the issuer URL belongs to, or custom_oidc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/org/workload_identity_issuers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "enabled": enabled,
                    "issuer_url": issuer_url,
                    "jwks": jwks,
                    "preset_type": preset_type,
                    "token_validation": token_validation,
                },
                workload_identity_issuer_create_params.WorkloadIdentityIssuerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityIssuer,
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
    ) -> WorkloadIdentityIssuer:
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
            path_template("/org/workload_identity_issuers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkloadIdentityIssuer,
        )

    async def update(
        self,
        id: str,
        *,
        expected_version: int,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        issuer_url: str | Omit = omit,
        jwks: WorkloadIdentityKeySourceParam | Omit = omit,
        name: str | Omit = omit,
        preset_type: WorkloadIdentityPresetType | Omit = omit,
        token_validation: WorkloadIdentityTokenValidationParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityIssuer:
        """
        Update a workload identity issuer

        Args:
          issuer_url: Exact expected signed issuer. Optional for github_actions and google_cloud,
              which each have one fixed issuer.

          preset_type: The kind of identity provider. GitHub Actions, Google Cloud and Microsoft Entra
              issuers are recognized by their issuer URL and must use their own type. Defaults
              to the type the issuer URL belongs to, or custom_oidc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/org/workload_identity_issuers/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "expected_version": expected_version,
                    "description": description,
                    "enabled": enabled,
                    "issuer_url": issuer_url,
                    "jwks": jwks,
                    "name": name,
                    "preset_type": preset_type,
                    "token_validation": token_validation,
                },
                workload_identity_issuer_update_params.WorkloadIdentityIssuerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityIssuer,
        )

    def list(
        self,
        *,
        enabled: bool | Omit = omit,
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
    ) -> AsyncPaginator[WorkloadIdentityIssuer, AsyncOffsetPagination[WorkloadIdentityIssuer]]:
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
            "/org/workload_identity_issuers",
            page=AsyncOffsetPagination[WorkloadIdentityIssuer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "status": status,
                    },
                    workload_identity_issuer_list_params.WorkloadIdentityIssuerListParams,
                ),
            ),
            model=WorkloadIdentityIssuer,
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
            path_template("/org/workload_identity_issuers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def verify(
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
    ) -> WorkloadIdentityIssuerKeyCheck:
        """Read-only.

        Does not enable trust, approve namespace ownership, create a grant or
        issue credentials.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/org/workload_identity_issuers/{id}/verify", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityIssuerKeyCheck,
        )


class WorkloadIdentityIssuersResourceWithRawResponse:
    def __init__(self, workload_identity_issuers: WorkloadIdentityIssuersResource) -> None:
        self._workload_identity_issuers = workload_identity_issuers

        self.create = to_raw_response_wrapper(
            workload_identity_issuers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workload_identity_issuers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workload_identity_issuers.update,
        )
        self.list = to_raw_response_wrapper(
            workload_identity_issuers.list,
        )
        self.delete = to_raw_response_wrapper(
            workload_identity_issuers.delete,
        )
        self.verify = to_raw_response_wrapper(
            workload_identity_issuers.verify,
        )


class AsyncWorkloadIdentityIssuersResourceWithRawResponse:
    def __init__(self, workload_identity_issuers: AsyncWorkloadIdentityIssuersResource) -> None:
        self._workload_identity_issuers = workload_identity_issuers

        self.create = async_to_raw_response_wrapper(
            workload_identity_issuers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workload_identity_issuers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workload_identity_issuers.update,
        )
        self.list = async_to_raw_response_wrapper(
            workload_identity_issuers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workload_identity_issuers.delete,
        )
        self.verify = async_to_raw_response_wrapper(
            workload_identity_issuers.verify,
        )


class WorkloadIdentityIssuersResourceWithStreamingResponse:
    def __init__(self, workload_identity_issuers: WorkloadIdentityIssuersResource) -> None:
        self._workload_identity_issuers = workload_identity_issuers

        self.create = to_streamed_response_wrapper(
            workload_identity_issuers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workload_identity_issuers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workload_identity_issuers.update,
        )
        self.list = to_streamed_response_wrapper(
            workload_identity_issuers.list,
        )
        self.delete = to_streamed_response_wrapper(
            workload_identity_issuers.delete,
        )
        self.verify = to_streamed_response_wrapper(
            workload_identity_issuers.verify,
        )


class AsyncWorkloadIdentityIssuersResourceWithStreamingResponse:
    def __init__(self, workload_identity_issuers: AsyncWorkloadIdentityIssuersResource) -> None:
        self._workload_identity_issuers = workload_identity_issuers

        self.create = async_to_streamed_response_wrapper(
            workload_identity_issuers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workload_identity_issuers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workload_identity_issuers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workload_identity_issuers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workload_identity_issuers.delete,
        )
        self.verify = async_to_streamed_response_wrapper(
            workload_identity_issuers.verify,
        )
