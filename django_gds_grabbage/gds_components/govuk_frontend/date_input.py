from dataclasses import dataclass
from typing import List, Optional

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
from django_gds_grabbage.gds_components.govuk_frontend import (
    label as govuk_frontend_label,
)
from django_gds_grabbage.gds_components.govuk_frontend import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class DateInputItems:
    id: Optional[str] = None
    name: str
    label: Optional[govuk_frontend_label.GovUKLabel] = None
    value: Optional[str] = None
    autocomplete: Optional[str] = None
    pattern: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKDateInput(govuk_frontend_base.GovUKComponent):
    """GovUK Date Input

    See: https://design-system.service.gov.uk/components/date-input/
    """

    id: str
    namePrefix: Optional[str] = None
    items: Optional[List[DateInputItems]] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    fieldset: Optional[govuk_frontend_fieldset.GovUKFieldset] = None

    _jinja2_template = "govuk_frontend_jinja/components/date-input/macro.html"
    _macro_name = "govukDateInput"


COMPONENT = GovUKDateInput
