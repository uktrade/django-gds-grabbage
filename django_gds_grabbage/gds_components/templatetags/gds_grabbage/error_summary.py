from typing import List

from django import template

from django_gds_grabbage.gds_components.govuk_frontend.error_summary import (
    ErrorSummaryErrorlist,
    GovUKErrorSummary,
)
from django_gds_grabbage.gds_components.templatetags.gds_grabbage import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class ErrorSummaryNode(GovUKComponentNode):
    dataclass_cls = GovUKErrorSummary

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        error_list: List[ErrorSummaryErrorlist] = []
        for node in self.nodelist.get_nodes_by_type(ErrorSummaryErrorListItemNode):
            error_list.append(node.resolve_dataclass(context))
        component_kwargs["errorList"] = error_list

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_error_summary",
    node_cls=ErrorSummaryNode,
)


class ErrorSummaryErrorListItemNode(GovUKComponentNode):
    dataclass_cls = ErrorSummaryErrorlist

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in self.extra_context:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_error_summary_error_list_item",
    node_cls=ErrorSummaryErrorListItemNode,
    end_if_not_contains=["text", "html"],
)
