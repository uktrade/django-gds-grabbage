"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from example_project.example.views import (
    UserListingView,
    component_view,
    components_view,
    active_search_view,
    MyActiveSearchView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", UserListingView.as_view(), name="user-listing"),
    path("components/", components_view, name="components"),
    path(
        "components/<str:component_hyphenated_name>/",
        component_view,
        name="component",
    ),
    path("active-search/", active_search_view, name="active-search"),
    path("search/", MyActiveSearchView.as_view(), name="search"),
]
