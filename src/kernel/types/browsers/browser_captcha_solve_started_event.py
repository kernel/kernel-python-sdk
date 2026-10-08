# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserCaptchaSolveStartedEvent", "Data"]


class Data(BaseModel):
    """Per-task payload.

    A visible challenge may create multiple tasks. When present, task_id correlates this event with a captcha_solve_result, while challenge_id groups tasks from the same challenge. Events may arrive out of order or be absent, so their arrival does not indicate current solve state.
    """

    captcha_type: Literal["hcaptcha", "recaptcha_v2", "recaptcha_v3", "turnstile", "geetest", "press_and_hold", "other"]
    """Deprecated: use captcha_provider and task_kind."""

    captcha_provider: Optional[
        Literal["hcaptcha", "recaptcha_v2", "recaptcha_v3", "turnstile", "geetest", "arkose", "human", "other"]
    ] = None
    """Captcha product the challenge belongs to, not the service that solved it.

    Enterprise reCAPTCHA variants are grouped into their version bucket
    (recaptcha_v2 or recaptcha_v3), FunCaptcha uses arkose, press-and-hold
    challenges served by HUMAN (formerly PerimeterX) use human, and unlisted
    products use other.
    """

    challenge_id: Optional[str] = None
    """Opaque identifier shared by events for one visible challenge.

    An image-grid captcha may create multiple task_id values for one challenge_id.
    The same value may continue across a page reload when the challenge episode
    continues. It does not indicate task ordering or challenge completion.
    """

    task_id: Optional[str] = None
    """Opaque identifier shared with the matching captcha_solve_result."""

    task_kind: Optional[Literal["token", "image_challenge", "press_and_hold"]] = None
    """What the solver task produces. Absent when the producer cannot tell."""

    website_host: Optional[str] = None
    """Host of the page where the captcha is being solved.

    May be empty for solver tasks that carry no page URL.
    """

    website_path: Optional[str] = None
    """Path of the page where the captcha is being solved. Query string excluded."""


class BrowserCaptchaSolveStartedEvent(BaseModel):
    """A captcha solver accepted a task."""

    category: Literal["captcha"]

    data: Data
    """Per-task payload.

    A visible challenge may create multiple tasks. When present, task_id correlates
    this event with a captcha_solve_result, while challenge_id groups tasks from the
    same challenge. Events may arrive out of order or be absent, so their arrival
    does not indicate current solve state.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["captcha_solve_started"]

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
