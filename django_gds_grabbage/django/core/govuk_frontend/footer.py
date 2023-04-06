
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from django_gds_grabbage.django.core.govuk_frontend import base as govuk_frontend_base
from django_gds_grabbage.django.core.govuk_frontend import error_message as govuk_frontend_error_message
from django_gds_grabbage.django.core.govuk_frontend import hint as govuk_frontend_hint
from django_gds_grabbage.django.core.govuk_frontend import fieldset as govuk_frontend_fieldset


@dataclass(kw_only=True)
class FooterNavigationItems:
    text: str
    href: str
    attributes: Optional[Dict[str, Any]] = None

@dataclass(kw_only=True)
class FooterNavigation:
    title: str
    columns: Optional[int] = None
    width: Optional[str] = None
    items: Optional[List[FooterNavigationItems]] = None

@dataclass(kw_only=True)
class GovUKFooter(govuk_frontend_base.GovUKComponent):
    """GovUK Footer

    See: https://design-system.service.gov.uk/components/footer/
    """

    meta: Optional[Dict[str, Any]] = None
    navigation: Optional[List[FooterNavigation]] = None
    contentLicence: Optional[Dict[str, Any]] = None
    copyright: Optional[Dict[str, Any]] = None
    containerClasses: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/footer/macro.html"
    _macro_name = "govukFooter"

