from dataclasses import dataclass
from typing import Any, Dict, List, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


class BreadcrumbItem(TypedDict):
    text: str
    href: str


@dataclass(kw_only=True)
class GovUKBreadcrumbs(GovUKComponent):
    """GovUK Breadcrumbs

    See: https://design-system.service.gov.uk/components/breadcrumbs/
    """

    items: List[BreadcrumbItem]

    jinja2_template = "govuk_frontend_jinja/components/breadcrumbs/macro.html"
    macro_name = "govukBreadcrumbs"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            items=self.items,
        )
        return data
