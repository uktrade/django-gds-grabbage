from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from dbt_govuk_django.django.core.govuk_frontend.accordion import \
    GovUKAccordion
from dbt_govuk_django.django.core.govuk_frontend.back_link import GovUKBackLink
from dbt_govuk_django.django.core.govuk_frontend.breadcrumbs import \
    GovUKBreadcrumbs
from dbt_govuk_django.django.core.govuk_frontend.button import GovUKButton
from dbt_govuk_django.django.core.govuk_frontend.character_count import \
    GovUKCharacterCount
from dbt_govuk_django.django.core.govuk_frontend.pagination import \
    GovUKPagination

User = get_user_model()


class UserListingView(ListView):
    template_name = "example/user_listing.html"
    model = User
    paginate_by = 1


def components_view(request):
    context = {}
    context["back_link"] = GovUKBackLink(text="Back", href="/")
    context["button"] = GovUKButton(text="Save and continue")
    context["accordion"] = GovUKAccordion(
        id="accordion-default",
        items=[
            {
                "heading": {"text": "Heading 1"},
                "summary": {"text": "Summary 1"},
                "content": {"html": "Content 1"},
            },
            {
                "heading": {"text": "Heading 2"},
                "content": {"html": "Content 2"},
            },
            {
                "heading": {"text": "Heading 3"},
                "summary": {"text": "Summary 3"},
                "content": {"html": "Content 3"},
            },
            {
                "heading": {"text": "Heading 4"},
                "content": {"html": "Content 4"},
            },
        ],
    )
    context["breadcrumbs"] = GovUKBreadcrumbs(
        items=[
            {"text": "Home", "href": "/"},
            {"text": "Section", "href": "/section"},
        ]
    )
    context["character_count"] = GovUKCharacterCount(
        id="character-count",
        name="character-count",
        label={"text": "Character count"},
        hint={"text": "Hint text"},
        maxlength=200,
    )
    context["pagination"] = GovUKPagination(
        previous={
            "href": "/",
            "labelText": "Previous",
        },
        next={
            "href": "/",
            "labelText": "Next",
        },
        items=[
            {
                "number": 1,
                "current": True,
                "href": "/",
            },
            {
                "ellipsis": True,
            },
            {
                "number": 3,
                "href": "/",
            },
            {
                "number": 4,
                "href": "/",
            },
            {
                "ellipsis": True,
            },
            {
                "number": 6,
                "href": "/",
            },
        ],
    )
    return render(request, "example/components.html", context)
