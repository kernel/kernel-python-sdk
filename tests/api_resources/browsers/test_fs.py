# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from kernel.types.browsers import (
    FFileInfoResponse,
    FListFilesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_directory(self, client: Kernel) -> None:
        f = client.browsers.fs.create_directory(
            id="id",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_directory_with_all_params(self, client: Kernel) -> None:
        f = client.browsers.fs.create_directory(
            id="id",
            path="/J!",
            mode="0611",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_directory(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.create_directory(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_directory(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.create_directory(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_directory(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.create_directory(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_directory(self, client: Kernel) -> None:
        f = client.browsers.fs.delete_directory(
            id="id",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_directory(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.delete_directory(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_directory(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.delete_directory(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_directory(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.delete_directory(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_file(self, client: Kernel) -> None:
        f = client.browsers.fs.delete_file(
            id="id",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_file(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.delete_file(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_file(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.delete_file(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_file(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.delete_file(
                id="",
                path="/J!",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_dir_zip(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/download_dir_zip").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        f = client.browsers.fs.download_dir_zip(
            id="id",
            path="/J!",
        )
        assert f.is_closed
        assert f.json() == {"foo": "bar"}
        assert cast(Any, f.is_closed) is True
        assert isinstance(f, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_dir_zip(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/download_dir_zip").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        f = client.browsers.fs.with_raw_response.download_dir_zip(
            id="id",
            path="/J!",
        )

        assert f.is_closed is True
        assert f.http_request.headers.get("X-Stainless-Lang") == "python"
        assert f.json() == {"foo": "bar"}
        assert isinstance(f, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_dir_zip(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/download_dir_zip").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.browsers.fs.with_streaming_response.download_dir_zip(
            id="id",
            path="/J!",
        ) as f:
            assert not f.is_closed
            assert f.http_request.headers.get("X-Stainless-Lang") == "python"

            assert f.json() == {"foo": "bar"}
            assert cast(Any, f.is_closed) is True
            assert isinstance(f, StreamedBinaryAPIResponse)

        assert cast(Any, f.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_dir_zip(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.download_dir_zip(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_file_info(self, client: Kernel) -> None:
        f = client.browsers.fs.file_info(
            id="id",
            path="/J!",
        )
        assert_matches_type(FFileInfoResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_file_info(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.file_info(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert_matches_type(FFileInfoResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_file_info(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.file_info(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert_matches_type(FFileInfoResponse, f, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_file_info(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.file_info(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files(self, client: Kernel) -> None:
        f = client.browsers.fs.list_files(
            id="id",
            path="/J!",
        )
        assert_matches_type(FListFilesResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_files(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.list_files(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert_matches_type(FListFilesResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_files(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.list_files(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert_matches_type(FListFilesResponse, f, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_files(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.list_files(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move(self, client: Kernel) -> None:
        f = client.browsers.fs.move(
            id="id",
            dest_path="/J!",
            src_path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_move(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.move(
            id="id",
            dest_path="/J!",
            src_path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_move(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.move(
            id="id",
            dest_path="/J!",
            src_path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_move(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.move(
                id="",
                dest_path="/J!",
                src_path="/J!",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_read_file(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/read_file").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        f = client.browsers.fs.read_file(
            id="id",
            path="/J!",
        )
        assert f.is_closed
        assert f.json() == {"foo": "bar"}
        assert cast(Any, f.is_closed) is True
        assert isinstance(f, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_read_file(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/read_file").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        f = client.browsers.fs.with_raw_response.read_file(
            id="id",
            path="/J!",
        )

        assert f.is_closed is True
        assert f.http_request.headers.get("X-Stainless-Lang") == "python"
        assert f.json() == {"foo": "bar"}
        assert isinstance(f, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_read_file(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/read_file").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.browsers.fs.with_streaming_response.read_file(
            id="id",
            path="/J!",
        ) as f:
            assert not f.is_closed
            assert f.http_request.headers.get("X-Stainless-Lang") == "python"

            assert f.json() == {"foo": "bar"}
            assert cast(Any, f.is_closed) is True
            assert isinstance(f, StreamedBinaryAPIResponse)

        assert cast(Any, f.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_read_file(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.read_file(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_file_permissions(self, client: Kernel) -> None:
        f = client.browsers.fs.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_file_permissions_with_all_params(self, client: Kernel) -> None:
        f = client.browsers.fs.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
            group="group",
            owner="owner",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_file_permissions(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_file_permissions(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_file_permissions(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.set_file_permissions(
                id="",
                mode="0611",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Kernel) -> None:
        f = client.browsers.fs.upload(
            id="id",
            files=[
                {
                    "dest_path": "/J!",
                    "file": b"Example data",
                }
            ],
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.upload(
            id="id",
            files=[
                {
                    "dest_path": "/J!",
                    "file": b"Example data",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.upload(
            id="id",
            files=[
                {
                    "dest_path": "/J!",
                    "file": b"Example data",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.upload(
                id="",
                files=[
                    {
                        "dest_path": "/J!",
                        "file": b"Example data",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_zip(self, client: Kernel) -> None:
        f = client.browsers.fs.upload_zip(
            id="id",
            dest_path="/J!",
            zip_file=b"Example data",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_zip(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.upload_zip(
            id="id",
            dest_path="/J!",
            zip_file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_zip(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.upload_zip(
            id="id",
            dest_path="/J!",
            zip_file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload_zip(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.upload_zip(
                id="",
                dest_path="/J!",
                zip_file=b"Example data",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_write_file(self, client: Kernel) -> None:
        f = client.browsers.fs.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_write_file_with_all_params(self, client: Kernel) -> None:
        f = client.browsers.fs.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
            mode="0611",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_write_file(self, client: Kernel) -> None:
        response = client.browsers.fs.with_raw_response.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_write_file(self, client: Kernel) -> None:
        with client.browsers.fs.with_streaming_response.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_write_file(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.fs.with_raw_response.write_file(
                id="",
                contents=b"Example data",
                path="/J!",
            )


class TestAsyncFs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_directory(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.create_directory(
            id="id",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_directory_with_all_params(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.create_directory(
            id="id",
            path="/J!",
            mode="0611",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_directory(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.create_directory(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_directory(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.create_directory(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_directory(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.create_directory(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_directory(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.delete_directory(
            id="id",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_directory(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.delete_directory(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_directory(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.delete_directory(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_directory(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.delete_directory(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_file(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.delete_file(
            id="id",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_file(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.delete_file(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_file(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.delete_file(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_file(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.delete_file(
                id="",
                path="/J!",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_dir_zip(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/download_dir_zip").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        f = await async_client.browsers.fs.download_dir_zip(
            id="id",
            path="/J!",
        )
        assert f.is_closed
        assert await f.json() == {"foo": "bar"}
        assert cast(Any, f.is_closed) is True
        assert isinstance(f, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_dir_zip(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/download_dir_zip").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        f = await async_client.browsers.fs.with_raw_response.download_dir_zip(
            id="id",
            path="/J!",
        )

        assert f.is_closed is True
        assert f.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await f.json() == {"foo": "bar"}
        assert isinstance(f, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_dir_zip(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/download_dir_zip").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.browsers.fs.with_streaming_response.download_dir_zip(
            id="id",
            path="/J!",
        ) as f:
            assert not f.is_closed
            assert f.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await f.json() == {"foo": "bar"}
            assert cast(Any, f.is_closed) is True
            assert isinstance(f, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, f.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_dir_zip(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.download_dir_zip(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_file_info(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.file_info(
            id="id",
            path="/J!",
        )
        assert_matches_type(FFileInfoResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_file_info(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.file_info(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert_matches_type(FFileInfoResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_file_info(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.file_info(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert_matches_type(FFileInfoResponse, f, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_file_info(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.file_info(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.list_files(
            id="id",
            path="/J!",
        )
        assert_matches_type(FListFilesResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.list_files(
            id="id",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert_matches_type(FListFilesResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.list_files(
            id="id",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert_matches_type(FListFilesResponse, f, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_files(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.list_files(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.move(
            id="id",
            dest_path="/J!",
            src_path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.move(
            id="id",
            dest_path="/J!",
            src_path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.move(
            id="id",
            dest_path="/J!",
            src_path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_move(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.move(
                id="",
                dest_path="/J!",
                src_path="/J!",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_read_file(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/read_file").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        f = await async_client.browsers.fs.read_file(
            id="id",
            path="/J!",
        )
        assert f.is_closed
        assert await f.json() == {"foo": "bar"}
        assert cast(Any, f.is_closed) is True
        assert isinstance(f, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_read_file(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/read_file").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        f = await async_client.browsers.fs.with_raw_response.read_file(
            id="id",
            path="/J!",
        )

        assert f.is_closed is True
        assert f.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await f.json() == {"foo": "bar"}
        assert isinstance(f, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_read_file(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.get("/browsers/id/fs/read_file").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.browsers.fs.with_streaming_response.read_file(
            id="id",
            path="/J!",
        ) as f:
            assert not f.is_closed
            assert f.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await f.json() == {"foo": "bar"}
            assert cast(Any, f.is_closed) is True
            assert isinstance(f, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, f.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_read_file(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.read_file(
                id="",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_file_permissions(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_file_permissions_with_all_params(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
            group="group",
            owner="owner",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_file_permissions(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_file_permissions(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.set_file_permissions(
            id="id",
            mode="0611",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_file_permissions(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.set_file_permissions(
                id="",
                mode="0611",
                path="/J!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.upload(
            id="id",
            files=[
                {
                    "dest_path": "/J!",
                    "file": b"Example data",
                }
            ],
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.upload(
            id="id",
            files=[
                {
                    "dest_path": "/J!",
                    "file": b"Example data",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.upload(
            id="id",
            files=[
                {
                    "dest_path": "/J!",
                    "file": b"Example data",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.upload(
                id="",
                files=[
                    {
                        "dest_path": "/J!",
                        "file": b"Example data",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.upload_zip(
            id="id",
            dest_path="/J!",
            zip_file=b"Example data",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.upload_zip(
            id="id",
            dest_path="/J!",
            zip_file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.upload_zip(
            id="id",
            dest_path="/J!",
            zip_file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload_zip(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.upload_zip(
                id="",
                dest_path="/J!",
                zip_file=b"Example data",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_write_file(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_write_file_with_all_params(self, async_client: AsyncKernel) -> None:
        f = await async_client.browsers.fs.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
            mode="0611",
        )
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_write_file(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.fs.with_raw_response.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert f is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_write_file(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.fs.with_streaming_response.write_file(
            id="id",
            contents=b"Example data",
            path="/J!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert f is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_write_file(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.fs.with_raw_response.write_file(
                id="",
                contents=b"Example data",
                path="/J!",
            )
