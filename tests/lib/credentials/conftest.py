from __future__ import annotations

from typing import Iterator

import pytest

from kernel.lib.credentials import _auth, _chain

from .utils import FEDERATION_ENV_VARS


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    for name in FEDERATION_ENV_VARS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(_auth, "_warned_api_key_shadows_federation", False)
    monkeypatch.setattr(_chain, "_env_tokens", {})
    yield
