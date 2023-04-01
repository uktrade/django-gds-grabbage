from typing import Any, Dict

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
