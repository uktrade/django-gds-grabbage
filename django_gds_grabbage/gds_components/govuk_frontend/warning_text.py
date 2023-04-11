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


@dataclass(kw_only=True)
class GovUKWarningText(govuk_frontend_base.GovUKComponent):
    """GovUK Warning Text

    See: https://design-system.service.gov.uk/components/warning-text/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    iconFallbackText: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/warning-text/macro.html"
    _macro_name = "govukWarningText"


COMPONENT = GovUKWarningText
