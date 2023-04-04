from dataclasses import dataclass
from typing import List, Optional

from django_gds_grabbage.django.core.govuk_frontend.base import (
    Attributes,
    GovUKComponent,
)


@dataclass(kw_only=True)
class BreadcrumbItem:
    text: Optional[str] = None
    html: Optional[str] = None
    href: Optional[str] = None
    attributes: Attributes = None


@dataclass(kw_only=True)
class GovUKBreadcrumbs(GovUKComponent):
    """GovUK Breadcrumbs

    See: https://design-system.service.gov.uk/components/breadcrumbs/
    """

    items: List[BreadcrumbItem]
    collapseOnMobile: bool = False

    _jinja2_template = "govuk_frontend_jinja/components/breadcrumbs/macro.html"
    _macro_name = "govukBreadcrumbs"
