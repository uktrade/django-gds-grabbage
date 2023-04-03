from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


class PaginationPrevNextLink(TypedDict):
    href: str
    labelText: Optional[str]


class PaginationItem(TypedDict):
    number: int
    current: bool
    href: str

class PaginationEllipsis(TypedDict):
    ellipsis: bool

@dataclass(kw_only=True)
class GovUKPagination(GovUKComponent):
    previous: Optional[PaginationPrevNextLink] = None
    next: Optional[PaginationPrevNextLink] = None
    items: List[PaginationItem | PaginationEllipsis]

    jinja2_template = "govuk_frontend_jinja/components/pagination/macro.html"
    macro_name = "govukPagination"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            previous=self.previous,
            next=self.next,
            items=self.items,
        )
        return data
