
from dataclasses import dataclass
from typing import Any, Dict, Optional

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUKErrorMessage(GovUKComponent):
    """GovUK Error Message

    See: https://design-system.service.gov.uk/components/error-message/
    """

    id: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    classes: str = ""
    visually_hidden_Text: str = ""

    jinja2_template = "govuk_frontend_jinja/components/error-message/macro.html"
    macro_name = "govukErrorMessage"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            id=self.id,
            text=self.text,
            html=self.html,
            classes=self.classes,
            visuallyHiddenText=self.visually_hidden_Text,
        )
        return data

