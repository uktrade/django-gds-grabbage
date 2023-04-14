from dataclasses import dataclass
from typing import Optional

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
class GovUKTextarea(govuk_frontend_base.GovUKComponent):
    """GovUK Textarea

    See: https://design-system.service.gov.uk/components/textarea/
    """

    id: str
    name: str
    spellcheck: Optional[bool] = None
    rows: Optional[str] = None
    value: Optional[str] = None
    disabled: Optional[bool] = None
    describedBy: Optional[str] = None
    label: govuk_frontend_label.GovUKLabel
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    autocomplete: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/textarea/macro.html"
    _macro_name = "govukTextarea"


COMPONENT = GovUKTextarea
