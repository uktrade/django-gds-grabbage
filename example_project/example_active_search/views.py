from django import forms
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import FormView

from django_gds_grabbage.active_search.forms import active_search_field
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
    users = active_search_field(
        forms.ModelMultipleChoiceField,
        view_name="search-users",
    )(
        queryset=User.objects.all(),
        required=False,
    )


class ExampleFormView(SuccessMessageMixin, FormView):
    template_name = "example_active_search/active_search.html"
    form_class = ExampleForm
    success_url = reverse_lazy("active-search")

    def get_initial(self):
        users = self.request.session.get("active-search-example:users", [])
        return {"users": users}

    def form_valid(self, form):
        self.request.session["active-search-example:users"] = [
            user.pk for user in form.cleaned_data["users"]
        ]
        return super().form_valid(form)

    def get_success_message(self, cleaned_data) -> str:
        users = ", ".join([str(user) for user in cleaned_data.get("users", [])])
        return f"Successfully submitted users {users}"
