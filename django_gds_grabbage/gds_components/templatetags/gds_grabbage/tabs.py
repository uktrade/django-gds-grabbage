from typing import List

from django import template

from django_gds_grabbage.gds_components.govuk_frontend.base import TextAndHtml
from django_gds_grabbage.gds_components.govuk_frontend.tabs import GovUKTabs, TabsItems
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class TabsNode(GovUKComponentNode):
    dataclass_cls = GovUKTabs

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        tabs: List[TabsItems] = []
        for node in self.get_nodes_by_type(TabsTabNode):
            tabs.append(node.resolve_dataclass(context))

        component_kwargs["items"] = tabs
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_tabs",
    node_cls=TabsNode,
)


class TabsTabNode(GovUKComponentNode):
    dataclass_cls = TabsItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["panel"] = TextAndHtml(html=self.nodelist.render(context))

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_tabs_tab",
    node_cls=TabsTabNode,
)
