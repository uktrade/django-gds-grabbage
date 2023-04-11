from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from django_gds_grabbage.gds_components.govuk_frontend import (
    base as govuk_frontend_base,
)
from django_gds_grabbage.gds_components.govuk_frontend import (
    error_message as govuk_frontend_error_message,
)
from django_gds_grabbage.gds_components.govuk_frontend import (
    fieldset as govuk_frontend_fieldset,
)
from django_gds_grabbage.gds_components.govuk_frontend import (
    hint as govuk_frontend_hint,
)


@dataclass(kw_only=True)
class CookieBannerMessagesActions:
    text: str
    type: Optional[str] = None
    href: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class CookieBannerMessages:
    headingText: Optional[str] = None
    headingHtml: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    actions: Optional[List[CookieBannerMessagesActions]] = None
    hidden: Optional[bool] = None
    role: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class GovUKCookieBanner(govuk_frontend_base.GovUKComponent):
    """GovUK Cookie Banner

    See: https://design-system.service.gov.uk/components/cookie-banner/
    """

    ariaLabel: Optional[str] = None
    hidden: Optional[bool] = None
    messages: List[CookieBannerMessages]

    _jinja2_template = "govuk_frontend_jinja/components/cookie-banner/macro.html"
    _macro_name = "govukCookieBanner"


COMPONENT = GovUKCookieBanner
