# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._utils import is_mapping, maybe_coerce_boolean, maybe_coerce_integer
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPageTokenPagination", "AsyncPageTokenPagination", "SyncOffsetPagination", "AsyncOffsetPagination"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class SyncPageTokenPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None
    has_more: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(params={"page_token": next_page_token})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                "next_page_token": response.headers.get("X-Next-Page-Token"),
                "has_more": maybe_coerce_boolean(response.headers.get("X-Has-More")),
            },
        )


class AsyncPageTokenPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None
    has_more: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(params={"page_token": next_page_token})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                "next_page_token": response.headers.get("X-Next-Page-Token"),
                "has_more": maybe_coerce_boolean(response.headers.get("X-Has-More")),
            },
        )


class SyncOffsetPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    has_more: Optional[bool] = None
    next_offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset = self.next_offset
        if next_offset is None:
            if self.has_more:  # type: ignore[unreachable]
                raise RuntimeError(
                    "Server reported X-Has-More: true without an X-Next-Offset header; "
                    "refusing to silently truncate pagination"
                )
            return None

        # X-Next-Offset is the next page's absolute start, or 0 on the last page
        # (the API's stop sentinel). Only a positive offset advances; the old code
        # added the current page length on top, skipping a page per iteration.
        if next_offset == 0:
            return None

        return PageInfo(params={"offset": next_offset})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                "has_more": maybe_coerce_boolean(response.headers.get("X-Has-More")),
                "next_offset": maybe_coerce_integer(response.headers.get("X-Next-Offset")),
            },
        )


class AsyncOffsetPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    has_more: Optional[bool] = None
    next_offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset = self.next_offset
        if next_offset is None:
            if self.has_more:  # type: ignore[unreachable]
                raise RuntimeError(
                    "Server reported X-Has-More: true without an X-Next-Offset header; "
                    "refusing to silently truncate pagination"
                )
            return None

        # X-Next-Offset is the next page's absolute start, or 0 on the last page
        # (the API's stop sentinel). Only a positive offset advances; the old code
        # added the current page length on top, skipping a page per iteration.
        if next_offset == 0:
            return None

        return PageInfo(params={"offset": next_offset})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                "has_more": maybe_coerce_boolean(response.headers.get("X-Has-More")),
                "next_offset": maybe_coerce_integer(response.headers.get("X-Next-Offset")),
            },
        )
