# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel._utils import parse_date
from kernel.types.search import Search

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        search = client.search.create(
            query="x",
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        search = client.search.create(
            query="x",
            content=True,
            country="se",
            end_date=parse_date("2019-12-27"),
            exclude_domains=["string"],
            include_domains=["string"],
            include_raw=True,
            language="language",
            max_results=1,
            recency="hour",
            safe_search="off",
            start_date=parse_date("2019-12-27"),
            strategy={
                "type": "auto",
                "fallback_on": ["error"],
                "provider_options": [
                    {
                        "provider": "brave",
                        "options": {
                            "count": 1,
                            "extra_snippets": True,
                            "goggles": "goggles",
                            "goggles_id": "goggles_id",
                            "include_fetch_metadata": True,
                            "offset": 0,
                            "operators": "operators",
                            "result_filter": "result_filter",
                            "search_lang": "search_lang",
                            "spellcheck": True,
                            "ui_lang": "ui_lang",
                            "units": "metric",
                        },
                    }
                ],
            },
            strict_params=True,
            timeout_ms=1000,
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.search.with_raw_response.create(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.search.with_streaming_response.create(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        search = client.search.retrieve(
            "srch_abc123",
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.search.with_raw_response.retrieve(
            "srch_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.search.with_streaming_response.retrieve(
            "srch_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.search.with_raw_response.retrieve(
                "",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        search = await async_client.search.create(
            query="x",
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        search = await async_client.search.create(
            query="x",
            content=True,
            country="se",
            end_date=parse_date("2019-12-27"),
            exclude_domains=["string"],
            include_domains=["string"],
            include_raw=True,
            language="language",
            max_results=1,
            recency="hour",
            safe_search="off",
            start_date=parse_date("2019-12-27"),
            strategy={
                "type": "auto",
                "fallback_on": ["error"],
                "provider_options": [
                    {
                        "provider": "brave",
                        "options": {
                            "count": 1,
                            "extra_snippets": True,
                            "goggles": "goggles",
                            "goggles_id": "goggles_id",
                            "include_fetch_metadata": True,
                            "offset": 0,
                            "operators": "operators",
                            "result_filter": "result_filter",
                            "search_lang": "search_lang",
                            "spellcheck": True,
                            "ui_lang": "ui_lang",
                            "units": "metric",
                        },
                    }
                ],
            },
            strict_params=True,
            timeout_ms=1000,
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.search.with_raw_response.create(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.search.with_streaming_response.create(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        search = await async_client.search.retrieve(
            "srch_abc123",
        )
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.search.with_raw_response.retrieve(
            "srch_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(Search, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.search.with_streaming_response.retrieve(
            "srch_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.search.with_raw_response.retrieve(
                "",
            )
