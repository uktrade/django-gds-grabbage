from dataclasses import dataclass
from typing import Any, Dict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass
class GovUKButton(GovUKComponent):
    text: str
    classes: str = ""
    disabled: bool = False
    preventDoubleClick: bool = True

    jinja2_template = "govuk_frontend_jinja/components/button/macro.html"
    macro_name = "govukButton"

    def get_data(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "classes": self.classes,
            "disabled": self.disabled,
            "preventDoubleClick": self.preventDoubleClick,
        }
