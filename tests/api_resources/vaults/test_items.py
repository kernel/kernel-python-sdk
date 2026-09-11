# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.vaults import (
    VaultItem,
    ItemListResponse,
    ItemEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        item = client.vaults.items.retrieve(
            key="x",
            id_or_name="id_or_name",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Kernel) -> None:
        item = client.vaults.items.retrieve(
            key="x",
            id_or_name="id_or_name",
            expand=["payment_methods"],
            wait=0,
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.retrieve(
            key="x",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.retrieve(
            key="x",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.retrieve(
                key="x",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.retrieve(
                key="",
                id_or_name="id_or_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        item = client.vaults.items.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
            },
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        item = client.vaults.items.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
                "expires_at": 0,
                "line_items": [
                    {
                        "name": "name",
                        "description": "description",
                        "image_url": "image_url",
                        "product_url": "product_url",
                        "quantity": 1,
                        "sku": "sku",
                        "totals": [
                            {
                                "amount": 0,
                                "display_text": "display_text",
                                "type": "type",
                            }
                        ],
                        "unit_amount": 0,
                        "url": "url",
                    }
                ],
                "metadata": {"foo": "string"},
                "totals": [
                    {
                        "amount": 0,
                        "display_text": "display_text",
                        "type": "type",
                    }
                ],
            },
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.update(
                key="x",
                id_or_name="",
                spec={
                    "amount": 3000,
                    "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                    "currency": "usd",
                    "merchant_name": "Example Store",
                    "merchant_url": "https://store.example.com",
                    "payment_method_id": "pm_example",
                    "provider": "link",
                    "wallet": "link-wallet",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.update(
                key="",
                id_or_name="id_or_name",
                spec={
                    "amount": 3000,
                    "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                    "currency": "usd",
                    "merchant_name": "Example Store",
                    "merchant_url": "https://store.example.com",
                    "payment_method_id": "pm_example",
                    "provider": "link",
                    "wallet": "link-wallet",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        item = client.vaults.items.list(
            "id_or_name",
        )
        assert_matches_type(ItemListResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.list(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemListResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.list(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemListResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        item = client.vaults.items.delete(
            key="x",
            id_or_name="id_or_name",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.delete(
            key="x",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.delete(
            key="x",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.delete(
                key="x",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.delete(
                key="",
                id_or_name="id_or_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events(self, client: Kernel) -> None:
        item = client.vaults.items.events(
            key="key",
            id_or_name="id_or_name",
        )
        assert_matches_type(ItemEventsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events_with_all_params(self, client: Kernel) -> None:
        item = client.vaults.items.events(
            key="key",
            id_or_name="id_or_name",
            after="after",
            wait=0,
        )
        assert_matches_type(ItemEventsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_events(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.events(
            key="key",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemEventsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_events(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.events(
            key="key",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemEventsResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_events(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.events(
                key="key",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.events(
                key="",
                id_or_name="id_or_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_perform_operation(self, client: Kernel) -> None:
        item = client.vaults.items.perform_operation(
            key="key",
            id_or_name="id_or_name",
            type="authorize",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_perform_operation(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.perform_operation(
            key="key",
            id_or_name="id_or_name",
            type="authorize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_perform_operation(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.perform_operation(
            key="key",
            id_or_name="id_or_name",
            type="authorize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_perform_operation(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.perform_operation(
                key="key",
                id_or_name="",
                type="authorize",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.perform_operation(
                key="",
                id_or_name="id_or_name",
                type="authorize",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_overload_1(self, client: Kernel) -> None:
        item = client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params_overload_1(self, client: Kernel) -> None:
        item = client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert_overload_1(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert_overload_1(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert_overload_1(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.upsert(
                key="x",
                id_or_name="",
                spec={
                    "authorization": {
                        "client": {"type": "kernel_managed"},
                        "method": "oauth",
                    },
                    "provider": "link",
                },
                type="wallet",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.upsert(
                key="",
                id_or_name="id_or_name",
                spec={
                    "authorization": {
                        "client": {"type": "kernel_managed"},
                        "method": "oauth",
                    },
                    "provider": "link",
                },
                type="wallet",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_overload_2(self, client: Kernel) -> None:
        item = client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
            },
            type="card",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params_overload_2(self, client: Kernel) -> None:
        item = client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
                "expires_at": 0,
                "line_items": [
                    {
                        "name": "name",
                        "description": "description",
                        "image_url": "image_url",
                        "product_url": "product_url",
                        "quantity": 1,
                        "sku": "sku",
                        "totals": [
                            {
                                "amount": 0,
                                "display_text": "display_text",
                                "type": "type",
                            }
                        ],
                        "unit_amount": 0,
                        "url": "url",
                    }
                ],
                "metadata": {"foo": "string"},
                "totals": [
                    {
                        "amount": 0,
                        "display_text": "display_text",
                        "type": "type",
                    }
                ],
            },
            type="card",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert_overload_2(self, client: Kernel) -> None:
        response = client.vaults.items.with_raw_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
            },
            type="card",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert_overload_2(self, client: Kernel) -> None:
        with client.vaults.items.with_streaming_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
            },
            type="card",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert_overload_2(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vaults.items.with_raw_response.upsert(
                key="x",
                id_or_name="",
                spec={
                    "amount": 1,
                    "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "currency": "bFx",
                    "merchant_name": "x",
                    "merchant_url": "https://example.com",
                    "payment_method_id": "x",
                    "provider": "link",
                    "wallet": "wallet",
                },
                type="card",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.vaults.items.with_raw_response.upsert(
                key="",
                id_or_name="id_or_name",
                spec={
                    "amount": 1,
                    "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "currency": "bFx",
                    "merchant_name": "x",
                    "merchant_url": "https://example.com",
                    "payment_method_id": "x",
                    "provider": "link",
                    "wallet": "wallet",
                },
                type="card",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.retrieve(
            key="x",
            id_or_name="id_or_name",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.retrieve(
            key="x",
            id_or_name="id_or_name",
            expand=["payment_methods"],
            wait=0,
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.retrieve(
            key="x",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.retrieve(
            key="x",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.retrieve(
                key="x",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.retrieve(
                key="",
                id_or_name="id_or_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
            },
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
                "expires_at": 0,
                "line_items": [
                    {
                        "name": "name",
                        "description": "description",
                        "image_url": "image_url",
                        "product_url": "product_url",
                        "quantity": 1,
                        "sku": "sku",
                        "totals": [
                            {
                                "amount": 0,
                                "display_text": "display_text",
                                "type": "type",
                            }
                        ],
                        "unit_amount": 0,
                        "url": "url",
                    }
                ],
                "metadata": {"foo": "string"},
                "totals": [
                    {
                        "amount": 0,
                        "display_text": "display_text",
                        "type": "type",
                    }
                ],
            },
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.update(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 3000,
                "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                "currency": "usd",
                "merchant_name": "Example Store",
                "merchant_url": "https://store.example.com",
                "payment_method_id": "pm_example",
                "provider": "link",
                "wallet": "link-wallet",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.update(
                key="x",
                id_or_name="",
                spec={
                    "amount": 3000,
                    "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                    "currency": "usd",
                    "merchant_name": "Example Store",
                    "merchant_url": "https://store.example.com",
                    "payment_method_id": "pm_example",
                    "provider": "link",
                    "wallet": "link-wallet",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.update(
                key="",
                id_or_name="id_or_name",
                spec={
                    "amount": 3000,
                    "context": "The order total changed to USD 30.00 including shipping and taxes for one notebook. Update this unapproved request rather than creating a second payment.",
                    "currency": "usd",
                    "merchant_name": "Example Store",
                    "merchant_url": "https://store.example.com",
                    "payment_method_id": "pm_example",
                    "provider": "link",
                    "wallet": "link-wallet",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.list(
            "id_or_name",
        )
        assert_matches_type(ItemListResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.list(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemListResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.list(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemListResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.delete(
            key="x",
            id_or_name="id_or_name",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.delete(
            key="x",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.delete(
            key="x",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.delete(
                key="x",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.delete(
                key="",
                id_or_name="id_or_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.events(
            key="key",
            id_or_name="id_or_name",
        )
        assert_matches_type(ItemEventsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.events(
            key="key",
            id_or_name="id_or_name",
            after="after",
            wait=0,
        )
        assert_matches_type(ItemEventsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.events(
            key="key",
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemEventsResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.events(
            key="key",
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemEventsResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_events(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.events(
                key="key",
                id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.events(
                key="",
                id_or_name="id_or_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_perform_operation(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.perform_operation(
            key="key",
            id_or_name="id_or_name",
            type="authorize",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_perform_operation(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.perform_operation(
            key="key",
            id_or_name="id_or_name",
            type="authorize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_perform_operation(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.perform_operation(
            key="key",
            id_or_name="id_or_name",
            type="authorize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_perform_operation(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.perform_operation(
                key="key",
                id_or_name="",
                type="authorize",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.perform_operation(
                key="",
                id_or_name="id_or_name",
                type="authorize",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_overload_1(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params_overload_1(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert_overload_1(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert_overload_1(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "authorization": {
                    "client": {"type": "kernel_managed"},
                    "method": "oauth",
                },
                "provider": "link",
            },
            type="wallet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert_overload_1(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.upsert(
                key="x",
                id_or_name="",
                spec={
                    "authorization": {
                        "client": {"type": "kernel_managed"},
                        "method": "oauth",
                    },
                    "provider": "link",
                },
                type="wallet",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.upsert(
                key="",
                id_or_name="id_or_name",
                spec={
                    "authorization": {
                        "client": {"type": "kernel_managed"},
                        "method": "oauth",
                    },
                    "provider": "link",
                },
                type="wallet",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_overload_2(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
            },
            type="card",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params_overload_2(self, async_client: AsyncKernel) -> None:
        item = await async_client.vaults.items.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
                "expires_at": 0,
                "line_items": [
                    {
                        "name": "name",
                        "description": "description",
                        "image_url": "image_url",
                        "product_url": "product_url",
                        "quantity": 1,
                        "sku": "sku",
                        "totals": [
                            {
                                "amount": 0,
                                "display_text": "display_text",
                                "type": "type",
                            }
                        ],
                        "unit_amount": 0,
                        "url": "url",
                    }
                ],
                "metadata": {"foo": "string"},
                "totals": [
                    {
                        "amount": 0,
                        "display_text": "display_text",
                        "type": "type",
                    }
                ],
            },
            type="card",
        )
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert_overload_2(self, async_client: AsyncKernel) -> None:
        response = await async_client.vaults.items.with_raw_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
            },
            type="card",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(VaultItem, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert_overload_2(self, async_client: AsyncKernel) -> None:
        async with async_client.vaults.items.with_streaming_response.upsert(
            key="x",
            id_or_name="id_or_name",
            spec={
                "amount": 1,
                "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "currency": "bFx",
                "merchant_name": "x",
                "merchant_url": "https://example.com",
                "payment_method_id": "x",
                "provider": "link",
                "wallet": "wallet",
            },
            type="card",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(VaultItem, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert_overload_2(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vaults.items.with_raw_response.upsert(
                key="x",
                id_or_name="",
                spec={
                    "amount": 1,
                    "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "currency": "bFx",
                    "merchant_name": "x",
                    "merchant_url": "https://example.com",
                    "payment_method_id": "x",
                    "provider": "link",
                    "wallet": "wallet",
                },
                type="card",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.vaults.items.with_raw_response.upsert(
                key="",
                id_or_name="id_or_name",
                spec={
                    "amount": 1,
                    "context": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "currency": "bFx",
                    "merchant_name": "x",
                    "merchant_url": "https://example.com",
                    "payment_method_id": "x",
                    "provider": "link",
                    "wallet": "wallet",
                },
                type="card",
            )
