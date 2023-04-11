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
class ErrorSummaryErrorlist:
    href: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class GovUKErrorSummary(govuk_frontend_base.GovUKComponent):
    """GovUK Error Summary

    See: https://design-system.service.gov.uk/components/error-summary/
    """

    titleText: str
    titleHtml: str
    descriptionText: Optional[str] = None
    descriptionHtml: Optional[str] = None
    errorList: List[ErrorSummaryErrorlist]
    disableAutoFocus: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/error-summary/macro.html"
    _macro_name = "govukErrorSummary"


COMPONENT = GovUKErrorSummary
