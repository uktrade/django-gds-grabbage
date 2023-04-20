from django.urls import path
from example_active_search.views import ExampleFormView, UserActiveSearchView

urlpatterns = [
    path("", ExampleFormView.as_view(), name="active-search"),
    path("search-users/", UserActiveSearchView.as_view(), name="search-users"),
]
