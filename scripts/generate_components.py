# Code to generate GovUK Design System components

new_component_python = """
from dataclasses import dataclass
from typing import Any, Dict

from dbt_govuk_django.django.core.govuk_frontend.base import GovUKComponent


@dataclass(kw_only=True)
class GovUK{capitalised}(GovUKComponent):

    jinja2_template = "govuk_frontend_jinja/components/{lower}/macro.html"
    macro_name = "govuk{capitalised}"

    def get_data(self) -> Dict[str, Any]:
        data = super().get_data()
        data.update(
            ...
        )
        return data

"""

# Loop over directories in "govuk_frontend_jinja/components/" where "govuk_frontend_jinja" is a python package
# and generate Python code for each component

import os

import govuk_frontend_jinja

jinja_path = govuk_frontend_jinja.__path__[0]

for component in os.listdir(jinja_path + "/templates/components"):
    # Generate Python code for each component
    # e.g. "govuk_frontend_jinja/components/accordion/macro.html" -> "dbt_django/core/govuk_frontend/accordion.py"
    filename = f"dbt_govuk_django/django/core/govuk_frontend/{component}.py"

    # Check if file already exists. If it does, don't overwrite it.
    if os.path.exists(filename):
        print(f"Skipping {filename} as it already exists")
        continue

    print(f"Generating {component.capitalize()} {component.lower()}")

    with open(filename, "w") as f:
        f.write(new_component_python.format(
            capitalised=component.capitalize(),
            lower=component.lower(),
        ))
