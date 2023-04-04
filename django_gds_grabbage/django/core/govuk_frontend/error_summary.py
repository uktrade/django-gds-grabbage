from dataclasses import dataclass
from typing import List, Optional

from django_gds_grabbage.django.core.govuk_frontend.base import (
    Attributes,
    GovUKComponent,
)


@dataclass(kw_only=True)
class ErrorListItem:
    text: Optional[str] = None
    html: Optional[str] = None
    href: Optional[str] = None
    attributes: Optional[Attributes] = None


@dataclass(kw_only=True)
class GovUKErrorSummary(GovUKComponent):
    """GovUK Error Summary

    See: https://design-system.service.gov.uk/components/error-summary/
    """

    titleText: Optional[str] = None
    titleHtml: Optional[str] = None
    descriptionText: Optional[str] = None
    descriptionHtml: Optional[str] = None
    errorList: List[ErrorListItem]
    disableAutoFocus: bool = False

    _jinja2_template = "govuk_frontend_jinja/components/error-summary/macro.html"
    _macro_name = "govukErrorSummary"
