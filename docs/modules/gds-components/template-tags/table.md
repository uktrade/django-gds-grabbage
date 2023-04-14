header = ["First name", "Last name", "Email"]
results = [
    {
        "First name": "John",
        "Last name": "Smith",
        "Email": "",
    }
]

{% gds_table head=header rows=results %}
OR
{% gds_table %}
    {% gds_table_head %}
        {% gds_table_head_item text="Col 1" %}
        {% gds_table_head_item text="Col 2" %}
        {% gds_table_head_item text="Col 3" %}
    {% end_gds_table_head %}
    {% gds_table_rows %}
        {% gds_table_row_item "Value 1" "Value 2" "Value 3" %}
    {% end_gds_table_row %}
{% end_gds_table %}
