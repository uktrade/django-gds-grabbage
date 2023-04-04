from dataclasses import dataclass, field
from typing import Optional

from django_gds_grabbage.django.core.govuk_frontend.base import (
    Attributes,
    FormGroup,
    GovUKComponent,
)


@dataclass(kw_only=True)
class CharacterCountCountMessage:
    classes: str


@dataclass(kw_only=True)
class CharacterCountLabel:
    text: Optional[str] = None
    html: Optional[str] = None
    _for: Optional[str] = field(
        metadata={"name": "for"},
        default=None,
    )
    isPageHeading: Optional[bool] = None
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None


@dataclass(kw_only=True)
class CharacterCountHint:
    id: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None


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
    formGroup: Optional[FormGroup] = None
    countMessage: Optional[CharacterCountCountMessage] = None

    _jinja2_template = "govuk_frontend_jinja/components/character-count/macro.html"
    _macro_name = "govukCharacterCount"
