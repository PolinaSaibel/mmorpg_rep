from .models import *
from django.views.generic import ListView 
from django.shortcuts import render


# User = get_user_model()


# Create your views here.


class PostList(ListView):
    model = Post
    ordering = '-time_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
                
    #     return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['filterset'] = self.filterset
        return context