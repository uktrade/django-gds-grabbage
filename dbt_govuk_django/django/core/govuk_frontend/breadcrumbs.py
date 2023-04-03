from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import (Attributes,
                                                              GovUKComponent)


class BreadcrumbItem(TypedDict):
    text: str
    html: str
    href: str
    attributes: Attributes


@dataclass(kw_only=True)
class GovUKBreadcrumbs(GovUKComponent):
    """GovUK Breadcrumbs

    See: https://design-system.service.gov.uk/components/breadcrumbs/
    """

    items: List[BreadcrumbItem]
    collapseOnMobile: bool = False

    _jinja2_template = "govuk_frontend_jinja/components/breadcrumbs/macro.html"
    _macro_name = "govukBreadcrumbs"
