from typing import Any

from django import template

from django_gds_grabbage.active_search.types import SelectableObject

register = template.Library()


@register.inclusion_tag("gds_grabbage/active_search/active_search.html")
def active_search(
    *,
    hx_id: str,
    hx_name: str,
    view_name: str,
    selected_objects: list[SelectableObject],
) -> dict[str, Any]:
    """_summary_

    Args:
        hx_id: _description_
        hx_name: _description_
        view_name: _description_
        selected_objects: _description_

    Returns:
        _description_
    """
    return {
        "hx_id": hx_id,
        "hx_name": hx_name,
        "view_name": view_name,
        "selected_objects": selected_objects,
    }
