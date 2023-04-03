from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


class CookieBannerMessageAction(TypedDict):
    text: str
    type: Optional[str]
    name: Optional[str]
    value: Optional[str]
    href: Optional[str]

class CookieBannerMessageItem(TypedDict):
    headingText: Optional[str]
    html: str
    role: Optional[str]
    actions: List[CookieBannerMessageAction]
    hidden: Optional[bool]

@dataclass(kw_only=True)
class GovUKCookieBanner(GovUKComponent):
    """GovUK Cookie Banner

    See: https://design-system.service.gov.uk/components/cookie-banner/
    """

    ariaLabel: str
    messages: List[CookieBannerMessageItem]

    _jinja2_template = "govuk_frontend_jinja/components/cookie-banner/macro.html"
    _macro_name = "govukCookieBanner"
