from django import template

from django_gds_grabbage.gds_components.govuk_frontend.phase_banner import (
    GovUKPhaseBanner,
)
from django_gds_grabbage.gds_components.govuk_frontend.tag import GovUKTag
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class PhaseBannerNode(GovUKComponentNode):
    dataclass_cls = GovUKPhaseBanner

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        nodes_to_hide = []

        component_kwargs["tag"] = None
        for node in self.get_nodes_by_type(GovUKComponentNode):
            if node.dataclass_cls == GovUKTag:
                component_kwargs["tag"] = node.build_component_kwargs(context)
                nodes_to_hide.append(node)
                break

        for node_to_hide in nodes_to_hide:
            self.nodelist.remove(node_to_hide)

        rendered_contents = self.nodelist.render(context).strip()

        for node_to_hide in nodes_to_hide:
            self.nodelist.append(node_to_hide)

        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_phase_banner",
    node_cls=PhaseBannerNode,
)
