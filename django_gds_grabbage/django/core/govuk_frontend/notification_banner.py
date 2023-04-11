
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from django_gds_grabbage.django.core.govuk_frontend import base as govuk_frontend_base
from django_gds_grabbage.django.core.govuk_frontend import error_message as govuk_frontend_error_message
from django_gds_grabbage.django.core.govuk_frontend import hint as govuk_frontend_hint
from django_gds_grabbage.django.core.govuk_frontend import fieldset as govuk_frontend_fieldset


@dataclass(kw_only=True)
class GovUKNotificationBanner(govuk_frontend_base.GovUKComponent):
    """GovUK Notification Banner

    See: https://design-system.service.gov.uk/components/notification-banner/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    titleText: Optional[str] = None
    titleHtml: Optional[str] = None
    titleHeadingLevel: Optional[str] = None
    type: Optional[str] = None
    role: Optional[str] = None
    titleId: Optional[str] = None
    disableAutoFocus: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/notification-banner/macro.html"
    _macro_name = "govukNotificationBanner"
