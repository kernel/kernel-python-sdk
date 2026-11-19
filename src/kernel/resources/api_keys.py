# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    api_key_list_params,
    api_key_create_params,
    api_key_rotate_params,
    api_key_update_params,
    api_key_retrieve_params,
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
from ..types.api_key import APIKey
from ..types.created_api_key import CreatedAPIKey

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    """Create and manage API keys for organization and project-scoped access."""

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        days_to_expire: Optional[int] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        policy: api_key_create_params.Policy | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        service_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CreatedAPIKey:
        """
        Create a personal API key, or link a key to an organization-owned service
        account. Service-account keys require an organization administrator, explicit
        project and nonempty policy. An optional `policy` scopes the key to its listed
        actions and resources, and each statement may carry a `condition`. A `source_ip`
        condition restricts the statement to requests whose client address falls inside
        its CIDR networks, so a key limited to your egress IP ranges only works from
        your network, even if its secret leaks.

        Args:
          name: Label for the API key (1-255 characters). API keys are not addressable by name.

          days_to_expire: Number of days until expiry, up to 3650. Use null for never. Cannot be combined
              with expires_at.

          expires_at: Exact expiry time. Must be in the future and no later than the issuing
              credential's own expiry. Cannot be combined with days_to_expire.

          policy: Issue a scoped key that may only perform the listed actions on the listed
              resources. A statement may carry a condition; a `source_ip` condition restricts
              the statement to requests from inside its CIDR networks.

          project_id: Unique project identifier

          service_account_id: Link to an active same-organization service account. Requires an organization
              administrator, explicit project and nonempty policy. Omit for a personal key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/org/api_keys",
            body=maybe_transform(
                {
                    "name": name,
                    "days_to_expire": days_to_expire,
                    "expires_at": expires_at,
                    "policy": policy,
                    "project_id": project_id,
                    "service_account_id": service_account_id,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CreatedAPIKey,
        )

    def retrieve(
        self,
        id: str,
        *,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Retrieve an API key by ID for the authenticated organization.

        API keys are
        masked.

        Args:
          include_deleted: When true, return the API key even if it has been deleted (soft-deleted), for
              audit purposes. Defaults to false, which returns 404 for a deleted key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/org/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_deleted": include_deleted}, api_key_retrieve_params.APIKeyRetrieveParams
                ),
            ),
            cast_to=APIKey,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        policy: api_key_update_params.Policy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> APIKey:
        """
        Update an API key's name, or replace its permissions by attaching a new policy
        in place: the key's credential never changes, so consumers keep the same secret.
        The replacement policy may carry `source_ip` conditions, so you can add, change,
        or remove IP allowlisting on an existing key without rotating its credential. A
        present `policy` fully replaces the key's policy and takes effect for new
        requests within the authorization cache; requests from outside a condition's
        networks get `403` and are recorded in the audit log with the client address.
        Requires api_keys:write to rename; api_keys:set_policy to replace permissions.

        Args:
          name: New API key name

          policy: Permissions that fully replace the key's policy. Attaching a policy to a key
              without one makes the key scoped: every action and resource the policy does not
              list is denied. The key's credential, name, project, and expiry are unchanged,
              so consumers never need the key redistributed. A `source_ip` condition adds or
              changes IP allowlisting without rotating the credential. Requires
              api_keys:set_policy on the key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/org/api_keys/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        created_by: str | Omit = omit,
        include_deleted: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        principal_type: Literal["user", "service_account"] | Omit = omit,
        project_id: str | Omit = omit,
        query: str | Omit = omit,
        service_account_id: str | Omit = omit,
        sort_by: Literal["created_at", "name", "expires_at", "last_used_at"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        status: Literal["active", "expired", "deleted", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[APIKey]:
        """List API keys for the authenticated organization.

        API keys are masked.

        Args:
          created_by: Return only keys created by this user ID. This is the same person the key's
              created_by field describes.

          include_deleted: Deprecated: use status=all instead. When true, include deleted (soft-deleted)
              API keys in the results for audit purposes.

          limit: Maximum number of results to return

          name: Exact-match filter on API key name using the database collation. In production,
              matching is case- and accent-insensitive. Names are not required to be unique,
              so multiple keys may match. When status=all or include_deleted=true is set,
              soft-deleted keys with the same name may also match.

          offset: Number of results to skip

          principal_type: Return only keys that act as a user, or only keys that act as a service account.

          project_id: Return only keys scoped to this project ID. The value "org" returns keys that
              are not scoped to a project.

          query: Case-insensitive substring match against API key name, creator, and project. API
              key identifiers and masked keys match by exact value or prefix.

          service_account_id: Return only keys that belong to this service account.

          sort_by: Field to sort API keys by. Keys with no expiry or no recorded use sort last for
              expires_at and last_used_at in either direction.

          sort_direction: Sort direction for API keys.

          status: Filter API keys by status. "active" returns keys that are neither deleted nor
              expired (default), "expired" returns keys that are not deleted and whose expiry
              has passed, "deleted" returns only soft-deleted keys, "all" returns every key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/org/api_keys",
            page=SyncOffsetPagination[APIKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_by": created_by,
                        "include_deleted": include_deleted,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "principal_type": principal_type,
                        "project_id": project_id,
                        "query": query,
                        "service_account_id": service_account_id,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "status": status,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            model=APIKey,
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
        Delete an API key and asynchronously end browser sessions attributed to it,
        discarding unsaved profile changes. A key cannot delete itself; use a different
        key to delete this one. If cleanup cannot be registered, the key is not deleted.

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
            path_template("/org/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def rotate(
        self,
        id: str,
        *,
        days_to_expire: Optional[int] | Omit = omit,
        expire_in_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CreatedAPIKey:
        """Rotate an API key.

        Issues a new key that copies the name and project of the
        rotated key, and schedules the rotated key to expire after a grace period so
        in-flight callers can swap over. The new plaintext key is returned once. With
        expire_in_days set to 0, browser sessions attributed to the old key are ended
        asynchronously and unsaved profile changes are discarded. Grace-period and
        natural expiry do not end existing browsers. If cleanup cannot be registered, an
        immediate rotation is not committed. Service-account keys retain their service
        principal and policy; the rotating administrator is recorded separately for
        audit.

        Args:
          days_to_expire: Lifetime in days for the new key, up to 3650. Omit to reuse the rotated key's
              original lifetime, or never-expires if it had none.

          expire_in_days: Grace period in days before the rotated key expires. Use 0 to expire it
              immediately. Omit for the default grace period of 7 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/org/api_keys/{id}/rotate", id=id),
            body=maybe_transform(
                {
                    "days_to_expire": days_to_expire,
                    "expire_in_days": expire_in_days,
                },
                api_key_rotate_params.APIKeyRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CreatedAPIKey,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    """Create and manage API keys for organization and project-scoped access."""

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        days_to_expire: Optional[int] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        policy: api_key_create_params.Policy | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        service_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CreatedAPIKey:
        """
        Create a personal API key, or link a key to an organization-owned service
        account. Service-account keys require an organization administrator, explicit
        project and nonempty policy. An optional `policy` scopes the key to its listed
        actions and resources, and each statement may carry a `condition`. A `source_ip`
        condition restricts the statement to requests whose client address falls inside
        its CIDR networks, so a key limited to your egress IP ranges only works from
        your network, even if its secret leaks.

        Args:
          name: Label for the API key (1-255 characters). API keys are not addressable by name.

          days_to_expire: Number of days until expiry, up to 3650. Use null for never. Cannot be combined
              with expires_at.

          expires_at: Exact expiry time. Must be in the future and no later than the issuing
              credential's own expiry. Cannot be combined with days_to_expire.

          policy: Issue a scoped key that may only perform the listed actions on the listed
              resources. A statement may carry a condition; a `source_ip` condition restricts
              the statement to requests from inside its CIDR networks.

          project_id: Unique project identifier

          service_account_id: Link to an active same-organization service account. Requires an organization
              administrator, explicit project and nonempty policy. Omit for a personal key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/org/api_keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "days_to_expire": days_to_expire,
                    "expires_at": expires_at,
                    "policy": policy,
                    "project_id": project_id,
                    "service_account_id": service_account_id,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CreatedAPIKey,
        )

    async def retrieve(
        self,
        id: str,
        *,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Retrieve an API key by ID for the authenticated organization.

        API keys are
        masked.

        Args:
          include_deleted: When true, return the API key even if it has been deleted (soft-deleted), for
              audit purposes. Defaults to false, which returns 404 for a deleted key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/org/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_deleted": include_deleted}, api_key_retrieve_params.APIKeyRetrieveParams
                ),
            ),
            cast_to=APIKey,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        policy: api_key_update_params.Policy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> APIKey:
        """
        Update an API key's name, or replace its permissions by attaching a new policy
        in place: the key's credential never changes, so consumers keep the same secret.
        The replacement policy may carry `source_ip` conditions, so you can add, change,
        or remove IP allowlisting on an existing key without rotating its credential. A
        present `policy` fully replaces the key's policy and takes effect for new
        requests within the authorization cache; requests from outside a condition's
        networks get `403` and are recorded in the audit log with the client address.
        Requires api_keys:write to rename; api_keys:set_policy to replace permissions.

        Args:
          name: New API key name

          policy: Permissions that fully replace the key's policy. Attaching a policy to a key
              without one makes the key scoped: every action and resource the policy does not
              list is denied. The key's credential, name, project, and expiry are unchanged,
              so consumers never need the key redistributed. A `source_ip` condition adds or
              changes IP allowlisting without rotating the credential. Requires
              api_keys:set_policy on the key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/org/api_keys/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        created_by: str | Omit = omit,
        include_deleted: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        principal_type: Literal["user", "service_account"] | Omit = omit,
        project_id: str | Omit = omit,
        query: str | Omit = omit,
        service_account_id: str | Omit = omit,
        sort_by: Literal["created_at", "name", "expires_at", "last_used_at"] | Omit = omit,
        sort_direction: Literal["asc", "desc"] | Omit = omit,
        status: Literal["active", "expired", "deleted", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[APIKey, AsyncOffsetPagination[APIKey]]:
        """List API keys for the authenticated organization.

        API keys are masked.

        Args:
          created_by: Return only keys created by this user ID. This is the same person the key's
              created_by field describes.

          include_deleted: Deprecated: use status=all instead. When true, include deleted (soft-deleted)
              API keys in the results for audit purposes.

          limit: Maximum number of results to return

          name: Exact-match filter on API key name using the database collation. In production,
              matching is case- and accent-insensitive. Names are not required to be unique,
              so multiple keys may match. When status=all or include_deleted=true is set,
              soft-deleted keys with the same name may also match.

          offset: Number of results to skip

          principal_type: Return only keys that act as a user, or only keys that act as a service account.

          project_id: Return only keys scoped to this project ID. The value "org" returns keys that
              are not scoped to a project.

          query: Case-insensitive substring match against API key name, creator, and project. API
              key identifiers and masked keys match by exact value or prefix.

          service_account_id: Return only keys that belong to this service account.

          sort_by: Field to sort API keys by. Keys with no expiry or no recorded use sort last for
              expires_at and last_used_at in either direction.

          sort_direction: Sort direction for API keys.

          status: Filter API keys by status. "active" returns keys that are neither deleted nor
              expired (default), "expired" returns keys that are not deleted and whose expiry
              has passed, "deleted" returns only soft-deleted keys, "all" returns every key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/org/api_keys",
            page=AsyncOffsetPagination[APIKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_by": created_by,
                        "include_deleted": include_deleted,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "principal_type": principal_type,
                        "project_id": project_id,
                        "query": query,
                        "service_account_id": service_account_id,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "status": status,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            model=APIKey,
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
        Delete an API key and asynchronously end browser sessions attributed to it,
        discarding unsaved profile changes. A key cannot delete itself; use a different
        key to delete this one. If cleanup cannot be registered, the key is not deleted.

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
            path_template("/org/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def rotate(
        self,
        id: str,
        *,
        days_to_expire: Optional[int] | Omit = omit,
        expire_in_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CreatedAPIKey:
        """Rotate an API key.

        Issues a new key that copies the name and project of the
        rotated key, and schedules the rotated key to expire after a grace period so
        in-flight callers can swap over. The new plaintext key is returned once. With
        expire_in_days set to 0, browser sessions attributed to the old key are ended
        asynchronously and unsaved profile changes are discarded. Grace-period and
        natural expiry do not end existing browsers. If cleanup cannot be registered, an
        immediate rotation is not committed. Service-account keys retain their service
        principal and policy; the rotating administrator is recorded separately for
        audit.

        Args:
          days_to_expire: Lifetime in days for the new key, up to 3650. Omit to reuse the rotated key's
              original lifetime, or never-expires if it had none.

          expire_in_days: Grace period in days before the rotated key expires. Use 0 to expire it
              immediately. Omit for the default grace period of 7 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/org/api_keys/{id}/rotate", id=id),
            body=await async_maybe_transform(
                {
                    "days_to_expire": days_to_expire,
                    "expire_in_days": expire_in_days,
                },
                api_key_rotate_params.APIKeyRotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CreatedAPIKey,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )
        self.rotate = to_raw_response_wrapper(
            api_keys.rotate,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )
        self.rotate = async_to_raw_response_wrapper(
            api_keys.rotate,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.rotate = to_streamed_response_wrapper(
            api_keys.rotate,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.rotate = async_to_streamed_response_wrapper(
            api_keys.rotate,
        )
