
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from django_gds_grabbage.django.core.govuk_frontend import base as govuk_frontend_base
from django_gds_grabbage.django.core.govuk_frontend import error_message as govuk_frontend_error_message
from django_gds_grabbage.django.core.govuk_frontend import hint as govuk_frontend_hint
from django_gds_grabbage.django.core.govuk_frontend import fieldset as govuk_frontend_fieldset


@dataclass(kw_only=True)
class GovUKInput(govuk_frontend_base.GovUKComponent):
    """GovUK Input

    See: https://design-system.service.gov.uk/components/input/
    """

    id: str
    name: str
    type: Optional[str] = None
    inputmode: Optional[str] = None
    value: Optional[str] = None
    disabled: Optional[bool] = None
    describedBy: Optional[str] = None
    label: Dict[str, Any]
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    prefix: Optional[Dict[str, Any]] = None
    suffix: Optional[Dict[str, Any]] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    autocomplete: Optional[str] = None
    pattern: Optional[str] = None
    spellcheck: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/input/macro.html"
    _macro_name = "govukInput"

