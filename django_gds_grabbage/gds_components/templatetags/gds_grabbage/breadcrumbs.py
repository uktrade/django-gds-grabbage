from typing import Any, Dict, List, Optional

from django import template
from django.core.paginator import Page
from django.template.base import Node, Parser, Token, token_kwargs

from django_gds_grabbage.gds_components.govuk_frontend.breadcrumbs import (
    BreadcrumbsItems,
)
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    DataclassNode,
    GovUKComponentNode,
)

register = template.Library()


class BreadcrumbsNode(GovUKComponentNode):
    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        if "items" not in self.resolved_kwargs:
            breadcrum_items: List[BreadcrumbsItems] = []
            for node in self.get_nodes_by_type(BreadcrumbsItemsNode):
                breadcrumb_node: BreadcrumbsItemsNode = node
                breadcrum_items.append(breadcrumb_node.resolve_dataclass(context))

            component_kwargs["items"] = breadcrum_items

        return component_kwargs


class BreadcrumbsItemsNode(DataclassNode):
    dataclass_cls = BreadcrumbsItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["text"] = self.resolved_kwargs.get("text")
        component_kwargs["html"] = self.resolved_kwargs.get("html")
        component_kwargs["href"] = self.resolved_kwargs.get("href")
        # TODO: Fix? Optional[Dict[str, Any]]
        component_kwargs["attributes"] = None

        return component_kwargs


@register.tag
def gds_breadcrumbs(parser: Parser, token: Token):
    """GDS breadcrumbs template tag."""
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)
    nodelist = template.NodeList()

    if "items" not in extra_context:
        nodelist = parser.parse(("end_gds_breadcrumbs",))
        parser.delete_first_token()

    return BreadcrumbsNode(
        extra_context=extra_context,
        component_name="breadcrumbs",
        nodelist=nodelist,
    )


@register.tag
def gds_breadcrumb_item(parser: Parser, token: Token):
    """GDS breadcrumb item template tag."""
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    return BreadcrumbsItemsNode(
        extra_context=extra_context,
    )
