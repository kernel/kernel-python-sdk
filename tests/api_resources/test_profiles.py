# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import Profile, ProfileListResponse
from kernel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        profile = client.profiles.create()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        profile = client.profiles.create(
            name="name",
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        profile = client.profiles.retrieve(
            "id_or_name",
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.profiles.with_raw_response.retrieve(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.profiles.with_streaming_response.retrieve(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        profile = client.profiles.delete(
            "id_or_name",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.profiles.with_raw_response.delete(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.profiles.with_streaming_response.delete(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.profiles.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/profiles/id_or_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        profile = client.profiles.download(
            "id_or_name",
        )
        assert profile.is_closed
        assert profile.json() == {"foo": "bar"}
        assert cast(Any, profile.is_closed) is True
        assert isinstance(profile, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/profiles/id_or_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        profile = client.profiles.with_raw_response.download(
            "id_or_name",
        )

        assert profile.is_closed is True
        assert profile.http_request.headers.get("X-Stainless-Lang") == "python"
        assert profile.json() == {"foo": "bar"}
        assert isinstance(profile, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/profiles/id_or_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.profiles.with_streaming_response.download(
            "id_or_name",
        ) as profile:
            assert not profile.is_closed
            assert profile.http_request.headers.get("X-Stainless-Lang") == "python"

            assert profile.json() == {"foo": "bar"}
            assert cast(Any, profile.is_closed) is True
            assert isinstance(profile, StreamedBinaryAPIResponse)

        assert cast(Any, profile.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.profiles.with_raw_response.download(
                "",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        profile = await async_client.profiles.create()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        profile = await async_client.profiles.create(
            name="name",
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        profile = await async_client.profiles.retrieve(
            "id_or_name",
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.profiles.with_raw_response.retrieve(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.profiles.with_streaming_response.retrieve(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        profile = await async_client.profiles.delete(
            "id_or_name",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.profiles.with_raw_response.delete(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.profiles.with_streaming_response.delete(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.profiles.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/profiles/id_or_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        profile = await async_client.profiles.download(
            "id_or_name",
        )
        assert profile.is_closed
        assert await profile.json() == {"foo": "bar"}
        assert cast(Any, profile.is_closed) is True
        assert isinstance(profile, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/profiles/id_or_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        profile = await async_client.profiles.with_raw_response.download(
            "id_or_name",
        )

        assert profile.is_closed is True
        assert profile.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await profile.json() == {"foo": "bar"}
        assert isinstance(profile, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/profiles/id_or_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.profiles.with_streaming_response.download(
            "id_or_name",
        ) as profile:
            assert not profile.is_closed
            assert profile.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await profile.json() == {"foo": "bar"}
            assert cast(Any, profile.is_closed) is True
            assert isinstance(profile, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, profile.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.profiles.with_raw_response.download(
                "",
            )
