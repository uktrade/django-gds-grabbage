from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import (
    Fieldset, GovUKFieldComponent, HintText)
from dbt_govuk_django.django.core.govuk_frontend.error_message import \
    GovUKErrorMessage


class CheckboxDivider(TypedDict):
    divider: str

class CheckboxItem(TypedDict):
    value: str
    text: str
    hint: Optional[HintText]
    behaviour: Optional[str]

@dataclass(kw_only=True)
class GovUKCheckboxes(GovUKFieldComponent):
    """GovUK Checkboxes

    See: https://design-system.service.gov.uk/components/checkboxes/
    """

    fieldset: Fieldset
    items: List[CheckboxDivider | CheckboxItem]

    jinja2_template = "govuk_frontend_jinja/components/checkboxes/macro.html"
    macro_name = "govukCheckboxes"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            fieldset=self.fieldset,
            items=self.items,
        )
        return data
