from typing import Dict

from django import template
from django.forms import BoundField
from django.template.base import Node, Parser, Token, token_kwargs

from django_gds_grabbage.gds_components.govuk_frontend.base import CheckboxesConditional
from django_gds_grabbage.gds_components.govuk_frontend.checkboxes import (
    CheckboxesItems,
    GovUKCheckboxes,
)
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    DataclassNode,
    GovUKComponentNode,
)

register = template.Library()


class FieldNode(GovUKComponentNode):
    def resolve(self, context):
        super().resolve(context)
        self.bound_field: BoundField = self.resolved_kwargs["field"]
        self.resolved_kwargs["name"] = self.bound_field.name
        self.resolved_kwargs["fieldset"] = {
            "legend": {
                "text": "How would you like to be contacted?",
                "isPageHeading": True,
                "classes": "govuk-fieldset__legend--l",
            }
        }

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)
        component_kwargs.pop("field")
        return component_kwargs


class CheckboxesNode(FieldNode):
    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        self.checkbox_conditional_items: Dict[str, CheckboxesConditional] = {}
        for node in self.get_nodes_by_type(CheckboxConditionalNode):
            checkbox_conditional_item = node.resolve_dataclass(context)
            conditional_value = node.resolved_kwargs["value"]
            self.checkbox_conditional_items[
                conditional_value
            ] = checkbox_conditional_item

        component_kwargs["items"] = []

        if self.bound_field.field.choices:
            for choice in self.bound_field.field.choices:
                item = CheckboxesItems(
                    value=choice[0],
                    text=choice[1],
                )
                if item.value in self.checkbox_conditional_items:
                    item.conditional = self.checkbox_conditional_items[item.value]
                component_kwargs["items"].append(item)

        return component_kwargs


class CheckboxConditionalNode(DataclassNode):
    dataclass_cls = CheckboxesConditional

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["html"] = self.resolved_kwargs["content"]

        del component_kwargs["value"]
        del component_kwargs["content"]

        return component_kwargs


@register.tag
def gds_checkboxes(parser: Parser, token: Token):
    """GDS checkboxes template tag.

    Args:
        parser (Parser)
        token (Token)

    Usage:
        template.html:
        ```django
        {% load gds_grabbage %}
        {% gds_checkboxes form.field %}
            {% gds_checkbox_conditional "value" %}
                <div>Conditional content</div>
            {% end_gds_checkbox_conditional %}
        {% end_gds_checkboxes %}
        ```
    """

    nodelist = parser.parse(("end_gds_checkboxes",))
    parser.delete_first_token()

    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    return CheckboxesNode(
        extra_context=extra_context,
        component_name="checkboxes",
        nodelist=nodelist,
    )


@register.tag
def gds_checkbox_conditional(parser: Parser, token: Token):
    """GDS checkbox conditional template tag."""
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    return CheckboxConditionalNode(
        extra_context=extra_context,
    )
