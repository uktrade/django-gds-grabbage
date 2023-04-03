from dataclasses import dataclass
from typing import Any, Dict, Optional, TypedDict

from dbt_govuk_django.django.core.govuk_frontend.base import Attributes, GovUKComponent


class CharacterCountFormGroup(TypedDict):
    classes: str


class CharacterCountCountMessage(TypedDict):
    classes: str


class CharacterCountFormGroup(TypedDict):
    classes: str


class CharacterCountLabel(TypedDict):
    text: str
    html: str
    # for: str
    classes: str
    isPageHeading: bool


class CharacterCountHint(TypedDict):
    id: Optional[str]
    text: str
    html: str
    classes: str
    attributes: Attributes


@dataclass(kw_only=True)
class GovUKCharacterCount(GovUKComponent):
    """GovUK Character Count

    See: https://design-system.service.gov.uk/components/character-count/
    """

    id: str
    name: str
    rows: Optional[str] = None
    value: Optional[str] = None
    maxlength: Optional[str] = None
    maxwords: Optional[str] = None
    threshold: Optional[str] = None
    label: Optional[CharacterCountLabel] = None
    hint: Optional[CharacterCountHint] = None
    spellcheck: bool = False
    formGroup: Optional[CharacterCountFormGroup] = None
    countMessage: Optional[CharacterCountCountMessage] = None

    _jinja2_template = "govuk_frontend_jinja/components/character-count/macro.html"
    _macro_name = "govukCharacterCount"
