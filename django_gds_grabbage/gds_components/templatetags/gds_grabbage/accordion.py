from typing import List

from django import template

from django_gds_grabbage.gds_components.govuk_frontend.accordion import GovUKAccordion
from django_gds_grabbage.gds_components.govuk_frontend.base import (
    AccordionItem,
    TextAndHtml,
)
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class AccordionNode(GovUKComponentNode):
    dataclass_cls = GovUKAccordion

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        accordion_items: List[AccordionItem] = []
        for node in self.get_nodes_by_type(AccordionItemNode):
            accordion_items.append(node.resolve_dataclass(context))

        component_kwargs["items"] = accordion_items
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_accordion",
    node_cls=AccordionNode,
)


class AccordionItemNode(GovUKComponentNode):
    dataclass_cls = AccordionItem

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["heading"] = TextAndHtml(text=component_kwargs["heading"])
        component_kwargs["summary"] = TextAndHtml(text=component_kwargs["summary"])
        component_kwargs["content"] = TextAndHtml(html=self.nodelist.render(context))

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_accordion_item",
    node_cls=AccordionItemNode,
)
