from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import (
    Fieldset, GovUKFieldComponent, HintText)


class CheckboxDivider(TypedDict):
    divider: str

class CheckboxItem(TypedDict):
    value: str
    text: str
    hint: Optional[HintText]
    behaviour: Optional[str]

class ErrorMesage(TypedDict):
    text: str

@dataclass(kw_only=True)
class GovUKCheckboxes(GovUKFieldComponent):
    fieldset: Fieldset
    items: List[CheckboxDivider | CheckboxItem]
    error_message: ErrorMesage

    jinja2_template = "govuk_frontend_jinja/components/checkboxes/macro.html"
    macro_name = "govukCheckboxes"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            fieldset=self.fieldset,
            items=self.items,
            errorMessage=self.error_message,
        )
        return data
