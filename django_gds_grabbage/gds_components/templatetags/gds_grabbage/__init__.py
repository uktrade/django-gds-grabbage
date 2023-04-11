import importlib
import pathlib
from dataclasses import dataclass
from typing import Dict, Optional, Type

from django import template
from django.forms import BoundField
from django.template.base import (
    FilterExpression,
    Node,
    NodeList,
    Parser,
    Token,
    token_kwargs,
)

from django_gds_grabbage.gds_components.govuk_frontend.base import GovUKComponent

register = template.Library()


class GovUKComponentNode(Node):
    def __init__(
        self,
        extra_context: Dict[str, FilterExpression],
        component_name: Optional[str] = None,
        nodelist: Optional[NodeList] = None,
    ):
        self.nodelist = nodelist or NodeList()
        self.component_name = component_name
        if self.component_name:
            self.component_class = self.get_component_class()
        self.extra_context = extra_context
        self.resolved_kwargs = {}

    def get_component_class(self):
        underscored_component_name = self.component_name.replace("-", "_")
        module_name = f"django_gds_grabbage.gds_components.govuk_frontend.{underscored_component_name}"
        module = importlib.import_module(module_name)
        return getattr(module, "COMPONENT")

    def resolve(self, context):
        if not self.resolved_kwargs:
            self.resolved_kwargs = {
                key: val.resolve(context) for key, val in self.extra_context.items()
            }

    def build_component_kwargs(self, context):
        self.resolve(context)
        return self.resolved_kwargs.copy()

    def render(self, context):
        rendered_output = super().render(context)
        if self.component_name:
            return self.component_class(**self.build_component_kwargs(context)).render()
        return rendered_output


class DataclassNode(GovUKComponentNode):
    dataclass_cls: Type[dataclass]

    def resolve_dataclass(self, context) -> dataclass:
        self.resolve(context)
        return self.dataclass_cls(**self.build_component_kwargs(context))


FIELD_COMPONENTS = [
    "character-count",
    "checkboxes",
    "date-input",
    "fieldset",
    "file-upload",
    "input",
    "radios",
    "select",
    "textarea",
]
COMPLEX_COMPONENTS = [
    "breadcrumbs",
    "cookie-banner",
    "error-summary",
    "footer",
    "header",
    "pagination",
    "phase-banner",
    "summary-list",
    "table",
    "tabs",
]


@register.tag
def gds_component(parser: Parser, token: Token):
    bits = token.split_contents()
    component_name = bits[1].replace("'", "").replace('"', "")

    if component_name in FIELD_COMPONENTS:
        raise Exception(
            f"Use the gds_field_component tag for {component_name} components."
        )
    if component_name in COMPLEX_COMPONENTS:
        raise Exception(
            f"{component_name} is a complex component with it's own templatetag."
        )

    remaining_bits = bits[2:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    return GovUKComponentNode(
        nodelist=[],
        component_name=component_name,
        extra_context=extra_context,
    )


@register.simple_tag
def gds_field_component(field: BoundField, **kwargs):
    return "Not yet implemented"


class SetNode(Node):
    def __init__(self, nodelist: NodeList, asvar: str):
        self.nodelist = nodelist
        self.asvar = asvar

    def render(self, context):
        context[self.asvar] = self.nodelist.render(context)
        return ""


@register.tag
def set(parser: Parser, token: Token):
    nodelist = parser.parse(("endset",))
    parser.delete_first_token()

    bits = token.split_contents()
    node = SetNode(nodelist=nodelist, asvar=bits[1])

    return node


@register.simple_tag
def gds_component_template(jinja2_template: str, macro_name: str, **kwargs):
    """Fallback template tag for rendering a GovUK component.

    Args:
        jinja2_template (str): The path to the Jinja2 template.
        macro_name (str): The name of the macro to render.
        **kwargs: The keyword arguments to pass to the macro.

    Usage:
        {% gds_component_template jinja2_template="govuk_frontend_jinja/components/warning-text/macro.html" macro_name="govukWarningText" text="WARNING: something is wrong!" %}
    """

    component = GovUKComponent()
    component._jinja2_template = jinja2_template
    component._macro_name = macro_name
    return component.render(component_data={**kwargs})


# Loop over python files in this directory and update the register object
# with the tags and filters defined in each file.
for path in pathlib.Path(__file__).parent.iterdir():
    if path.suffix == ".py" and path.name != "__init__.py":
        module_name = path.stem
        module = importlib.import_module(f".{module_name}", __package__)
        register.tags.update(module.register.tags)
        register.filters.update(module.register.filters)
