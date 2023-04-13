import os
import pathlib

from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from django_gds_grabbage.django.core.govuk_frontend.accordion import GovUKAccordion
from django_gds_grabbage.django.core.govuk_frontend.back_link import GovUKBackLink
from django_gds_grabbage.django.core.govuk_frontend.breadcrumbs import GovUKBreadcrumbs
from django_gds_grabbage.django.core.govuk_frontend.button import GovUKButton
from django_gds_grabbage.django.core.govuk_frontend.character_count import (
    GovUKCharacterCount,
)
from django_gds_grabbage.django.core.govuk_frontend.checkboxes import GovUKCheckboxes
from django_gds_grabbage.django.core.govuk_frontend.cookie_banner import (
    GovUKCookieBanner,
)
from django_gds_grabbage.django.core.govuk_frontend.date_input import GovUKDateInput
from django_gds_grabbage.django.core.govuk_frontend.error_message import (
    GovUKErrorMessage,
)
from django_gds_grabbage.django.core.govuk_frontend.pagination import GovUKPagination


User = get_user_model()


class UserListingView(ListView):
    template_name = "example/user_listing.html"
    model = User
    paginate_by = 1


COMPONENT_EXAMPLES = {
    "accordion": GovUKAccordion(
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
    ),
    "back-link": GovUKBackLink(text="Back", href="/"),
    "breadcrumbs": GovUKBreadcrumbs(
        items=[
            {"text": "Home", "href": "/"},
            {"text": "Section", "href": "/section"},
        ]
    ),
    "button": GovUKButton(text="Save and continue"),
    "character-count": GovUKCharacterCount(
        id="character-count",
        name="character-count",
        label={"text": "Character count"},
        hint={"text": "Hint text"},
        maxlength=200,
        maxwords="",
    ),
    "checkboxes": GovUKCheckboxes(
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
    ),
    "cookie-banner": GovUKCookieBanner(
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
    ),
    "date-input": GovUKDateInput(
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
    ),
    "error-message": GovUKErrorMessage(text="Error message"),
    "pagination": GovUKPagination(
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
    ),
}


class CustomForm(forms.Form):
    # Checkboxes
    contact = forms.ChoiceField(
        label="How would you like to be contacted?",
        choices=(
            ("email", "Email"),
            ("phone", "Phone"),
            ("text", "Text"),
        ),
        widget=forms.CheckboxSelectMultiple,
    )


def component_view(request, component_hyphenated_name: str):
    component_underscored_name = component_hyphenated_name.replace("-", "_")
    component_name = component_hyphenated_name.replace("-", " ").capitalize()
    context = {
        "component_hyphenated_name": component_hyphenated_name,
        "component_underscored_name": component_underscored_name,
        "component_name": component_name,
        "component": COMPONENT_EXAMPLES.get(component_hyphenated_name),
    }

    parent_dir = pathlib.Path(__file__).parent
    custom_component_template = (
        parent_dir / f"templates/example/components/{component_underscored_name}.html"
    )

    context.update(form=CustomForm)

    if os.path.exists(custom_component_template):
        return render(request, custom_component_template, context)

    return render(request, "example/components/base.html", context)


def components_view(request):
    context = {"component_list": []}
    for component_hyphenated_name in COMPONENT_EXAMPLES:
        context["component_list"].append(component_hyphenated_name)
    context["component_list"].sort()
    return render(request, "example/components/listing.html", context)
