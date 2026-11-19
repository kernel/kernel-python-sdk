# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    workload_identity_federation_rule_list_params,
    workload_identity_federation_rule_create_params,
    workload_identity_federation_rule_update_params,
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
from ..types.workload_identity_match_param import WorkloadIdentityMatchParam
from ..types.workload_identity_target_param import WorkloadIdentityTargetParam
from ..types.workload_identity_federation_rule import WorkloadIdentityFederationRule
from ..types.workload_identity_authorization_param import WorkloadIdentityAuthorizationParam

__all__ = ["WorkloadIdentityFederationRulesResource", "AsyncWorkloadIdentityFederationRulesResource"]


class WorkloadIdentityFederationRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkloadIdentityFederationRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WorkloadIdentityFederationRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkloadIdentityFederationRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return WorkloadIdentityFederationRulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        authorization: WorkloadIdentityAuthorizationParam,
        expected_audience: str,
        issuer_id: str,
        match: WorkloadIdentityMatchParam,
        name: str,
        target: WorkloadIdentityTargetParam,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityFederationRule:
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
            "/org/workload_identity_federation_rules",
            body=maybe_transform(
                {
                    "authorization": authorization,
                    "expected_audience": expected_audience,
                    "issuer_id": issuer_id,
                    "match": match,
                    "name": name,
                    "target": target,
                    "description": description,
                    "enabled": enabled,
                },
                workload_identity_federation_rule_create_params.WorkloadIdentityFederationRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityFederationRule,
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
    ) -> WorkloadIdentityFederationRule:
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
            path_template("/org/workload_identity_federation_rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkloadIdentityFederationRule,
        )

    def update(
        self,
        id: str,
        *,
        expected_version: int,
        authorization: WorkloadIdentityAuthorizationParam | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        expected_audience: str | Omit = omit,
        issuer_id: str | Omit = omit,
        match: WorkloadIdentityMatchParam | Omit = omit,
        name: str | Omit = omit,
        target: WorkloadIdentityTargetParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityFederationRule:
        """
        Update a workload identity federation rule

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
            path_template("/org/workload_identity_federation_rules/{id}", id=id),
            body=maybe_transform(
                {
                    "expected_version": expected_version,
                    "authorization": authorization,
                    "description": description,
                    "enabled": enabled,
                    "expected_audience": expected_audience,
                    "issuer_id": issuer_id,
                    "match": match,
                    "name": name,
                    "target": target,
                },
                workload_identity_federation_rule_update_params.WorkloadIdentityFederationRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityFederationRule,
        )

    def list(
        self,
        *,
        issuer_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        project_id: str | Omit = omit,
        query: str | Omit = omit,
        service_account_id: str | Omit = omit,
        status: Literal["active", "archived", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[WorkloadIdentityFederationRule]:
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
            "/org/workload_identity_federation_rules",
            page=SyncOffsetPagination[WorkloadIdentityFederationRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "issuer_id": issuer_id,
                        "limit": limit,
                        "offset": offset,
                        "project_id": project_id,
                        "query": query,
                        "service_account_id": service_account_id,
                        "status": status,
                    },
                    workload_identity_federation_rule_list_params.WorkloadIdentityFederationRuleListParams,
                ),
            ),
            model=WorkloadIdentityFederationRule,
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
            path_template("/org/workload_identity_federation_rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncWorkloadIdentityFederationRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkloadIdentityFederationRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkloadIdentityFederationRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkloadIdentityFederationRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncWorkloadIdentityFederationRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        authorization: WorkloadIdentityAuthorizationParam,
        expected_audience: str,
        issuer_id: str,
        match: WorkloadIdentityMatchParam,
        name: str,
        target: WorkloadIdentityTargetParam,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityFederationRule:
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
            "/org/workload_identity_federation_rules",
            body=await async_maybe_transform(
                {
                    "authorization": authorization,
                    "expected_audience": expected_audience,
                    "issuer_id": issuer_id,
                    "match": match,
                    "name": name,
                    "target": target,
                    "description": description,
                    "enabled": enabled,
                },
                workload_identity_federation_rule_create_params.WorkloadIdentityFederationRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityFederationRule,
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
    ) -> WorkloadIdentityFederationRule:
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
            path_template("/org/workload_identity_federation_rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkloadIdentityFederationRule,
        )

    async def update(
        self,
        id: str,
        *,
        expected_version: int,
        authorization: WorkloadIdentityAuthorizationParam | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        expected_audience: str | Omit = omit,
        issuer_id: str | Omit = omit,
        match: WorkloadIdentityMatchParam | Omit = omit,
        name: str | Omit = omit,
        target: WorkloadIdentityTargetParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WorkloadIdentityFederationRule:
        """
        Update a workload identity federation rule

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
            path_template("/org/workload_identity_federation_rules/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "expected_version": expected_version,
                    "authorization": authorization,
                    "description": description,
                    "enabled": enabled,
                    "expected_audience": expected_audience,
                    "issuer_id": issuer_id,
                    "match": match,
                    "name": name,
                    "target": target,
                },
                workload_identity_federation_rule_update_params.WorkloadIdentityFederationRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WorkloadIdentityFederationRule,
        )

    def list(
        self,
        *,
        issuer_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        project_id: str | Omit = omit,
        query: str | Omit = omit,
        service_account_id: str | Omit = omit,
        status: Literal["active", "archived", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkloadIdentityFederationRule, AsyncOffsetPagination[WorkloadIdentityFederationRule]]:
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
            "/org/workload_identity_federation_rules",
            page=AsyncOffsetPagination[WorkloadIdentityFederationRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "issuer_id": issuer_id,
                        "limit": limit,
                        "offset": offset,
                        "project_id": project_id,
                        "query": query,
                        "service_account_id": service_account_id,
                        "status": status,
                    },
                    workload_identity_federation_rule_list_params.WorkloadIdentityFederationRuleListParams,
                ),
            ),
            model=WorkloadIdentityFederationRule,
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
            path_template("/org/workload_identity_federation_rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class WorkloadIdentityFederationRulesResourceWithRawResponse:
    def __init__(self, workload_identity_federation_rules: WorkloadIdentityFederationRulesResource) -> None:
        self._workload_identity_federation_rules = workload_identity_federation_rules

        self.create = to_raw_response_wrapper(
            workload_identity_federation_rules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workload_identity_federation_rules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workload_identity_federation_rules.update,
        )
        self.list = to_raw_response_wrapper(
            workload_identity_federation_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            workload_identity_federation_rules.delete,
        )


class AsyncWorkloadIdentityFederationRulesResourceWithRawResponse:
    def __init__(self, workload_identity_federation_rules: AsyncWorkloadIdentityFederationRulesResource) -> None:
        self._workload_identity_federation_rules = workload_identity_federation_rules

        self.create = async_to_raw_response_wrapper(
            workload_identity_federation_rules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workload_identity_federation_rules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workload_identity_federation_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            workload_identity_federation_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workload_identity_federation_rules.delete,
        )


class WorkloadIdentityFederationRulesResourceWithStreamingResponse:
    def __init__(self, workload_identity_federation_rules: WorkloadIdentityFederationRulesResource) -> None:
        self._workload_identity_federation_rules = workload_identity_federation_rules

        self.create = to_streamed_response_wrapper(
            workload_identity_federation_rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workload_identity_federation_rules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workload_identity_federation_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            workload_identity_federation_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            workload_identity_federation_rules.delete,
        )


class AsyncWorkloadIdentityFederationRulesResourceWithStreamingResponse:
    def __init__(self, workload_identity_federation_rules: AsyncWorkloadIdentityFederationRulesResource) -> None:
        self._workload_identity_federation_rules = workload_identity_federation_rules

        self.create = async_to_streamed_response_wrapper(
            workload_identity_federation_rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workload_identity_federation_rules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workload_identity_federation_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workload_identity_federation_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workload_identity_federation_rules.delete,
        )
