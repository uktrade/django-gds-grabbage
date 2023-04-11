from django import template

from django_gds_grabbage.django.core.govuk_frontend.base import GovUKComponent

register = template.Library()


@register.simple_tag
def gds_component(jinja2_template: str, macro_name: str, **kwargs):
    """Fallback template tag for rendering a GovUK component.

    Args:
        jinja2_template (str): The path to the Jinja2 template.
        macro_name (str): The name of the macro to render.
        **kwargs: The keyword arguments to pass to the macro.
    """

    component = GovUKComponent()
    component._jinja2_template = jinja2_template
    component._macro_name = macro_name
    return component.render(component_data={**kwargs})


from django_gds_grabbage.django.core.templatetags.gds_grabbage import (
    accordion,
    pagination,
)
