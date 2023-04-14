from typing import List

from django import template

from django_gds_grabbage.gds_components.govuk_frontend.footer import (
    FooterContentlicence,
    FooterCopyright,
    FooterMeta,
    FooterMetaItems,
    FooterNavigation,
    FooterNavigationItems,
    GovUKFooter,
)
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class FooterNode(GovUKComponentNode):
    dataclass_cls = GovUKFooter

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        navigations: List[FooterNavigation] = []
        for node in self.get_nodes_by_type(FooterNavigationNode):
            navigations.append(node.resolve_dataclass(context))

        component_kwargs["navigation"] = navigations

        component_kwargs["meta"] = self.get_node_by_type_and_resolve(
            FooterMetaNode, context
        )
        component_kwargs["contentLicence"] = self.get_node_by_type_and_resolve(
            FooterContentlicenceNode, context
        )
        component_kwargs["copyright"] = self.get_node_by_type_and_resolve(
            FooterCopyrightNode, context
        )

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer",
    node_cls=FooterNode,
)


class FooterNavigationNode(GovUKComponentNode):
    dataclass_cls = FooterNavigation

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        nav_items: List[FooterNavigationItems] = []
        for node in self.get_nodes_by_type(FooterNavigationItemNode):
            nav_items.append(node.resolve_dataclass(context))

        component_kwargs["items"] = nav_items

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer_nav",
    node_cls=FooterNavigationNode,
)


class FooterNavigationItemNode(GovUKComponentNode):
    dataclass_cls = FooterNavigationItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer_nav_item",
    node_cls=FooterNavigationItemNode,
    end_if_not_contains=["text", "html"],
)


class FooterMetaNode(GovUKComponentNode):
    dataclass_cls = FooterMeta

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        nav_items: List[FooterMetaItems] = []
        for node in self.get_nodes_by_type(FooterMetaItemNode):
            nav_items.append(node.resolve_dataclass(context))

        component_kwargs["items"] = nav_items

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer_meta",
    node_cls=FooterMetaNode,
)


class FooterMetaItemNode(GovUKComponentNode):
    dataclass_cls = FooterMetaItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer_meta_item",
    node_cls=FooterMetaItemNode,
    end_if_not_contains=["text", "html"],
)


class FooterContentlicenceNode(GovUKComponentNode):
    dataclass_cls = FooterContentlicence

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer_content_licence",
    node_cls=FooterContentlicenceNode,
    end_if_not_contains=["text", "html"],
)


class FooterCopyrightNode(GovUKComponentNode):
    dataclass_cls = FooterCopyright

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_footer_copyright",
    node_cls=FooterCopyrightNode,
    end_if_not_contains=["text", "html"],
)
