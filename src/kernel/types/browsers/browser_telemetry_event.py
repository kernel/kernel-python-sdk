# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .browser_api_call_event import BrowserAPICallEvent
from .browser_page_lcp_event import BrowserPageLcpEvent
from .browser_page_load_event import BrowserPageLoadEvent
from .browser_console_log_event import BrowserConsoleLogEvent
from .browser_cdp_connect_event import BrowserCdpConnectEvent
from .browser_network_idle_event import BrowserNetworkIdleEvent
from .browser_console_error_event import BrowserConsoleErrorEvent
from .browser_cdp_disconnect_event import BrowserCdpDisconnectEvent
from .browser_interaction_key_event import BrowserInteractionKeyEvent
from .browser_network_request_event import BrowserNetworkRequestEvent
from .browser_page_navigation_event import BrowserPageNavigationEvent
from .browser_page_tab_opened_event import BrowserPageTabOpenedEvent
from .browser_service_crashed_event import BrowserServiceCrashedEvent
from .browser_system_oom_kill_event import BrowserSystemOomKillEvent
from .browser_network_response_event import BrowserNetworkResponseEvent
from .browser_interaction_click_event import BrowserInteractionClickEvent
from .browser_live_view_connect_event import BrowserLiveViewConnectEvent
from .browser_page_layout_shift_event import BrowserPageLayoutShiftEvent
from .browser_monitor_screenshot_event import BrowserMonitorScreenshotEvent
from .browser_monitor_init_failed_event import BrowserMonitorInitFailedEvent
from .browser_monitor_reconnected_event import BrowserMonitorReconnectedEvent
from .browser_page_layout_settled_event import BrowserPageLayoutSettledEvent
from .browser_captcha_solve_result_event import BrowserCaptchaSolveResultEvent
from .browser_live_view_disconnect_event import BrowserLiveViewDisconnectEvent
from .browser_monitor_disconnected_event import BrowserMonitorDisconnectedEvent
from .browser_network_loading_failed_event import BrowserNetworkLoadingFailedEvent
from .browser_page_dom_content_loaded_event import BrowserPageDomContentLoadedEvent
from .browser_page_navigation_settled_event import BrowserPageNavigationSettledEvent
from .browser_monitor_reconnect_failed_event import BrowserMonitorReconnectFailedEvent
from .browser_interaction_scroll_settled_event import BrowserInteractionScrollSettledEvent

__all__ = ["BrowserTelemetryEvent"]

BrowserTelemetryEvent: TypeAlias = Annotated[
    Union[
        BrowserConsoleLogEvent,
        BrowserConsoleErrorEvent,
        BrowserNetworkRequestEvent,
        BrowserNetworkResponseEvent,
        BrowserNetworkLoadingFailedEvent,
        BrowserNetworkIdleEvent,
        BrowserPageNavigationEvent,
        BrowserPageDomContentLoadedEvent,
        BrowserPageLoadEvent,
        BrowserPageTabOpenedEvent,
        BrowserPageLayoutShiftEvent,
        BrowserPageLcpEvent,
        BrowserPageLayoutSettledEvent,
        BrowserPageNavigationSettledEvent,
        BrowserInteractionClickEvent,
        BrowserInteractionKeyEvent,
        BrowserInteractionScrollSettledEvent,
        BrowserMonitorScreenshotEvent,
        BrowserMonitorDisconnectedEvent,
        BrowserMonitorReconnectedEvent,
        BrowserMonitorReconnectFailedEvent,
        BrowserMonitorInitFailedEvent,
        BrowserAPICallEvent,
        BrowserCdpConnectEvent,
        BrowserCdpDisconnectEvent,
        BrowserLiveViewConnectEvent,
        BrowserLiveViewDisconnectEvent,
        BrowserCaptchaSolveResultEvent,
        BrowserSystemOomKillEvent,
        BrowserServiceCrashedEvent,
    ],
    PropertyInfo(discriminator="type"),
]
