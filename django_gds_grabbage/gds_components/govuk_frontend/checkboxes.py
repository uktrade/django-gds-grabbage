from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from django_gds_grabbage.gds_components.govuk_frontend import (
    base as govuk_frontend_base,
)
from django_gds_grabbage.gds_components.govuk_frontend import (
    error_message as govuk_frontend_error_message,
)
from django_gds_grabbage.gds_components.govuk_frontend import (
    fieldset as govuk_frontend_fieldset,
)
from django_gds_grabbage.gds_components.govuk_frontend import (
    hint as govuk_frontend_hint,
)


@dataclass(kw_only=True)
class CheckboxesItems:
    text: Optional[str] = None
    html: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    value: str
    label: Optional[Dict[str, Any]] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    divider: Optional[str] = None
    checked: Optional[bool] = None
    conditional: Optional[govuk_frontend_base.CheckboxesConditional] = None
    behaviour: Optional[str] = None
    disabled: Optional[bool] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class GovUKCheckboxes(govuk_frontend_base.GovUKComponent):
    """GovUK Checkboxes

    See: https://design-system.service.gov.uk/components/checkboxes/
    """

    describedBy: Optional[str] = None
    fieldset: Optional[govuk_frontend_fieldset.GovUKFieldset] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    idPrefix: Optional[str] = None
    name: str
    items: List[CheckboxesItems]
    values: Optional[List[str]] = None

    _jinja2_template = "govuk_frontend_jinja/components/checkboxes/macro.html"
    _macro_name = "govukCheckboxes"


COMPONENT = GovUKCheckboxes
