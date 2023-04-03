from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


class AccordionItemText(TypedDict):
    text: str

class AccordionItemHtml(TypedDict):
    html: str

class AccordionItem(TypedDict):
    heading: AccordionItemText
    summary: Optional[AccordionItemText]
    content: AccordionItemHtml

@dataclass(kw_only=True)
class GovUKAccordion(GovUKComponent):
    """GovUK Accordion

    See: https://design-system.service.gov.uk/components/accordion/
    """

    id: str
    items: List[AccordionItem]

    jinja2_template = "govuk_frontend_jinja/components/accordion/macro.html"
    macro_name = "govukAccordion"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            id=self.id,
            items=self.items,
        )
        return data
