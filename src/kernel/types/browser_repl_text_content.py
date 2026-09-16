# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrowserReplTextContent"]


class BrowserReplTextContent(BaseModel):
    channel: Literal["write", "stdout", "stderr"]
    """
    `write` is emitted by `repl.write`; `stdout` and `stderr` are emitted by console
    methods.
    """

    text: str

    type: Literal["text"]
