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
class BreadcrumbsItems:
    text: Optional[str] = None
    html: Optional[str] = None
    href: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKBreadcrumbs(govuk_frontend_base.GovUKComponent):
    """GovUK Breadcrumbs

    See: https://design-system.service.gov.uk/components/breadcrumbs/
    """

    items: List[BreadcrumbsItems]
    collapseOnMobile: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/breadcrumbs/macro.html"
    _macro_name = "govukBreadcrumbs"


COMPONENT = GovUKBreadcrumbs
