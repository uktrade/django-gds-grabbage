import importlib
import pathlib

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

    Usage:
        {% gds_component jinja2_template="govuk_frontend_jinja/components/warning-text/macro.html" macro_name="govukWarningText" text="WARNING: something is wrong!" %}
    """

    component = GovUKComponent()
    component._jinja2_template = jinja2_template
    component._macro_name = macro_name
    return component.render(component_data={**kwargs})


# Loop over python files in this directory and update the register object
# with the tags and filters defined in each file.
for path in pathlib.Path(__file__).parent.iterdir():
    if path.suffix == ".py" and path.name != "__init__.py":
        module_name = path.stem
        module = importlib.import_module(f".{module_name}", __package__)
        register.tags.update(module.register.tags)
        register.filters.update(module.register.filters)
