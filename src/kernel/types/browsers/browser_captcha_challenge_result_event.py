# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserCaptchaChallengeResultEvent", "Data"]


class Data(BaseModel):
    """Per-challenge payload.

    This event is emitted once per challenge and determines its overall outcome; captcha_solve_started and captcha_solve_result describe individual tasks and may occur multiple times within the challenge.
    """

    captcha_type: Literal["hcaptcha", "recaptcha_v2", "recaptcha_v3", "turnstile", "geetest", "press_and_hold", "other"]
    """Deprecated: use captcha_provider."""

    challenge_id: str
    """Opaque identifier shared by events for one visible challenge.

    An image-grid captcha may create multiple task_id values for one challenge_id.
    The same value may continue across a page reload when the challenge episode
    continues. It does not indicate task ordering or challenge completion.
    """

    duration_ms: float
    """
    Wall-clock duration from the challenge appearing to its terminal outcome,
    covering every solver attempt in between.
    """

    status: Literal["solved", "failure", "timeout", "abandoned"]
    """Terminal outcome of the visible challenge.

    solved: the page observed the challenge clear after a solver attempt. failure: a
    terminal solver failure occurred, or all attempts ended while the challenge
    remained. timeout: the challenge-level wait budget expired while the challenge
    remained. abandoned: observation ended without an attributable terminal
    challenge outcome. This includes a dismissed widget or page unload without a
    solved signal or terminal solver outcome, and a token appearing while multiple
    same-provider challenges are open, because the producer cannot attribute that
    token to this visible challenge. A captcha_solve_result with the same
    challenge_id may therefore report success while the challenge result reports
    abandoned. A solved challenge does not prove the site accepted the token or that
    the guarded action succeeded.
    """

    captcha_provider: Optional[
        Literal["hcaptcha", "recaptcha_v2", "recaptcha_v3", "turnstile", "geetest", "arkose", "human", "other"]
    ] = None
    """Captcha product the challenge belongs to, not the service that solved it.

    Enterprise reCAPTCHA variants are grouped into their version bucket
    (recaptcha_v2 or recaptcha_v3), FunCaptcha uses arkose, press-and-hold
    challenges served by HUMAN (formerly PerimeterX) use human, and unlisted
    products use other.
    """

    website_host: Optional[str] = None
    """Host of the page where the challenge appeared."""

    website_path: Optional[str] = None
    """Path of the page where the challenge appeared. Query string excluded."""


class BrowserCaptchaChallengeResultEvent(BaseModel):
    """A visible captcha challenge reached a terminal outcome."""

    category: Literal["captcha"]

    data: Data
    """Per-challenge payload.

    This event is emitted once per challenge and determines its overall outcome;
    captcha_solve_started and captcha_solve_result describe individual tasks and may
    occur multiple times within the challenge.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["captcha_challenge_result"]

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
