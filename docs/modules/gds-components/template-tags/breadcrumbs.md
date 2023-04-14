# Breadcrumbs

See: [https://design-system.service.gov.uk/components/breadcrumbs/](https://design-system.service.gov.uk/components/breadcrumbs/)

## Usage

To use the breadcrumbs, you need to load the `gds_grabbage` template tag library and then use the `gds_breadcrumb`tag.

There are 2 ways you can use this tag, either by passing through the items to the tag, or by building the items with the `gds_breadcrumb_item` tag.

### Examples:

```django
{% load gds_grabbage %}
...
{% gds_breadcrumbs %}
    {% gds_breadcrumb_item text="Item 1" href="/" %}
    {% gds_breadcrumb_item text="Item 2" href="/" %}
    {% gds_breadcrumb_item text="Item 3" href="/" %}
    {% gds_breadcrumb_item text="Item 4" href="/" %}
{% end_gds_breadcrumbs %}
```

**OR** by building a list of `BreadcrumbsItems` and passing it through the context.

View:
```python
context["breadcrumb_items"] = [
    BreadcrumbsItems(
        text="Item 1",
        href="#",
    ),
    BreadcrumbsItems(
        text="Item 2",
        href="#",
    ),
    BreadcrumbsItems(
        text="Item 3",
        href="#",
    ),
]
```

Template:
```django
{% load gds_grabbage %}
...
{% gds_breadcrumbs items=breadcrumb_items %}
```
