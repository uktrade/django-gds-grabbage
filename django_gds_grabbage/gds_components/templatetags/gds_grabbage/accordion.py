from typing import List

from django import template
from django.template.base import Node, Parser, Token, token_kwargs

from django_gds_grabbage.gds_components.govuk_frontend.accordion import GovUKAccordion
from django_gds_grabbage.gds_components.govuk_frontend.base import (
    AccordionItem,
    TextAndHtml,
)
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    DataclassNode,
    GovUKComponentNode,
)

register = template.Library()


class AccordionNode(GovUKComponentNode):
    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        accordion_items: List[AccordionItem] = []
        for node in self.get_nodes_by_type(AccordionItemNode):
            accordion_node: AccordionItemNode = node
            accordion_items.append(accordion_node.resolve_dataclass(context))

        component_kwargs["items"] = accordion_items
        return component_kwargs


class AccordionItemNode(DataclassNode):
    dataclass_cls = AccordionItem

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["heading"] = TextAndHtml(text=component_kwargs["heading"])
        component_kwargs["summary"] = TextAndHtml(text=component_kwargs["summary"])
        component_kwargs["content"] = TextAndHtml(html=self.nodelist.render(context))

        return component_kwargs


@register.tag
def gds_accordion(parser: Parser, token: Token):
    """GDS accordion template tag.

    Args:
        parser (Parser)
        token (Token)

    Usage:
        template.html:
        ```django
        {% load gds_grabbage %}
        {% gds_accordion "accordion-1" %}
            {% gds_accordion_item "Heading 1" "Summary 1" %}
                <strong>Content1</strong>
            {% end_gds_accordion_item %}
            {% gds_accordion_item "Heading 2" "Summary 2" %}
                <strong>Content2</strong>
            {% end_gds_accordion_item %}
        {% end_gds_accordion %}
        ```
    """

    nodelist = parser.parse(("end_gds_accordion",))
    parser.delete_first_token()

    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    node = AccordionNode(
        extra_context=extra_context,
        component_name="accordion",
        nodelist=nodelist,
    )

    return node


@register.tag
def gds_accordion_item(parser: Parser, token: Token):
    """GDS accordion item template tag."""
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    nodelist = parser.parse(("end_gds_accordion_item",))
    parser.delete_first_token()

    node = AccordionItemNode(
        extra_context=extra_context,
        nodelist=nodelist,
    )
    return node
