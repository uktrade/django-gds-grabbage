from dataclasses import dataclass
from typing import List, Optional, TypedDict

from django_gds_grabbage.django.core.govuk_frontend.base import (
    FormGroup,
    GovUKFieldComponent,
    HintText,
)


@dataclass(kw_only=True)
class CheckboxDivider:
    divider: str


@dataclass(kw_only=True)
class CheckboxItem:
    value: str
    text: str
    hint: Optional[HintText]
    behaviour: Optional[str]


@dataclass(kw_only=True)
class GovUKCheckboxes(GovUKFieldComponent):
    """GovUK Checkboxes

    See: https://design-system.service.gov.uk/components/checkboxes/
    """

    items: List[CheckboxDivider | CheckboxItem]
    describedBy: Optional[str] = None
    formGroup: Optional[FormGroup] = None
    idPrefix: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/checkboxes/macro.html"
    _macro_name = "govukCheckboxes"
