from dataclasses import dataclass
from typing import Any, Dict, Optional, TypedDict

from django.forms.utils import RenderableMixin
from django.utils.safestring import mark_safe
from jinja2 import (ChoiceLoader, Environment, PackageLoader, PrefixLoader,
                    select_autoescape)


class GovUKComponent(RenderableMixin):
    jinja2_template: str
    macro_name: str

    def get_data(self) -> Dict[str, Any]:
        return {}

    def build_jinja_template(self):
        return "".join(
            [
                "{%- from '", self.jinja2_template, "' import ", self.macro_name, " -%}",
                "{{ ", self.macro_name, "(data) }}",
            ]
        )

    def render(self, template_name=None, context=None, renderer=None):
        jinja_loader = ChoiceLoader(
            [
                PrefixLoader(
                    {
                        "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")
                    }
                )
            ]
        )
        env = Environment(
            loader=jinja_loader,
            autoescape=select_autoescape(),
        )
        template = env.from_string(self.build_jinja_template())
        return mark_safe(template.render(data=self.get_data()))

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
    from dbt_govuk_django.django.core.govuk_frontend.error_message import \
        GovUKErrorMessage

    name: Optional[str] = None
    fieldset: Fieldset
    hint: HintText
    error_message: GovUKErrorMessage

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            name=self.name,
            fieldset=self.fieldset,
            hint=self.hint,
            errorMessage=self.error_message,
        )
        return data
