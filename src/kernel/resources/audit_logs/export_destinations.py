# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.audit_logs import (
    export_destination_list_params,
    export_destination_create_params,
    export_destination_update_params,
)
from ...types.audit_logs.audit_log_export_destination import AuditLogExportDestination
from ...types.audit_logs.audit_log_export_destination_test_result import AuditLogExportDestinationTestResult

__all__ = ["ExportDestinationsResource", "AsyncExportDestinationsResource"]


class ExportDestinationsResource(SyncAPIResource):
    """Read audit log records for the authenticated organization."""

    @cached_property
    def with_raw_response(self) -> ExportDestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExportDestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportDestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ExportDestinationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bucket: str,
        format: Literal["jsonl.gz"],
        prefix: str,
        region: str,
        role_arn: str,
        type: Literal["s3"],
        kms_key_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AuditLogExportDestination:
        """Create a paused destination.

        Activate it with a status update once the
        destination test passes. Requires an active Enterprise plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/audit-logs/export/destinations",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "format": format,
                    "prefix": prefix,
                    "region": region,
                    "role_arn": role_arn,
                    "type": type,
                    "kms_key_id": kms_key_id,
                },
                export_destination_create_params.ExportDestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuditLogExportDestination,
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
    ) -> AuditLogExportDestination:
        """
        Retrieve details for a single audit log export destination by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/audit-logs/export/destinations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditLogExportDestination,
        )

    def update(
        self,
        id: str,
        *,
        bucket: str | Omit = omit,
        kms_key_id: str | Omit = omit,
        prefix: str | Omit = omit,
        region: str | Omit = omit,
        role_arn: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AuditLogExportDestination:
        """Apply a partial update to a destination.

        Requires an active Enterprise plan.
        Returns 409 when the destination was changed concurrently, because the merged
        configuration this request validated is no longer the one that would be stored;
        retry against fresh state. Pausing prevents new delivery attempts, but an S3
        upload already in progress may complete after the response.

        Args:
          kms_key_id: KMS key ID, alias, or ARN. Set to an empty string to remove the configured KMS
              key; omit or send null to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/audit-logs/export/destinations/{id}", id=id),
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "kms_key_id": kms_key_id,
                    "prefix": prefix,
                    "region": region,
                    "role_arn": role_arn,
                    "status": status,
                },
                export_destination_update_params.ExportDestinationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuditLogExportDestination,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[AuditLogExportDestination]:
        """
        List audit log export destinations for the organization with pagination support.

        Args:
          limit: Limit the number of destinations to return.

          offset: Offset the number of destinations to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audit-logs/export/destinations",
            page=SyncOffsetPagination[AuditLogExportDestination],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    export_destination_list_params.ExportDestinationListParams,
                ),
            ),
            model=AuditLogExportDestination,
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
        """Soft delete the destination and prevent new delivery attempts.

        An S3 upload
        already in progress may complete after the response.

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
            path_template("/audit-logs/export/destinations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def test(
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
    ) -> AuditLogExportDestinationTestResult:
        """
        Verify the destination is writable by assuming the configured role and uploading
        a temporary probe object with the same request metadata as a real delivery.
        Requires an active Enterprise plan.

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
            path_template("/audit-logs/export/destinations/{id}/test", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuditLogExportDestinationTestResult,
        )


