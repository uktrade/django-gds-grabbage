from typing import List, Optional

from django import template
from django.core.paginator import Page

from django_gds_grabbage.django.core.govuk_frontend.base import PaginationPrevNext
from django_gds_grabbage.django.core.govuk_frontend.pagination import (
    GovUKPagination,
    PaginationItems,
)

register = template.Library()


@register.simple_tag
def gds_pagination(page_obj: Page):
    """GDS pagination template tag.

    Args:
        page_obj (Page):
            The Django Paginator Page object.

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
        {% load gds_grabbage %}
        {% gds_pagination page_obj %}
        ```
    """

    previous: Optional[PaginationPrevNext] = None
    next: Optional[PaginationPrevNext] = None
    pagination_items: List[PaginationItems] = []

    if page_obj.has_previous():
        previous = PaginationPrevNext(
            href=f"?page={page_obj.previous_page_number()}",
            labelText="Previous",
        )

    if page_obj.has_next():
        next = PaginationPrevNext(
            href=f"?page={page_obj.next_page_number()}",
            labelText="Next",
        )

    for page_number in page_obj.paginator.get_elided_page_range(
        page_obj.number, on_each_side=2, on_ends=1
    ):
        if page_number == "...":
            pagination_items.append({"ellipsis": True})
        else:
            pagination_items.append(
                {
                    "number": page_number,
                    "current": page_number == page_obj.number,
                    "href": f"?page={page_number}",
                }
            )

    return GovUKPagination(previous=previous, next=next, items=pagination_items)
