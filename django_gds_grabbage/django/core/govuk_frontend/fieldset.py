
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from django_gds_grabbage.django.core.govuk_frontend import base as govuk_frontend_base
from django_gds_grabbage.django.core.govuk_frontend import error_message as govuk_frontend_error_message
from django_gds_grabbage.django.core.govuk_frontend import hint as govuk_frontend_hint
from django_gds_grabbage.django.core.govuk_frontend import fieldset as govuk_frontend_fieldset


@dataclass(kw_only=True)
class GovUKFieldset(govuk_frontend_base.GovUKComponent):
    """GovUK Fieldset

    See: https://design-system.service.gov.uk/components/fieldset/
    """

    describedBy: Optional[str] = None
    legend: Optional[govuk_frontend_base.FieldsetLegend] = None
    role: Optional[str] = None
    html: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/fieldset/macro.html"
    _macro_name = "govukFieldset"

