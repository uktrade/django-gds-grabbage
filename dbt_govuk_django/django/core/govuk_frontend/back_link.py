from dataclasses import dataclass
from typing import Any, Dict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass
class GovUKBackLink(GovUKComponent):
    text: str
    href: str

    jinja2_template = "govuk_frontend_jinja/components/back-link/macro.html"
    macro_name = "govukBackLink"

    def get_data(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "href": self.href,
        }
