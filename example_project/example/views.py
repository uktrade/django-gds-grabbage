from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from dbt_govuk_django.django.core.govuk_frontend.accordion import GovUKAccordion
from dbt_govuk_django.django.core.govuk_frontend.back_link import GovUKBackLink
from dbt_govuk_django.django.core.govuk_frontend.breadcrumbs import GovUKBreadcrumbs
from dbt_govuk_django.django.core.govuk_frontend.button import GovUKButton
from dbt_govuk_django.django.core.govuk_frontend.character_count import (
    GovUKCharacterCount,
)
from dbt_govuk_django.django.core.govuk_frontend.checkboxes import GovUKCheckboxes
from dbt_govuk_django.django.core.govuk_frontend.cookie_banner import GovUKCookieBanner
from dbt_govuk_django.django.core.govuk_frontend.date_input import GovUKDateInput
from dbt_govuk_django.django.core.govuk_frontend.error_message import GovUKErrorMessage
from dbt_govuk_django.django.core.govuk_frontend.pagination import GovUKPagination

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
    context["checkboxes"] = GovUKCheckboxes(
        name="checkboxes_1",
        fieldset={
            "legend": {"text": "Legend text"},
        },
        errorMessage={"text": "Error message"},
        hint={"text": "Hint text"},
        items=[
            {
                "value": "1",
                "text": "Option 1",
            },
            {
                "value": "2",
                "text": "Option 2",
            },
            {
                "divider": "or",
            },
            {
                "value": "3",
                "text": "Option 3",
                "hint": {
                    "text": "Hint text",
                },
                "behaviour": "exclusive",
            },
        ],
    )
    context["cookie_banner"] = GovUKCookieBanner(
        ariaLabel="Cookies on [name of service]",
        messages=[
            {
                "headingText": "Cookies on [name of service]",
                "html": "<p class='govuk-body'>Some text</p>",
                "actions": [
                    {
                        "text": "Accept analytics cookies",
                        "type": "button",
                    },
                    {
                        "text": "Reject analytics cookies",
                        "type": "button",
                    },
                    {
                        "text": "View cookies",
                        "href": "#",
                    },
                ],
            },
            {
                "html": "<p class='govuk-body'>Some text</p>",
                "role": "alert",
                "hidden": True,
                "actions": [{"text": "Hide cookie message"}],
            },
            {
                "html": "<p class='govuk-body'>Some text</p>",
                "role": "alert",
                "hidden": True,
                "actions": [{"text": "Hide cookie message"}],
            },
        ],
    )
    context["date_input"] = GovUKDateInput(
        id="passport-issued",
        namePrefix="passport-issued",
        fieldset={
            "legend": {
                "text": "When was your passport issued?",
                "isPageHeading": True,
                "classes": "govuk-fieldset__legend--l",
            }
        },
        hint={
            "text": "For example, 27 3 2007",
        },
        errorMessage={
            "text": "The date your passport was issued must be in the past",
        },
        items=[
            {
                "classes": "govuk-input--width-2 govuk-input--error",
                "name": "day",
                "value": "6",
            },
            {
                "classes": "govuk-input--width-2 govuk-input--error",
                "name": "month",
                "value": "3",
            },
            {
                "classes": "govuk-input--width-4 govuk-input--error",
                "name": "year",
                "value": "2076",
            },
        ],
    )
    context["error_message"] = GovUKErrorMessage(text="Error message")
    return render(request, "example/components.html", context)
