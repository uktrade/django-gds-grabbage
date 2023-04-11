from dataclasses import dataclass, field
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
class GovUKLabel(govuk_frontend_base.GovUKComponent):
    """GovUK Label

    See: https://design-system.service.gov.uk/components/label/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    _for: Optional[str] = field(default=None, metadata={"name": "for"})
    isPageHeading: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/label/macro.html"
    _macro_name = "govukLabel"


COMPONENT = GovUKLabel
