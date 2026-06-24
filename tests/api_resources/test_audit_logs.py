# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import AuditLogEntry
from kernel._utils import parse_datetime
from kernel.pagination import SyncPageTokenPagination, AsyncPageTokenPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        audit_log = client.audit_logs.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )
        assert_matches_type(SyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        audit_log = client.audit_logs.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
            auth_strategy="auth_strategy",
            exclude_method="exclude_method",
            limit=1,
            method="method",
            page_token="page_token",
            search="search",
            search_user_id=["string"],
            service="service",
        )
        assert_matches_type(SyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.audit_logs.with_raw_response.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.audit_logs.with_streaming_response.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        audit_log = await async_client.audit_logs.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )
        assert_matches_type(AsyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        audit_log = await async_client.audit_logs.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
            auth_strategy="auth_strategy",
            exclude_method="exclude_method",
            limit=1,
            method="method",
            page_token="page_token",
            search="search",
            search_user_id=["string"],
            service="service",
        )
        assert_matches_type(AsyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.with_raw_response.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.with_streaming_response.list(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncPageTokenPagination[AuditLogEntry], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True
