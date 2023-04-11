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
class GovUKErrorMessage(govuk_frontend_base.GovUKComponent):
    """GovUK Error Message

    See: https://design-system.service.gov.uk/components/error-message/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    id: Optional[str] = None
    visuallyHiddenText: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/error-message/macro.html"
    _macro_name = "govukErrorMessage"


COMPONENT = GovUKErrorMessage
