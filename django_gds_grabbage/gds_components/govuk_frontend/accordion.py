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


@dataclass(kw_only=True)
class GovUKAccordion(govuk_frontend_base.GovUKComponent):
    """GovUK Accordion

    See: https://design-system.service.gov.uk/components/accordion/
    """

    id: str
    headingLevel: Optional[int] = None
    rememberExpanded: Optional[bool] = None
    hideAllSectionsText: Optional[str] = None
    hideSectionText: Optional[str] = None
    hideSectionAriaLabelText: Optional[str] = None
    showAllSectionsText: Optional[str] = None
    showSectionText: Optional[str] = None
    showSectionAriaLabelText: Optional[str] = None
    items: List[govuk_frontend_base.AccordionItem]

    _jinja2_template = "govuk_frontend_jinja/components/accordion/macro.html"
    _macro_name = "govukAccordion"


COMPONENT = GovUKAccordion
