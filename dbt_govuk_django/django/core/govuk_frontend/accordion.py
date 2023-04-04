from dataclasses import dataclass
from typing import List, Optional

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent, TextAndHtml


@dataclass(kw_only=True)
class AccordionItem:
    heading: Optional[TextAndHtml] = None
    summary: Optional[TextAndHtml] = None
    content: Optional[TextAndHtml] = None


@dataclass(kw_only=True)
class GovUKAccordion(GovUKComponent):
    """GovUK Accordion

    See: https://design-system.service.gov.uk/components/accordion/
    """

    id: str
    headingLevel: int = 2
    items: List[AccordionItem]

    _jinja2_template = "govuk_frontend_jinja/components/accordion/macro.html"
    _macro_name = "govukAccordion"
