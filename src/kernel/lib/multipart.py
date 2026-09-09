from __future__ import annotations

from typing import Mapping, Sequence, cast

from .._utils import is_given

__all__ = ["indexed_multipart_body"]


def indexed_multipart_body(body: object) -> dict[str, object]:
    """Flatten a multipart body so that array entries carry their index.

    Endpoints that take an array of objects with a file field need each entry's
    fields grouped together: `files[0][dest_path]` pairs with the `files[0][file]`
    part, while repeated `files[][dest_path]` names cannot be matched back to
    their file. The returned mapping is already flat, so the client's generic
    multipart serialization passes the names through untouched and every other
    endpoint keeps its existing encoding.
    """
    flattened: dict[str, object] = {}
    if isinstance(body, Mapping):
        for key, value in cast(Mapping[object, object], body).items():
            _flatten(str(key), value, flattened)
    return flattened


def _flatten(key: str, value: object, out: dict[str, object]) -> None:
    if not is_given(value):
        return

    if isinstance(value, Mapping):
        for child_key, child in cast(Mapping[object, object], value).items():
            _flatten(f"{key}[{child_key}]", child, out)
        return

    if isinstance(value, (list, tuple)):
        for index, child in enumerate(cast(Sequence[object], value)):
            _flatten(f"{key}[{index}]", child, out)
        return

    out[key] = value
