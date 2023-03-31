from django import template
from django.core.paginator import Page

register = template.Library()

@register.inclusion_tag("dbt_govuk_django_core/templatetags/pagination.html")
def gds_pagination(page_obj: Page, page_obj_name: str = "pages"):
    """GDS pagination template tag.

    Args:
        page_obj (Page):
            The Django Paginator Page object.
        page_obj_name (str, optional):
            The plural name for the object displayed on the page. Defaults to
            "pages".

    Usage:
        This template tag is designed to be used with the Django pagination,
        below is an example of it being used with a ListView.

        *views.py:*
        ```python
        from django.views.generic import ListView
        from django.contrib.auth import get_user_model

        User = get_user_model()


        class UserListingView(ListView):
            template_name = "template.html"
            model = User
            paginate_by = 25
        ```

        *template.html:*
        ```django-html
        {% load dbt_govuk_django_core %}
        {% gds_pagination page_obj page_obj_name %}
        ```
    """
    return {
        "page_obj": page_obj,
        "page_numbers": list(
            page_obj.paginator.get_elided_page_range(
                page_obj.number, on_each_side=2, on_ends=1
            )
        ),
        "page_obj_name": page_obj_name,
    }
4