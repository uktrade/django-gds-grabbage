# Tabs

See: [https://design-system.service.gov.uk/components/tabs/](https://design-system.service.gov.uk/components/tabs/)

## Usage

To use the tabs component, you need to load the `gds_grabbage` template tag library and then use the `gds_tabs` and `gds_tabs_tab` tags.

Similar to Django's `{% block %}` and `{% endblock %}` tags, the `gds_tabs` and `gds_tabs_tab` tags will have to be closed off with their respective `end_gds_tabs` and `end_gds_tabs_tab` tags.

### Example:

```django
{% load gds_grabbage %}
...
{% gds_tabs id="tabs-1" title="Tab title" %}
    {% gds_tabs_tab id="tab-1" label="Tab 1" %}
        <strong>Test 1</strong>
    {% end_gds_tabs_tab %}
    {% gds_tabs_tab id="tab-2" label="Tab 2" %}
        <strong>Test 2</strong>
    {% end_gds_tabs_tab %}
    {% gds_tabs_tab id="tab-3" label="Tab 3" %}
        <strong>Test 3</strong>
    {% end_gds_tabs_tab %}
{% end_gds_tabs %}
```