class AsyncExportDestinationsResource(AsyncAPIResource):
    """Read audit log records for the authenticated organization."""

    @cached_property
    def with_raw_response(self) -> AsyncExportDestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExportDestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportDestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncExportDestinationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bucket: str,
        format: Literal["jsonl.gz"],
        prefix: str,
        region: str,
        role_arn: str,
        type: Literal["s3"],
        kms_key_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AuditLogExportDestination:
        """Create a paused destination.

        Activate it with a status update once the
        destination test passes. Requires an active Enterprise plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/audit-logs/export/destinations",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "format": format,
                    "prefix": prefix,
                    "region": region,
                    "role_arn": role_arn,
                    "type": type,
                    "kms_key_id": kms_key_id,
                },
                export_destination_create_params.ExportDestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuditLogExportDestination,
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
    ) -> AuditLogExportDestination:
        """
        Retrieve details for a single audit log export destination by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/audit-logs/export/destinations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditLogExportDestination,
        )

    async def update(
        self,
        id: str,
        *,
        bucket: str | Omit = omit,
        kms_key_id: str | Omit = omit,
        prefix: str | Omit = omit,
        region: str | Omit = omit,
        role_arn: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AuditLogExportDestination:
        """Apply a partial update to a destination.

        Requires an active Enterprise plan.
        Returns 409 when the destination was changed concurrently, because the merged
        configuration this request validated is no longer the one that would be stored;
        retry against fresh state. Pausing prevents new delivery attempts, but an S3
        upload already in progress may complete after the response.

        Args:
          kms_key_id: KMS key ID, alias, or ARN. Set to an empty string to remove the configured KMS
              key; omit or send null to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/audit-logs/export/destinations/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "kms_key_id": kms_key_id,
                    "prefix": prefix,
                    "region": region,
                    "role_arn": role_arn,
                    "status": status,
                },
                export_destination_update_params.ExportDestinationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuditLogExportDestination,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogExportDestination, AsyncOffsetPagination[AuditLogExportDestination]]:
        """
        List audit log export destinations for the organization with pagination support.

        Args:
          limit: Limit the number of destinations to return.

          offset: Offset the number of destinations to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audit-logs/export/destinations",
            page=AsyncOffsetPagination[AuditLogExportDestination],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    export_destination_list_params.ExportDestinationListParams,
                ),
            ),
            model=AuditLogExportDestination,
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
        """Soft delete the destination and prevent new delivery attempts.

        An S3 upload
        already in progress may complete after the response.

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
            path_template("/audit-logs/export/destinations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def test(
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
    ) -> AuditLogExportDestinationTestResult:
        """
        Verify the destination is writable by assuming the configured role and uploading
        a temporary probe object with the same request metadata as a real delivery.
        Requires an active Enterprise plan.

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
            path_template("/audit-logs/export/destinations/{id}/test", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuditLogExportDestinationTestResult,
        )


class ExportDestinationsResourceWithRawResponse:
    def __init__(self, export_destinations: ExportDestinationsResource) -> None:
        self._export_destinations = export_destinations

        self.create = to_raw_response_wrapper(
            export_destinations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            export_destinations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            export_destinations.update,
        )
        self.list = to_raw_response_wrapper(
            export_destinations.list,
        )
        self.delete = to_raw_response_wrapper(
            export_destinations.delete,
        )
        self.test = to_raw_response_wrapper(
            export_destinations.test,
        )


class AsyncExportDestinationsResourceWithRawResponse:
    def __init__(self, export_destinations: AsyncExportDestinationsResource) -> None:
        self._export_destinations = export_destinations

        self.create = async_to_raw_response_wrapper(
            export_destinations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            export_destinations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            export_destinations.update,
        )
        self.list = async_to_raw_response_wrapper(
            export_destinations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            export_destinations.delete,
        )
        self.test = async_to_raw_response_wrapper(
            export_destinations.test,
        )


class ExportDestinationsResourceWithStreamingResponse:
    def __init__(self, export_destinations: ExportDestinationsResource) -> None:
        self._export_destinations = export_destinations

        self.create = to_streamed_response_wrapper(
            export_destinations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            export_destinations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            export_destinations.update,
        )
        self.list = to_streamed_response_wrapper(
            export_destinations.list,
        )
        self.delete = to_streamed_response_wrapper(
            export_destinations.delete,
        )
        self.test = to_streamed_response_wrapper(
            export_destinations.test,
        )


class AsyncExportDestinationsResourceWithStreamingResponse:
    def __init__(self, export_destinations: AsyncExportDestinationsResource) -> None:
        self._export_destinations = export_destinations

        self.create = async_to_streamed_response_wrapper(
            export_destinations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            export_destinations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            export_destinations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            export_destinations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            export_destinations.delete,
        )
        self.test = async_to_streamed_response_wrapper(
            export_destinations.test,
        )
