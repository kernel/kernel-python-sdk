# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    ExtensionListResponse,
    ExtensionUploadResponse,
)
from kernel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtensions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        extension = client.extensions.list()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.extensions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.extensions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionListResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        extension = client.extensions.delete(
            "id_or_name",
        )
        assert extension is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.extensions.with_raw_response.delete(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert extension is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.extensions.with_streaming_response.delete(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert extension is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.extensions.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/id_or_name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extension = client.extensions.download(
            "id_or_name",
        )
        assert extension.is_closed
        assert extension.json() == {"foo": "bar"}
        assert cast(Any, extension.is_closed) is True
        assert isinstance(extension, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/id_or_name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        extension = client.extensions.with_raw_response.download(
            "id_or_name",
        )

        assert extension.is_closed is True
        assert extension.http_request.headers.get("X-Stainless-Lang") == "python"
        assert extension.json() == {"foo": "bar"}
        assert isinstance(extension, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/id_or_name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.extensions.with_streaming_response.download(
            "id_or_name",
        ) as extension:
            assert not extension.is_closed
            assert extension.http_request.headers.get("X-Stainless-Lang") == "python"

            assert extension.json() == {"foo": "bar"}
            assert cast(Any, extension.is_closed) is True
            assert isinstance(extension, StreamedBinaryAPIResponse)

        assert cast(Any, extension.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.extensions.with_raw_response.download(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_from_chrome_store(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extension = client.extensions.download_from_chrome_store(
            url="url",
        )
        assert extension.is_closed
        assert extension.json() == {"foo": "bar"}
        assert cast(Any, extension.is_closed) is True
        assert isinstance(extension, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_from_chrome_store_with_all_params(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extension = client.extensions.download_from_chrome_store(
            url="url",
            os="win",
        )
        assert extension.is_closed
        assert extension.json() == {"foo": "bar"}
        assert cast(Any, extension.is_closed) is True
        assert isinstance(extension, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_from_chrome_store(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        extension = client.extensions.with_raw_response.download_from_chrome_store(
            url="url",
        )

        assert extension.is_closed is True
        assert extension.http_request.headers.get("X-Stainless-Lang") == "python"
        assert extension.json() == {"foo": "bar"}
        assert isinstance(extension, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_from_chrome_store(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.extensions.with_streaming_response.download_from_chrome_store(
            url="url",
        ) as extension:
            assert not extension.is_closed
            assert extension.http_request.headers.get("X-Stainless-Lang") == "python"

            assert extension.json() == {"foo": "bar"}
            assert cast(Any, extension.is_closed) is True
            assert isinstance(extension, StreamedBinaryAPIResponse)

        assert cast(Any, extension.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Kernel) -> None:
        extension = client.extensions.upload(
            file=b"raw file contents",
        )
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Kernel) -> None:
        extension = client.extensions.upload(
            file=b"raw file contents",
            name="name",
        )
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Kernel) -> None:
        response = client.extensions.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Kernel) -> None:
        with client.extensions.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtensions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        extension = await async_client.extensions.list()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.extensions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.extensions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionListResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        extension = await async_client.extensions.delete(
            "id_or_name",
        )
        assert extension is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.extensions.with_raw_response.delete(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert extension is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.extensions.with_streaming_response.delete(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert extension is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.extensions.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/id_or_name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extension = await async_client.extensions.download(
            "id_or_name",
        )
        assert extension.is_closed
        assert await extension.json() == {"foo": "bar"}
        assert cast(Any, extension.is_closed) is True
        assert isinstance(extension, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/id_or_name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        extension = await async_client.extensions.with_raw_response.download(
            "id_or_name",
        )

        assert extension.is_closed is True
        assert extension.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await extension.json() == {"foo": "bar"}
        assert isinstance(extension, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/id_or_name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.extensions.with_streaming_response.download(
            "id_or_name",
        ) as extension:
            assert not extension.is_closed
            assert extension.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await extension.json() == {"foo": "bar"}
            assert cast(Any, extension.is_closed) is True
            assert isinstance(extension, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, extension.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.extensions.with_raw_response.download(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_from_chrome_store(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extension = await async_client.extensions.download_from_chrome_store(
            url="url",
        )
        assert extension.is_closed
        assert await extension.json() == {"foo": "bar"}
        assert cast(Any, extension.is_closed) is True
        assert isinstance(extension, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_from_chrome_store_with_all_params(
        self, async_client: AsyncKernel, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extension = await async_client.extensions.download_from_chrome_store(
            url="url",
            os="win",
        )
        assert extension.is_closed
        assert await extension.json() == {"foo": "bar"}
        assert cast(Any, extension.is_closed) is True
        assert isinstance(extension, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_from_chrome_store(
        self, async_client: AsyncKernel, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        extension = await async_client.extensions.with_raw_response.download_from_chrome_store(
            url="url",
        )

        assert extension.is_closed is True
        assert extension.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await extension.json() == {"foo": "bar"}
        assert isinstance(extension, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_from_chrome_store(
        self, async_client: AsyncKernel, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/extensions/from_chrome_store").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.extensions.with_streaming_response.download_from_chrome_store(
            url="url",
        ) as extension:
            assert not extension.is_closed
            assert extension.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await extension.json() == {"foo": "bar"}
            assert cast(Any, extension.is_closed) is True
            assert isinstance(extension, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, extension.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncKernel) -> None:
        extension = await async_client.extensions.upload(
            file=b"raw file contents",
        )
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncKernel) -> None:
        extension = await async_client.extensions.upload(
            file=b"raw file contents",
            name="name",
        )
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncKernel) -> None:
        response = await async_client.extensions.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncKernel) -> None:
        async with async_client.extensions.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True
