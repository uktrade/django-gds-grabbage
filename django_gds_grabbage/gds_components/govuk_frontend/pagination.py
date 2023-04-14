from dataclasses import dataclass
from typing import List, Optional

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
class PaginationNext:
    text: Optional[str] = None
    labelText: Optional[str] = None
    href: str
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class PaginationPrevious:
    text: Optional[str] = None
    labelText: Optional[str] = None
    href: str
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class PaginationItems:
    number: Optional[str] = None
    visuallyHiddenText: Optional[str] = None
    href: str
    current: Optional[bool] = None
    ellipsis: Optional[bool] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKPagination(govuk_frontend_base.GovUKComponent):
    """GovUK Pagination

    See: https://design-system.service.gov.uk/components/pagination/
    """

    items: Optional[List[PaginationItems]] = None
    previous: Optional[PaginationPrevious] = None
    next: Optional[PaginationNext] = None
    landmarkLabel: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/pagination/macro.html"
    _macro_name = "govukPagination"


COMPONENT = GovUKPagination
