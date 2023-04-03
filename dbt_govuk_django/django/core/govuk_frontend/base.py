from dataclasses import dataclass
from typing import Any, Dict, Optional, TypedDict

from django.forms.utils import RenderableMixin
from django.utils.safestring import mark_safe
from jinja2 import (
    ChoiceLoader,
    Environment,
    PackageLoader,
    PrefixLoader,
    select_autoescape,
)


class Attributes(TypedDict):
    pass


class GovUKComponent(RenderableMixin):
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None

    _jinja2_template: str
    _macro_name: str

    def build_jinja_template(self):
        return "".join(
            [
                "{%- from '",
                self._jinja2_template,
                "' import ",
                self._macro_name,
                " -%}",
                "{{ ",
                self._macro_name,
                "(data) }}",
            ]
        )

    def render(self, template_name=None, context=None, renderer=None):
        jinja_loader = ChoiceLoader(
            [
                PrefixLoader(
                    {"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}
                )
            ]
        )
        env = Environment(
            loader=jinja_loader,
            autoescape=select_autoescape(),
        )
        template = env.from_string(self.build_jinja_template())
        return mark_safe(template.render(data=self.__dict__))
        # return mark_safe(template.render(data=self.get_data()))

    __str__ = render
    __html__ = render


class FieldsetLegend(TypedDict):
    text: str
    isPageHeading: bool
    classes: str


class Fieldset(TypedDict):
    legend: FieldsetLegend


class HintText(TypedDict):
    text: str


@dataclass(kw_only=True)
class GovUKFieldComponent(GovUKComponent):
    from dbt_govuk_django.django.core.govuk_frontend.error_message import (
        GovUKErrorMessage,
    )

    name: Optional[str] = None
    fieldset: Fieldset
    hint: HintText
    errorMessage: GovUKErrorMessage
