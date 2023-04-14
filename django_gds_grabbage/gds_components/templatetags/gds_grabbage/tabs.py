from typing import List

from django import template
from django.template.base import Parser, Token, token_kwargs

from django_gds_grabbage.gds_components.govuk_frontend.base import TextAndHtml
from django_gds_grabbage.gds_components.govuk_frontend.tabs import TabsItems
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    DataclassNode,
    GovUKComponentNode,
)

register = template.Library()


class TabsNode(GovUKComponentNode):
    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        tabs: List[TabsItems] = []
        for node in self.get_nodes_by_type(TabsTabNode):
            tabs.append(node.resolve_dataclass(context))

        component_kwargs["items"] = tabs
        return component_kwargs


class TabsTabNode(DataclassNode):
    dataclass_cls = TabsItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["panel"] = TextAndHtml(html=self.nodelist.render(context))

        return component_kwargs


@register.tag
def gds_tabs(parser: Parser, token: Token):
    """GDS tabs template tag.

    Usage:
        template.html:
        ```django
        {% load gds_grabbage %}
        ...
        {% gds_tabs id="tabs-1" title="Tab title" %}
            {% gds_tabs_tab id="tab-1" label="Tab 1" %}
                <strong>Test 1</strong>
            {% end_gds_tabs_tab %}
            {% gds_tabs_tab id="tab-2" label="Tab 2" %}
                <strong>Test 2</strong>
            {% end_gds_tabs_tab %}
            {% gds_tabs_tab id="tab-3" label="Tab 3" %}
                <strong>Test 3</strong>
            {% end_gds_tabs_tab %}
        {% end_gds_tabs %}
        ```
    """

    nodelist = parser.parse(("end_gds_tabs",))
    parser.delete_first_token()

    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    node = TabsNode(
        extra_context=extra_context,
        component_name="tabs",
        nodelist=nodelist,
    )

    return node


@register.tag
def gds_tabs_tab(parser: Parser, token: Token):
    """GDS tabs tab template tag."""
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    nodelist = parser.parse(("end_gds_tabs_tab",))
    parser.delete_first_token()

    node = TabsTabNode(
        extra_context=extra_context,
        nodelist=nodelist,
    )
    return node
