from dataclasses import dataclass
from typing import Any, Dict, List, Optional

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
class HeaderNavigation:
    text: Optional[str] = None
    html: Optional[str] = None
    href: Optional[str] = None
    active: Optional[bool] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class GovUKHeader(govuk_frontend_base.GovUKComponent):
    """GovUK Header

    See: https://design-system.service.gov.uk/components/header/
    """

    homepageUrl: Optional[str] = None
    assetsPath: Optional[str] = None
    productName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceUrl: Optional[str] = None
    navigation: Optional[List[HeaderNavigation]] = None
    navigationClasses: Optional[str] = None
    navigationLabel: Optional[str] = None
    menuButtonLabel: Optional[str] = None
    menuButtonText: Optional[str] = None
    containerClasses: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/header/macro.html"
    _macro_name = "govukHeader"


COMPONENT = GovUKHeader