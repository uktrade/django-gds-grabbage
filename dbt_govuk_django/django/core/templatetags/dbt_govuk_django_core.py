from typing import List, Optional

from django import template
from django.core.paginator import Page
from django.template.base import Node, Parser, Token

from dbt_govuk_django.django.core.govuk_frontend.accordion import (
    AccordionItem, GovUKAccordion)
from dbt_govuk_django.django.core.govuk_frontend.pagination import (
    GovUKPagination, PaginationEllipsis, PaginationItem,
    PaginationPrevNextLink)

register = template.Library()

@register.simple_tag
def gds_pagination(page_obj: Page):
    """GDS pagination template tag.

    Args:
        page_obj (Page):
            The Django Paginator Page object.

    Usage:
        This template tag is designed to be used with the Django pagination,
        below is an example of it being used with a ListView.

        *views.py:*
        ```python
        from django.views.generic import ListView
        from django.contrib.auth import get_user_model

        User = get_user_model()


        class UserListingView(ListView):
            template_name = "template.html"
            model = User
            paginate_by = 25
        ```

        *template.html:*
        ```django-html
        {% load dbt_govuk_django_core %}
        {% gds_pagination page_obj %}
        ```
    """

    previous: Optional[PaginationPrevNextLink] = None
    next: Optional[PaginationPrevNextLink] = None
    pagination_items: List[PaginationItem | PaginationEllipsis] = []

    if page_obj.has_previous():
        previous={
            "href": f"?page={page_obj.previous_page_number()}",
            "labelText": "Previous",
        }

    if page_obj.has_next():
        next = {
            "href": f"?page={page_obj.next_page_number()}",
            "labelText": "Next",
        }

    for page_number in page_obj.paginator.get_elided_page_range(
        page_obj.number, on_each_side=2, on_ends=1
    ):
        if page_number == "...":
            pagination_items.append({"ellipsis": True})
        else:
            pagination_items.append(
                {
                    "number": page_number,
                    "current": page_number == page_obj.number,
                    "href": f"?page={page_number}",
                }
            )

    return GovUKPagination(
        previous=previous,
        next=next,
        items=pagination_items
    )


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