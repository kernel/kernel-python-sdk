# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import workload_identity_authentication_event_list_params
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
from ..types.workload_identity_authentication_event import WorkloadIdentityAuthenticationEvent

__all__ = ["WorkloadIdentityAuthenticationEventsResource", "AsyncWorkloadIdentityAuthenticationEventsResource"]


class WorkloadIdentityAuthenticationEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkloadIdentityAuthenticationEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WorkloadIdentityAuthenticationEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkloadIdentityAuthenticationEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return WorkloadIdentityAuthenticationEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        federation_rule_id: str | Omit = omit,
        issuer_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        outcome: Literal["success", "failure"] | Omit = omit,
        project_id: str | Omit = omit,
        service_account_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[WorkloadIdentityAuthenticationEvent]:
        """Any signed-in member of the organization can read this.

        API keys cannot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/org/workload_identity_authentication_events",
            page=SyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "federation_rule_id": federation_rule_id,
                        "issuer_id": issuer_id,
                        "limit": limit,
                        "offset": offset,
                        "outcome": outcome,
                        "project_id": project_id,
                        "service_account_id": service_account_id,
                        "start_time": start_time,
                    },
                    workload_identity_authentication_event_list_params.WorkloadIdentityAuthenticationEventListParams,
                ),
            ),
            model=WorkloadIdentityAuthenticationEvent,
        )


class AsyncWorkloadIdentityAuthenticationEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkloadIdentityAuthenticationEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkloadIdentityAuthenticationEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkloadIdentityAuthenticationEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncWorkloadIdentityAuthenticationEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        federation_rule_id: str | Omit = omit,
        issuer_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        outcome: Literal["success", "failure"] | Omit = omit,
        project_id: str | Omit = omit,
        service_account_id: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        WorkloadIdentityAuthenticationEvent, AsyncOffsetPagination[WorkloadIdentityAuthenticationEvent]
    ]:
        """Any signed-in member of the organization can read this.

        API keys cannot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/org/workload_identity_authentication_events",
            page=AsyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "federation_rule_id": federation_rule_id,
                        "issuer_id": issuer_id,
                        "limit": limit,
                        "offset": offset,
                        "outcome": outcome,
                        "project_id": project_id,
                        "service_account_id": service_account_id,
                        "start_time": start_time,
                    },
                    workload_identity_authentication_event_list_params.WorkloadIdentityAuthenticationEventListParams,
                ),
            ),
            model=WorkloadIdentityAuthenticationEvent,
        )


class WorkloadIdentityAuthenticationEventsResourceWithRawResponse:
    def __init__(self, workload_identity_authentication_events: WorkloadIdentityAuthenticationEventsResource) -> None:
        self._workload_identity_authentication_events = workload_identity_authentication_events

        self.list = to_raw_response_wrapper(
            workload_identity_authentication_events.list,
        )


class AsyncWorkloadIdentityAuthenticationEventsResourceWithRawResponse:
    def __init__(
        self, workload_identity_authentication_events: AsyncWorkloadIdentityAuthenticationEventsResource
    ) -> None:
        self._workload_identity_authentication_events = workload_identity_authentication_events

        self.list = async_to_raw_response_wrapper(
            workload_identity_authentication_events.list,
        )


class WorkloadIdentityAuthenticationEventsResourceWithStreamingResponse:
    def __init__(self, workload_identity_authentication_events: WorkloadIdentityAuthenticationEventsResource) -> None:
        self._workload_identity_authentication_events = workload_identity_authentication_events

        self.list = to_streamed_response_wrapper(
            workload_identity_authentication_events.list,
        )


class AsyncWorkloadIdentityAuthenticationEventsResourceWithStreamingResponse:
    def __init__(
        self, workload_identity_authentication_events: AsyncWorkloadIdentityAuthenticationEventsResource
    ) -> None:
        self._workload_identity_authentication_events = workload_identity_authentication_events

        self.list = async_to_streamed_response_wrapper(
            workload_identity_authentication_events.list,
        )
