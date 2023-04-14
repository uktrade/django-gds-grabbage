from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from django import forms

from django_gds_grabbage.active_search.views import ActiveSearchView


User = get_user_model()


class UserActiveSearchView(ActiveSearchView):
    def search(self, query):
        if not query:
            return []

        return User.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        ).exclude(pk__in=self.selected_pks)

    def get_object(self, id):
        return User.objects.get(pk=id)


class ExampleForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())


def active_search_view(request):
    users = User.objects.all()[:1]
    example_form = ExampleForm(data={"users": users})

    return render(
        request,
        "example/active_search.html",
        {
            "users": users,
            "example_form": example_form,
        },
    )
