---
title: GOV.UK Frontend
---

# GOV.UK Frontend

This project uses the [GOV.UK Frontend Jinja Macros](https://github.com/LandRegistry/govuk-frontend-jinja) package for the component templates. This means that we can generate Django objects that are renderable with up to date GDS markup.

## Adding/updating components

To generate any new components, run the following commands:

```bash
poetry update govuk_frontend_jinja
poetry run python ./scripts/generate_components.py
```

This will let you know of any new components that need adding to the project.
