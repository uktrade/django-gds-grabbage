from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()


class UserListingView(ListView):
    template_name = "example/user_listing.html"
    model = User
    paginate_by = 1
