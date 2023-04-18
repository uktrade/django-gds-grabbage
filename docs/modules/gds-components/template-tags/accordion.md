# Accordion

See: [https://design-system.service.gov.uk/components/accordion/](https://design-system.service.gov.uk/components/accordion/)

## Usage

To use the accordion, you need to load the `gds_grabbage` template tag library and then use the `gds_accordion` and `gds_accordion_item` tags.

### Example:

```django
{% load gds_grabbage %}
...
{% gds_accordion id="accordion-1" %}
    {% gds_accordion_item heading="Heading 1" summary="Summary 1" %}
        Some <strong>HTML</strong> content
    {% end_gds_accordion_item %}
    {% gds_accordion_item heading="Heading 2" summary="Summary 2" %}
        Some more <strong>HTML</strong> content
    {% end_gds_accordion_item %}
{% end_gds_accordion %}
```
