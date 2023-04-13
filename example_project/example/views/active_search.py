from django.shortcuts import render

from django_gds_grabbage.active_search.views import ActiveSearchView


TEST_DATA = [
    {"pk": 1, "name": "Apple"},
    {"pk": 2, "name": "Banana"},
    {"pk": 3, "name": "Pear"},
    {"pk": 4, "name": "Kiwi"},
    {"pk": 5, "name": "Grape"},
]


class MyActiveSearchView(ActiveSearchView):
    def search(self, query):
        if not query:
            return []

        return [
            x
            for x in TEST_DATA
            if query.lower() in x["name"].lower() and x["pk"] not in self.selected_pks
        ]

    def get_object(self, id):
        for x in TEST_DATA:
            if x["pk"] == id:
                return x


def active_search_view(request):
    selected = TEST_DATA[2]

    return render(
        request, "example/active_search.html", {"selected_objects": [selected]}
    )
