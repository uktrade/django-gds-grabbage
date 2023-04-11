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
class RadiosItems:
    text: Optional[str] = None
    html: Optional[str] = None
    id: Optional[str] = None
    value: str
    label: Optional[Dict[str, Any]] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    divider: Optional[str] = None
    checked: Optional[bool] = None
    conditional: Optional[str] = None
    conditional.html: Optional[str] = None
    disabled: Optional[bool] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class GovUKRadios(govuk_frontend_base.GovUKComponent):
    """GovUK Radios

    See: https://design-system.service.gov.uk/components/radios/
    """

    fieldset: Optional[govuk_frontend_fieldset.GovUKFieldset] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    idPrefix: Optional[str] = None
    name: str
    items: List[RadiosItems]
    value: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/radios/macro.html"
    _macro_name = "govukRadios"


COMPONENT = GovUKRadios
