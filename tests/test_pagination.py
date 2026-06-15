from typing import Any, List, Type, Union, Optional

import httpx
import pytest

from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

PageClass = Union[Type[SyncOffsetPagination[Any]], Type[AsyncOffsetPagination[Any]]]

# build() and next_page_info() are plain synchronous methods on both classes,
# so both generated variants are pinned against drifting apart on regeneration.
both_classes = pytest.mark.parametrize("cls", [SyncOffsetPagination, AsyncOffsetPagination])


def _page(cls: PageClass, *, items: List[Any], next_offset: Optional[int], has_more: Optional[bool]) -> Any:
    headers: dict[str, str] = {}
    if next_offset is not None:
        headers["X-Next-Offset"] = str(next_offset)
    if has_more is not None:
        headers["X-Has-More"] = "true" if has_more else "false"
    response = httpx.Response(200, headers=headers)
    return cls.build(response=response, data=items)


@both_classes
def test_next_page_starts_at_exactly_x_next_offset(cls: PageClass) -> None:
    # X-Next-Offset already holds the next page's start. Adding the current
    # page length on top (the old behavior) skipped a full page per iteration.
    page = _page(cls, items=[{}] * 100, next_offset=100, has_more=True)
    info = page.next_page_info()
    assert info is not None
    assert info.params == {"offset": 100}


@both_classes
def test_stops_cleanly_when_last_page_omits_x_next_offset(cls: PageClass) -> None:
    page = _page(cls, items=[{}] * 50, next_offset=None, has_more=False)
    assert page.next_page_info() is None
    assert page.has_next_page() is False


@both_classes
def test_stops_when_x_has_more_false(cls: PageClass) -> None:
    # Covers the 0 sentinel the API emits on last pages: has_more is false
    # whenever next_offset is 0, and has_more gates first.
    page = _page(cls, items=[{}] * 50, next_offset=0, has_more=False)
    assert page.has_next_page() is False


@both_classes
def test_stops_on_empty_page(cls: PageClass) -> None:
    page = _page(cls, items=[], next_offset=300, has_more=True)
    assert page.has_next_page() is False


@both_classes
def test_refuses_to_silently_truncate_on_contradictory_headers(cls: PageClass) -> None:
    page = _page(cls, items=[{}] * 100, next_offset=None, has_more=True)
    with pytest.raises(RuntimeError, match="refusing to silently truncate"):
        page.has_next_page()
