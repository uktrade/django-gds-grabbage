# Header

See: [https://design-system.service.gov.uk/components/header/](https://design-system.service.gov.uk/components/header/)

## Usage

To use the header component, you need to load the `gds_grabbage` template tag library and then use the `gds_header` and `gds_header_nav_item` tags.

Similar to Django's `{% block %}` and `{% endblock %}` tags, the `gds_header` and `gds_header_nav_item` tags will have to be closed off with their respective `end_gds_header` and `end_gds_header_nav_item` tags.

### Example:

```django
{% load gds_grabbage %}
...
{% gds_header homepageUrl="/" productName="Some product" serviceName="Service name" serviceUrl="/" %}
    {% gds_header_nav_item href="/" %}
        Nav item 1
    {% end_gds_header_nav_item %}
    {% gds_header_nav_item href="/" text="Nav item 2" %}
{% end_gds_header %}
```
