# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import AuditLogEntry
from kernel._utils import parse_datetime
from kernel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
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
            exclude_method=["string"],
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_chunk(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audit_log = client.audit_logs.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )
        assert audit_log.is_closed
        assert audit_log.json() == {"foo": "bar"}
        assert cast(Any, audit_log.is_closed) is True
        assert isinstance(audit_log, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_chunk_with_all_params(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audit_log = client.audit_logs.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
            auth_strategy="auth_strategy",
            cursor="cursor",
            exclude_method=["string"],
            format="jsonl",
            limit=1,
            method="method",
            search="search",
            search_user_id=["string"],
            service="service",
        )
        assert audit_log.is_closed
        assert audit_log.json() == {"foo": "bar"}
        assert cast(Any, audit_log.is_closed) is True
        assert isinstance(audit_log, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_chunk(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        audit_log = client.audit_logs.with_raw_response.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )

        assert audit_log.is_closed is True
        assert audit_log.http_request.headers.get("X-Stainless-Lang") == "python"
        assert audit_log.json() == {"foo": "bar"}
        assert isinstance(audit_log, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_chunk(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.audit_logs.with_streaming_response.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        ) as audit_log:
            assert not audit_log.is_closed
            assert audit_log.http_request.headers.get("X-Stainless-Lang") == "python"

            assert audit_log.json() == {"foo": "bar"}
            assert cast(Any, audit_log.is_closed) is True
            assert isinstance(audit_log, StreamedBinaryAPIResponse)

        assert cast(Any, audit_log.is_closed) is True


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
            exclude_method=["string"],
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_chunk(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audit_log = await async_client.audit_logs.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )
        assert audit_log.is_closed
        assert await audit_log.json() == {"foo": "bar"}
        assert cast(Any, audit_log.is_closed) is True
        assert isinstance(audit_log, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_chunk_with_all_params(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audit_log = await async_client.audit_logs.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
            auth_strategy="auth_strategy",
            cursor="cursor",
            exclude_method=["string"],
            format="jsonl",
            limit=1,
            method="method",
            search="search",
            search_user_id=["string"],
            service="service",
        )
        assert audit_log.is_closed
        assert await audit_log.json() == {"foo": "bar"}
        assert cast(Any, audit_log.is_closed) is True
        assert isinstance(audit_log, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_chunk(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        audit_log = await async_client.audit_logs.with_raw_response.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        )

        assert audit_log.is_closed is True
        assert audit_log.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await audit_log.json() == {"foo": "bar"}
        assert isinstance(audit_log, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_chunk(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/audit-logs/export/chunk").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.audit_logs.with_streaming_response.export_chunk(
            end=parse_datetime("2026-01-02T00:00:00Z"),
            start=parse_datetime("2026-01-01T00:00:00Z"),
        ) as audit_log:
            assert not audit_log.is_closed
            assert audit_log.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await audit_log.json() == {"foo": "bar"}
            assert cast(Any, audit_log.is_closed) is True
            assert isinstance(audit_log, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, audit_log.is_closed) is True
