from dataclasses import dataclass
from typing import Optional

from django_gds_grabbage.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUKErrorMessage(GovUKComponent):
    """GovUK Error Message

    See: https://design-system.service.gov.uk/components/error-message/
    """

    id: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    visuallyHiddenText: str = ""

    _jinja2_template = "govuk_frontend_jinja/components/error-message/macro.html"
    _macro_name = "govukErrorMessage"
