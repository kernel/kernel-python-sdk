# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ConfigRegistryResolveParams"]


class ConfigRegistryResolveParams(TypedDict, total=False):
    url: Required[str]
    """Public HTTP(S) URL to refresh."""

    allowed_proxy_countries: SequenceNotStr[str]
    """
    ISO 3166 country codes Kernel may use when searching for or returning a proxy
    configuration. Kernel may test a subset of allowed countries. When omitted,
    Kernel uses its default country selection.
    """

    intent: str
    """
    Plain-language description of the workload you intend to run against this
    target, in a sentence or two. Requires an https target, because the pass treats
    any non-HTTPS destination as off-site and will not drive an http one. Kernel
    uses it to drive the browser further into the site, where it can observe
    protections that only appear once a session interacts. When this target already
    has a verified configuration, the run confirms that one instead of re-deriving
    the whole matrix, so supplying an intent narrows what can be recommended.
    """
