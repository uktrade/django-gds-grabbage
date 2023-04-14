from dataclasses import dataclass
from typing import Any, Optional

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
class CharacterCountCountmessage:
    classes: Optional[str] = None


@dataclass(kw_only=True)
class GovUKCharacterCount(govuk_frontend_base.GovUKComponent):
    """GovUK Character Count

    See: https://design-system.service.gov.uk/components/character-count/
    """

    id: str
    name: str
    rows: Optional[str] = None
    value: Optional[str] = None
    maxlength: str
    maxwords: str
    threshold: Optional[str] = None
    label: govuk_frontend_label.GovUKLabel
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    spellcheck: Optional[bool] = None
    countMessage: Optional[CharacterCountCountmessage] = None
    textareaDescriptionText: Optional[str] = None
    charactersUnderLimitText: Optional[Any] = None
    charactersAtLimitText: Optional[str] = None
    charactersOverLimitText: Optional[Any] = None
    wordsUnderLimitText: Optional[Any] = None
    wordsAtLimitText: Optional[str] = None
    wordsOverLimitText: Optional[Any] = None

    _jinja2_template = "govuk_frontend_jinja/components/character-count/macro.html"
    _macro_name = "govukCharacterCount"


COMPONENT = GovUKCharacterCount
