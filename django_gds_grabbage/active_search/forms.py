from django import forms


def active_search_field(field_cls, view_name: str):
    class ActiveSearchBoundField(forms.BoundField):
        def value(self):
            value = super().value()
            return self.field.to_python(value)

    class ActiveSearchWidget(field_cls.widget):
        template_name = "gds_grabbage/active_search/active_search.html"

        class Media:
            css = {
                "all": ["gds_grabbage/active_search/active_search.css"],
            }

        def get_context(self, name, value, attrs):
            return {
                "hx_id": attrs.get("id"),
                "hx_name": name,
                "view_name": view_name,
                "selected_objects": value,
            }

    class ActiveSearchField(field_cls):
        widget = ActiveSearchWidget

        def get_bound_field(self, form, field_name):
            return ActiveSearchBoundField(form, self, field_name)

    return ActiveSearchField
