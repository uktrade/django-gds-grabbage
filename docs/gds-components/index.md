# GDS Components

See: [https://design-system.service.gov.uk/components/](https://design-system.service.gov.uk/components/)

## How to use the Python components?

The components have been built in a way that allows you to simply pass through a dict as the `kwargs` for the component in the same format that we see in teh Nunjucks template examples on the GDS website.

For example, the **Back Link**, which can be found [here](https://design-system.service.gov.uk/components/back-link/), has the folowing Nunjucks example:

```nunjucks
{% from "govuk/components/back-link/macro.njk" import govukBackLink %}

{{ govukBackLink({
  text: "Back",
  href: "#"
}) }}
```

To use the Python version of this component you can do the following:

**views.py**
```python
from django_gds_grabbage.django.core.govuk_frontend.back_link import GovUKBackLink

def my_view(request):
    data = {
        "text": "Back",
        "href": "#"
    }
    context = {
        'back_link': GovUKBackLink(**data)
    }
    return render(request, 'my_template.html', context)
```

**my_template.html**
```django
{% load gds_grabbage %}

{{ back_link }}
```

This works because the `GovUKBackLink` class inherits from the `GovUKComponent` class which handles the rendering of the component.

### Keyword Arguments
Instead of defining a `data` dict and passing it through as `**data` you can also pass through the keyword arguments directly.

```python
GovUKBackLink(
    text="Back",
    href="#",
)
```

## Why do only some components have templatetags?

As we find common use cases for components we create template tags to make those scenarios easier to implement. For example, we know that Django `ListView`s return paginated pages, so we created the `gds_pagination` template tag that accepts a paginated page as an argument and renders the pagination component. Please contribute any other template tags that you find useful.