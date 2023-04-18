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
from django.views.generic import TemplateView

from example_project.example.views.active_search import (
    ExampleFormView,
    UserActiveSearchView,
)
from example_project.example.views.gds_components import (
    UserListingView,
    gds_components_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", UserListingView.as_view(), name="user-listing"),
    path("components/", gds_components_view, name="components"),
    path("active-search/", ExampleFormView.as_view(), name="active-search"),
    path("search-users/", UserActiveSearchView.as_view(), name="search-users"),
    path(
        "templates/confirmation/",
        TemplateView.as_view(
            template_name="gds_grabbage/gds_components/confirmation.html"
        ),
        name="confirmation",
    ),
    path(
        "templates/404/",
        TemplateView.as_view(template_name="gds_grabbage/gds_components/404.html"),
        name="confirmation",
    ),
    path(
        "templates/500/",
        TemplateView.as_view(template_name="gds_grabbage/gds_components/500.html"),
        name="confirmation",
    ),
]
