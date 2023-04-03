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
    id: str
    name_prefix: str
    items: List[DateInputItem]

    jinja2_template = "govuk_frontend_jinja/components/date-input/macro.html"
    macro_name = "govukDateInput"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            id=self.id,
            namePrefix=self.name_prefix,
            items=self.items,
        )
        return data
