from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import Attributes, GovUKComponent


@dataclass(kw_only=True)
class AccordionItemText:
    text: str


@dataclass(kw_only=True)
class AccordionItemHtml:
    html: str


@dataclass(kw_only=True)
class AccordionItem:
    heading: AccordionItemText
    summary: Optional[AccordionItemText]
    content: AccordionItemHtml


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
