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
class GovUKSummaryList(govuk_frontend_base.GovUKComponent):
    """GovUK Summary List

    See: https://design-system.service.gov.uk/components/summary-list/
    """

    rows: govuk_frontend_base.SummaryListRows
    card: Optional[Dict[str, Any]] = None

    _jinja2_template = "govuk_frontend_jinja/components/summary-list/macro.html"
    _macro_name = "govukSummaryList"


COMPONENT = GovUKSummaryList