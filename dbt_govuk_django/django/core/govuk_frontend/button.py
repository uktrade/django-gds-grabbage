from dataclasses import dataclass
from typing import Optional

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUKButton(GovUKComponent):
    """GovUK Button

    See: https://design-system.service.gov.uk/components/button/
    """

    element: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    disabled: bool = False
    href: Optional[str] = None
    preventDoubleClick: bool = True
    isStartButton: bool = False

    _jinja2_template = "govuk_frontend_jinja/components/button/macro.html"
    _macro_name = "govukButton"
