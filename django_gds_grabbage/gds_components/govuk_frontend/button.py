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
class GovUKButton(govuk_frontend_base.GovUKComponent):
    """GovUK Button

    See: https://design-system.service.gov.uk/components/button/
    """

    element: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    disabled: Optional[bool] = None
    href: Optional[str] = None
    preventDoubleClick: Optional[bool] = None
    isStartButton: Optional[bool] = None
    id: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/button/macro.html"
    _macro_name = "govukButton"


COMPONENT = GovUKButton
