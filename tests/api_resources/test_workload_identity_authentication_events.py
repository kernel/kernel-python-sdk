# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import WorkloadIdentityAuthenticationEvent
from kernel._utils import parse_datetime
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkloadIdentityAuthenticationEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        workload_identity_authentication_event = client.workload_identity_authentication_events.list()
        assert_matches_type(
            SyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            workload_identity_authentication_event,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        workload_identity_authentication_event = client.workload_identity_authentication_events.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            federation_rule_id="federation_rule_id",
            issuer_id="issuer_id",
            limit=1,
            offset=0,
            outcome="success",
            project_id="project_id",
            service_account_id="service_account_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            SyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            workload_identity_authentication_event,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.workload_identity_authentication_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_authentication_event = response.parse()
        assert_matches_type(
            SyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            workload_identity_authentication_event,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.workload_identity_authentication_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_authentication_event = response.parse()
            assert_matches_type(
                SyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
                workload_identity_authentication_event,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkloadIdentityAuthenticationEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        workload_identity_authentication_event = await async_client.workload_identity_authentication_events.list()
        assert_matches_type(
            AsyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            workload_identity_authentication_event,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_authentication_event = await async_client.workload_identity_authentication_events.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            federation_rule_id="federation_rule_id",
            issuer_id="issuer_id",
            limit=1,
            offset=0,
            outcome="success",
            project_id="project_id",
            service_account_id="service_account_id",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            AsyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            workload_identity_authentication_event,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_authentication_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_authentication_event = await response.parse()
        assert_matches_type(
            AsyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
            workload_identity_authentication_event,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_authentication_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_authentication_event = await response.parse()
            assert_matches_type(
                AsyncOffsetPagination[WorkloadIdentityAuthenticationEvent],
                workload_identity_authentication_event,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
