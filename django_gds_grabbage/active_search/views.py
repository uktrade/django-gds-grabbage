import json

from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.base import ContextMixin


class ActiveSearchView(ContextMixin, View):
    pk_decoder = int

    def search(self, query):
        raise NotImplementedError

    def get_object(self, id):
        raise NotImplementedError

    def get_selected_pks(self):
        for pk in self.request.GET.getlist(self.hx_name):
            yield self.pk_decoder(pk)

    def do_search(self, request, *args, **kwargs):
        query = request.GET.get("query", "")

        search_results = self.search(query)

        return self.render_response(
            "gds_grabbage/active_search/search_results.html",
            context={
                "search_query": query,
                "search_results": search_results,
            },
            trigger="active-search:search",
        )

    def do_select(self, request, *args, **kwargs):
        obj_id = request.GET.get("id")

        obj = self.get_object(int(obj_id))

        return self.render_response(
            "gds_grabbage/active_search/selected_object.html",
            context={
                "object": obj,
            },
            trigger="active-search:change",
        )

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.hx_id = request.GET.get("hx_id")
        self.hx_name = request.GET.get("hx_name")
        self.selected_pks = list(self.get_selected_pks())

    def get(self, request, *args, **kwargs):
        match request.GET:
            case {"hx_action": action}:
                return getattr(self, f"do_{action}")(request, *args, **kwargs)

        return self.render_response("gds_grabbage/active_search/index.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context | {
            "hx_id": self.hx_id,
            "hx_name": self.hx_name,
            "view_name": self.request.resolver_match.view_name,
        }

    def render_response(self, template, context=None, trigger=None):
        if context is None:
            context = {}

        headers = {}

        if isinstance(trigger, str):
            trigger = trigger

        if isinstance(trigger, list):
            trigger = {name: "" for name in trigger}

        if isinstance(trigger, dict):
            trigger = json.dumps(trigger)

        if trigger:
            headers["HX-Trigger-After-Settle"] = trigger

        return TemplateResponse(
            request=self.request,
            template=template,
            context=self.get_context_data() | context,
            headers=headers,
        )
