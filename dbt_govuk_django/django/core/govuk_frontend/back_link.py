from dataclasses import dataclass
from typing import Any, Dict, Optional

from dbt_govuk_django.django.core.govuk_frontend.base import Attributes, GovUKComponent


@dataclass(kw_only=True)
class GovUKBackLink(GovUKComponent):
    """GovUK Back Link

    See: https://design-system.service.gov.uk/components/back-link/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    href: str

    _jinja2_template = "govuk_frontend_jinja/components/back-link/macro.html"
    _macro_name = "govukBackLink"
