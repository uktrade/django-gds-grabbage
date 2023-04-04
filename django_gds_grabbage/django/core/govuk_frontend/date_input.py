from dataclasses import dataclass
from typing import List

from django_gds_grabbage.django.core.govuk_frontend.base import GovUKFieldComponent


@dataclass(kw_only=True)
class DateInputItem:
    classes: str
    name: str
    value: str


@dataclass(kw_only=True)
class GovUKDateInput(GovUKFieldComponent):
    """GovUK Date Input

    See: https://design-system.service.gov.uk/components/date-input/
    """

    id: str
    namePrefix: str
    items: List[DateInputItem]

    _jinja2_template = "govuk_frontend_jinja/components/date-input/macro.html"
    _macro_name = "govukDateInput"
