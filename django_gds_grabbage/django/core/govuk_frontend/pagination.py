from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from django_gds_grabbage.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class PaginationPrevNextLink:
    href: str
    labelText: Optional[str]


@dataclass(kw_only=True)
class PaginationItem:
    number: int
    current: bool
    href: str


@dataclass(kw_only=True)
class PaginationEllipsis:
    ellipsis: bool


@dataclass(kw_only=True)
class GovUKPagination(GovUKComponent):
    """GovUK Pagination

    See: https://design-system.service.gov.uk/components/pagination/
    """

    previous: Optional[PaginationPrevNextLink] = None
    next: Optional[PaginationPrevNextLink] = None
    items: List[PaginationItem | PaginationEllipsis]

    _jinja2_template = "govuk_frontend_jinja/components/pagination/macro.html"
    _macro_name = "govukPagination"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            previous=self.previous,
            next=self.next,
            items=self.items,
        )
        return data
