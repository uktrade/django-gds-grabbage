from typing import Optional

from django import template
from django.urls import reverse

from django_gds_grabbage.django.core.govuk_frontend.back_link import GovUKBackLink

register = template.Library()


@register.simple_tag
def gds_back_link(
    viewname: Optional[str] = None,
    href: Optional[str] = None,
    text: Optional[str] = None,
):
    if not viewname and not href:
        raise ValueError("Either viewname or href must be provided.")
    if viewname and href:
        raise ValueError("Only one of viewname or href must be provided.")

    if viewname:
        href = reverse(viewname)

    return GovUKBackLink(
        href=href,
        text=text,
    )
