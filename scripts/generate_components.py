# Code to generate GovUK Design System components

new_component_python = '''
from dataclasses import dataclass
from typing import Any, Dict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUK{component_class_name}(GovUKComponent):
    """GovUK {component_name}

    See: {gds_url}
    """

    # Dataclass fields go here...
    ...

    _jinja2_template = "govuk_frontend_jinja/components/{component_hyphenated}/macro.html"
    _macro_name = "govuk{component_class_name}"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            # Add dataclass values to the data dict here...
            ...
        )
        return data

'''

# Loop over directories in "govuk_frontend_jinja/components/" where "govuk_frontend_jinja" is a python package
# and generate Python code for each component

import os

import govuk_frontend_jinja

jinja_path = govuk_frontend_jinja.__path__[0]

for component_hyphenated in os.listdir(jinja_path + "/templates/components"):
    # Generate Python code for each component
    # e.g. "govuk_frontend_jinja/components/accordion/macro.html" -> "dbt_django/core/govuk_frontend/accordion.py"

    component_underscored = component_hyphenated.replace("-", "_")
    filename = f"dbt_govuk_django/django/core/govuk_frontend/{component_underscored}.py"

    # Check if file already exists. If it does, don't overwrite it.
    if os.path.exists(filename):
        print(f"Skipping {filename} as it already exists")
        continue

    component_name = " ".join(
        [word.capitalize() for word in component_hyphenated.split("-")]
    )
    component_class_name = "".join(
        [word.capitalize() for word in component_hyphenated.split("-")]
    )

    print(f"Generating {component_class_name} {component_hyphenated} {component_underscored}")

    gds_url = f"https://design-system.service.gov.uk/components/{component_hyphenated}/"

    with open(filename, "w") as f:
        f.write(new_component_python.format(
            component_name=component_name,
            component_class_name=component_class_name,
            component_hyphenated=component_hyphenated,
            gds_url=gds_url,
        ))
