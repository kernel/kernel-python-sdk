# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserCaptchaSolveResultEvent", "Data"]


class Data(BaseModel):
    captcha_type: Literal["hcaptcha", "recaptcha_v2", "recaptcha_v3", "turnstile", "geetest", "other"]
    """Captcha vendor family.

    Provider-specific task names are normalized into this set; anything not covered
    is reported as other.
    """

    duration_ms: float
    """Wall-clock duration from solve start to terminal outcome."""

    status: Literal["success", "failure", "timeout", "abandoned"]
    """Terminal outcome.

    success: solver returned a usable solution. failure: solver returned an error
    (see error_code). timeout: solver did not return within the caller's wait
    budget. abandoned: caller cancelled or the page navigated away mid-solve.
    """

    error_code: Optional[str] = None
    """Solver-specific error code on failure (e.g.

    ERROR_CAPTCHA_UNSOLVABLE). Absent on success.
    """

    task_id: Optional[str] = None
    """Solver-assigned identifier. Opaque, useful for support cross-references."""

    website_host: Optional[str] = None
    """Host of the page where the captcha was solved."""

    website_path: Optional[str] = None
    """Path of the page where the captcha was solved. Query string excluded."""


class BrowserCaptchaSolveResultEvent(BaseModel):
    """A captcha solve attempt reached a terminal outcome."""

    category: Literal["captcha"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["captcha_solve_result"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
