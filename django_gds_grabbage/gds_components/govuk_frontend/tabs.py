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
class TabsItems:
    id: str
    label: govuk_frontend_label.GovUKLabel
    attributes: Optional[govuk_frontend_base.Attributes] = None
    panel: govuk_frontend_base.TextAndHtml


@dataclass(kw_only=True)
class GovUKTabs(govuk_frontend_base.GovUKComponent):
    """GovUK Tabs

    See: https://design-system.service.gov.uk/components/tabs/
    """

    id: Optional[str] = None
    idPrefix: Optional[str] = None
    title: Optional[str] = None
    items: List[TabsItems]

    _jinja2_template = "govuk_frontend_jinja/components/tabs/macro.html"
    _macro_name = "govukTabs"


COMPONENT = GovUKTabs
