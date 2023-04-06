
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from django_gds_grabbage.django.core.govuk_frontend import base as govuk_frontend_base
from django_gds_grabbage.django.core.govuk_frontend import error_message as govuk_frontend_error_message
from django_gds_grabbage.django.core.govuk_frontend import hint as govuk_frontend_hint
from django_gds_grabbage.django.core.govuk_frontend import fieldset as govuk_frontend_fieldset


@dataclass(kw_only=True)
class GovUKBackLink(govuk_frontend_base.GovUKComponent):
    """GovUK Back Link

    See: https://design-system.service.gov.uk/components/back-link/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    href: str

    _jinja2_template = "govuk_frontend_jinja/components/back-link/macro.html"
    _macro_name = "govukBackLink"

