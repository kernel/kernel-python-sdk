# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..usage import Usage
from ..result import Result
from ..attempt import Attempt
from ..warning import Warning
from ..._models import BaseModel

__all__ = ["Search"]


class Search(BaseModel):
    """Retained search results and provider attempt history."""

    id: str
    """Search resource ID. Request tracing uses X-Request-Id."""

    attempts: List[Attempt]

    expires_at: datetime
    """Expiration of result IDs for deferred retrieval.

    Results expire 24 hours after search completion.
    """

    provider: str
    """Concrete serving provider, never auto or fallback."""

    query: str
    """Echo of the query.

    Native multi-query inputs are visible in the selected strategy target and the
    optional raw response.
    """

    results: List[Result]

    usage: Usage

    warnings: List[Warning]

    answer: Optional[str] = None
    """Provider-generated answer when requested (e.g.

    via Tavily include_answer or Perplexity). Preserved independently of
    include_raw.
    """

    raw: Optional[object] = None
    """
    Full serving-provider response, including top-level metadata that does not
    belong to a result. Present only with include_raw=true; untrusted provider data.
    """
