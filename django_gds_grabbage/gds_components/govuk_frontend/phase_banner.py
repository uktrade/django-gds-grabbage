from dataclasses import dataclass
from typing import Any, Dict, Optional

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
class GovUKPhaseBanner(govuk_frontend_base.GovUKComponent):
    """GovUK Phase Banner

    See: https://design-system.service.gov.uk/components/phase-banner/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    tag: Dict[str, Any]

    _jinja2_template = "govuk_frontend_jinja/components/phase-banner/macro.html"
    _macro_name = "govukPhaseBanner"


COMPONENT = GovUKPhaseBanner
