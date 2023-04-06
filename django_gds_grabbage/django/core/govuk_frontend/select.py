
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from django_gds_grabbage.django.core.govuk_frontend import base as govuk_frontend_base
from django_gds_grabbage.django.core.govuk_frontend import error_message as govuk_frontend_error_message
from django_gds_grabbage.django.core.govuk_frontend import hint as govuk_frontend_hint
from django_gds_grabbage.django.core.govuk_frontend import fieldset as govuk_frontend_fieldset


@dataclass(kw_only=True)
class SelectItems:
    value: Optional[str] = None
    text: str
    selected: Optional[bool] = None
    disabled: Optional[bool] = None
    attributes: Optional[Dict[str, Any]] = None

@dataclass(kw_only=True)
class GovUKSelect(govuk_frontend_base.GovUKComponent):
    """GovUK Select

    See: https://design-system.service.gov.uk/components/select/
    """

    id: str
    name: str
    items: List[SelectItems]
    value: Optional[str] = None
    disabled: Optional[bool] = None
    describedBy: Optional[str] = None
    label: Optional[Dict[str, Any]] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None

    _jinja2_template = "govuk_frontend_jinja/components/select/macro.html"
    _macro_name = "govukSelect"

