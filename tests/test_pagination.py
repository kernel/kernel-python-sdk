from typing import Any, List, Optional

import httpx

from kernel.pagination import SyncOffsetPagination


def _page(
    *, items: List[Any], next_offset: Optional[int], has_more: Optional[bool]
) -> SyncOffsetPagination[Any]:
    headers: dict[str, str] = {}
    if next_offset is not None:
        headers["X-Next-Offset"] = str(next_offset)
    if has_more is not None:
        headers["X-Has-More"] = "true" if has_more else "false"
    response = httpx.Response(200, headers=headers)
    return SyncOffsetPagination.build(response=response, data=items)


def test_next_page_starts_at_exactly_x_next_offset() -> None:
    # X-Next-Offset already holds the next page's start. Adding the current
    # page length on top (the old behavior) skipped a full page per iteration.
    page = _page(items=[{}] * 100, next_offset=100, has_more=True)
    info = page.next_page_info()
    assert info is not None
    assert info.params == {"offset": 100}


def test_stops_when_x_next_offset_absent() -> None:
    page = _page(items=[{}] * 100, next_offset=None, has_more=True)
    assert page.next_page_info() is None
    assert page.has_next_page() is False


def test_stops_when_x_has_more_false() -> None:
    page = _page(items=[{}] * 50, next_offset=200, has_more=False)
    assert page.has_next_page() is False


def test_stops_on_empty_page() -> None:
    page = _page(items=[], next_offset=300, has_more=True)
    assert page.has_next_page() is False
