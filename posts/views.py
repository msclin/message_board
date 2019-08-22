from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    context_object_name = 'all_posts_list'
    model = Post
    template_name = 'home.html'
