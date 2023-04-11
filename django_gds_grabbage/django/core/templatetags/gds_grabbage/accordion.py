from typing import List

from django import template
from django.template.base import Node, Parser, Token

from django_gds_grabbage.django.core.govuk_frontend.accordion import GovUKAccordion
from django_gds_grabbage.django.core.govuk_frontend.base import AccordionItem

register = template.Library()


class AccordionNode(Node):
    id: str

    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.accordion_items: List[AccordionItem] = []
        for node in nodelist:
            if isinstance(node, AccordionItemNode):
                accordion_item: AccordionItem = {
                    "heading": {"text": node.heading},
                    "summary": {"text": node.summary},
                    "content": {"html": node.html},
                }
                self.accordion_items.append(accordion_item)

    def render(self, context):
        return GovUKAccordion(
            id=self.id,
            items=self.accordion_items,
        ).render()


class AccordionItemNode(Node):
    heading: str
    summary: str
    html: str

    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.html = nodelist.render({})

    def render(self, context):
        return ""


@register.tag
def gds_accordion(parser: Parser, token: Token):
    """GDS accordion template tag.

    Args:
        parser (Parser)
        token (Token)

    Usage:
        template.html:
        ```django-html
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
    node = AccordionNode(nodelist)

    contents = token.split_contents()
    node.id = contents[1].replace('"', "").replace("'", "")
    return node


@register.tag
def gds_accordion_item(parser: Parser, token: Token):
    nodelist = parser.parse(("end_gds_accordion_item",))
    parser.delete_first_token()
    node = AccordionItemNode(nodelist)

    contents = token.split_contents()
    node.heading = contents[1].replace('"', "").replace("'", "")
    node.summary = contents[2].replace('"', "").replace("'", "")
    return node
