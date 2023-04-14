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
class FooterCopyright:
    text: Optional[str] = None
    html: Optional[str] = None


@dataclass(kw_only=True)
class FooterContentlicence:
    text: Optional[str] = None
    html: Optional[str] = None


@dataclass(kw_only=True)
class FooterNavigationItems:
    text: str
    href: str
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class FooterNavigation:
    title: str
    columns: Optional[int] = None
    width: Optional[str] = None
    items: Optional[List[FooterNavigationItems]] = None


@dataclass(kw_only=True)
class FooterMetaItems:
    text: str
    href: str
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class FooterMeta:
    visuallyHiddenTitle: Optional[str] = None
    html: Optional[str] = None
    text: Optional[str] = None
    items: Optional[List[FooterMetaItems]] = None


@dataclass(kw_only=True)
class GovUKFooter(govuk_frontend_base.GovUKComponent):
    """GovUK Footer

    See: https://design-system.service.gov.uk/components/footer/
    """

    meta: Optional[FooterMeta] = None
    navigation: Optional[List[FooterNavigation]] = None
    contentLicence: Optional[FooterContentlicence] = None
    copyright: Optional[FooterCopyright] = None
    containerClasses: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/footer/macro.html"
    _macro_name = "govukFooter"


COMPONENT = GovUKFooter
