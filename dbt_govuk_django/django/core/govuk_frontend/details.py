from dataclasses import dataclass
from typing import Any, Dict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUKDetails(GovUKComponent):
    """GovUK Details

    See: https://design-system.service.gov.uk/components/details/
    """

    _jinja2_template = "govuk_frontend_jinja/components/details/macro.html"
    _macro_name = "govukDetails"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(...)
        return data
