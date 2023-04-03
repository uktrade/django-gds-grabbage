from dataclasses import dataclass
from typing import Any, Dict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUKBackLink(GovUKComponent):
    """GovUK Back Link

    See: https://design-system.service.gov.uk/components/back-link/
    """

    text: str
    href: str

    jinja2_template = "govuk_frontend_jinja/components/back-link/macro.html"
    macro_name = "govukBackLink"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            text=self.text,
            href=self.href,
        )
        return data
