from dataclasses import dataclass
from typing import Any, Dict, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


class CharacterCountLabel(TypedDict):
    text: str
    classes: str
    isPageHeading: bool

class CharacterCountHint(TypedDict):
    text: str

@dataclass
class GovUKCharacterCount(GovUKComponent):
    name: str
    id: str
    maxlength: int
    label: CharacterCountLabel
    hint: CharacterCountHint

    jinja2_template = "govuk_frontend_jinja/components/character-count/macro.html"
    macro_name = "govukCharacterCount"

    def get_data(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "id": self.id,
            "maxlength": self.maxlength,
            "label": self.label,
            "hint": self.hint,
        }
