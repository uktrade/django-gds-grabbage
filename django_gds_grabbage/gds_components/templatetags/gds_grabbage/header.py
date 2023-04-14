from typing import List

from django import template

from django_gds_grabbage.gds_components.govuk_frontend.header import (
    GovUKHeader,
    HeaderNavigation,
)
from django_gds_grabbage.gds_components.govuk_frontend.tabs import TabsItems
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class HeaderNode(GovUKComponentNode):
    dataclass_cls = GovUKHeader

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        nav_items: List[TabsItems] = []
        for node in self.get_nodes_by_type(HeaderNavItemNode):
            nav_items.append(node.resolve_dataclass(context))

        component_kwargs["navigation"] = nav_items
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_header",
    node_cls=HeaderNode,
)


class HeaderNavItemNode(GovUKComponentNode):
    dataclass_cls = HeaderNavigation

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        href = component_kwargs["href"]
        component_kwargs["active"] = bool(href == context["request"].path)

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_header_nav_item",
    node_cls=HeaderNavItemNode,
    end_if_not_contains=["text", "html"],
)
