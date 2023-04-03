from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import (
    Fieldset, GovUKComponent, GovUKFieldComponent)


class DateInputItem(TypedDict):
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
