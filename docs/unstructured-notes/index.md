# Dev thoughts

A place to dump thoughts before categorising them into docs/code.


## Readme Driven Development

### Installation

```bash
pip install django-gds-grabbage
```

```python
INSTAALLED_APPS = [
    ...
    "django_gds_grabbage"
]
```

### Usage

- override a widget (SplitDateWidget)
- use templatetags to build a GDS component

```django
{% load gds_grabbage %}
...
{% gds_messages %}
{% gds_error_summary form %}
{% gds_table table_data %}
{% gds_pagination page_obj %}
...
{% gds_accordion "accordion-1" %}
    {% gds_accordion_item "Heading 1" "Summary 1" %}
        <strong>Content1</strong>
    {% end_gds_accordion_item %}
    {% gds_accordion_item "Heading 2" "Summary 2" %}
        <strong>Content2</strong>
    {% end_gds_accordion_item %}
{% end_gds_accordion %}
```
