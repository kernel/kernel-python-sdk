# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserCaptchaChallengeResultEvent", "Data"]


class Data(BaseModel):
    """An observed challenge emits one outcome across any number of solver tasks.

    For eligible providers without a widget observer, each successful token task emits an inferred solved result instead; multiple such results may belong to one challenge. Failed tasks and image_challenge rounds produce no inferred result. Exactly one of challenge_id or task_id is present: challenge_id on an observed result, task_id on an inferred one. A challenge whose tasks all fail produces task events only, so consumers fall back to captcha_solve_result for it.
    """

    captcha_type: Literal["hcaptcha", "recaptcha_v2", "recaptcha_v3", "turnstile", "geetest", "press_and_hold", "other"]
    """Deprecated: use captcha_provider."""

    duration_ms: float
    """
    Wall-clock duration from the challenge appearing to its terminal outcome,
    covering every solver attempt in between. For an inferred result, the duration
    of its solver task.
    """

    status: Literal["solved", "failure", "timeout", "abandoned"]
    """Terminal outcome of a challenge.

    solved: the page observed the challenge clear after a solver attempt, or an
    inferred result reports a token for the whole widget without page observation.
    failure: a terminal solver failure occurred, or all attempts ended while the
    challenge remained. timeout: the challenge-level wait budget expired while the
    challenge remained. abandoned: observation ended without an attributable
    terminal challenge outcome. This includes a dismissed widget or page unload
    without a solved signal or terminal solver outcome, and a token appearing while
    multiple same-provider challenges are open, because the producer cannot
    attribute that token to this visible challenge. A captcha_solve_result with the
    same challenge_id may therefore report success while the challenge result
    reports abandoned. A solved challenge does not prove the site accepted the token
    or that the guarded action succeeded.
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

    challenge_id: Optional[str] = None
    """Opaque identifier shared by events for one visible challenge.

    An image-grid captcha may create multiple task_id values for one challenge_id.
    The same value may continue across a page reload when the challenge episode
    continues. It does not indicate task ordering or challenge completion.
    """

    inferred: Optional[bool] = None
    """
    True when the relay derived this result from a successful token task without
    observing the page. An inferred result has task_id instead of challenge_id.
    Absent on page-observed results.
    """

    task_id: Optional[str] = None
    """The task_id of the solver task an inferred result was derived from.

    Join on it to pair the result with that task's captcha_solve_started and
    captcha_solve_result. Present only when inferred is true.
    """

    website_host: Optional[str] = None
    """Host of the page where the challenge appeared."""

    website_path: Optional[str] = None
    """Path of the page where the challenge appeared. Query string excluded."""


class BrowserCaptchaChallengeResultEvent(BaseModel):
    """A captcha challenge reached an observed or inferred terminal outcome."""

    category: Literal["captcha"]

    data: Data
    """An observed challenge emits one outcome across any number of solver tasks.

    For eligible providers without a widget observer, each successful token task
    emits an inferred solved result instead; multiple such results may belong to one
    challenge. Failed tasks and image_challenge rounds produce no inferred result.
    Exactly one of challenge_id or task_id is present: challenge_id on an observed
    result, task_id on an inferred one. A challenge whose tasks all fail produces
    task events only, so consumers fall back to captcha_solve_result for it.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["captcha_challenge_result"]

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
