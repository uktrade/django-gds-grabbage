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
class SummaryListCardActionsItems:
    href: str
    text: Optional[str] = None
    html: Optional[str] = None
    visuallyHiddenText: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class SummaryListCardActions:
    items: Optional[List[SummaryListCardActionsItems]] = None
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListCardTitle:
    text: Optional[str] = None
    html: Optional[str] = None
    headingLevel: Optional[int] = None
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListCard:
    title: Optional[SummaryListCardTitle] = None
    actions: Optional[SummaryListCardActions] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKSummaryList(govuk_frontend_base.GovUKComponent):
    """GovUK Summary List

    See: https://design-system.service.gov.uk/components/summary-list/
    """

    rows: govuk_frontend_base.SummaryListRows
    card: Optional[SummaryListCard] = None

    _jinja2_template = "govuk_frontend_jinja/components/summary-list/macro.html"
    _macro_name = "govukSummaryList"


COMPONENT = GovUKSummaryList
