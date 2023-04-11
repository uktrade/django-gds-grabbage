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
class TableHead:
    text: Optional[str] = None
    html: Optional[str] = None
    format: Optional[str] = None
    classes: Optional[str] = None
    colspan: Optional[int] = None
    rowspan: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class TableRows:
    text: Optional[str] = None
    html: Optional[str] = None
    format: Optional[str] = None
    classes: Optional[str] = None
    colspan: Optional[int] = None
    rowspan: Optional[int] = None
    attributes: Optional[Dict[str, Any]] = None


@dataclass(kw_only=True)
class GovUKTable(govuk_frontend_base.GovUKComponent):
    """GovUK Table

    See: https://design-system.service.gov.uk/components/table/
    """

    rows: List[TableRows]
    head: Optional[List[TableHead]] = None
    caption: Optional[str] = None
    captionClasses: Optional[str] = None
    firstCellIsHeader: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/table/macro.html"
    _macro_name = "govukTable"


COMPONENT = GovUKTable
