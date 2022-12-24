from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.views.generic.edit import FormMixin
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .forms import PostCreateForm, ResponseForm, AuthorForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# User = get_user_model()


# Create your views here.


class PostList(ListView):
    """ вывод всех новостей """
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
        return context


class PostCreation(CreateView, LoginRequiredMixin,):
    """создание поста"""
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create.html'
    #permission_required = ('news.add_post')


    def post(self, request):
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.author = Author.objects.get(user=self.request.user)
            self.object.save()
            form.save()
            return redirect('posts')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

# добавить проверку формата в модели
   



class PostDetail(FormMixin, DetailView, ):  
    """вывод одного поста и откликов"""
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form_class=ResponseForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'pk':self.get_object().id})


    def post(self, request, *args, **kwargs):
        print('post resep')
        form=self.get_form()
        if form.is_valid():
            print('valid resep')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)    

    def form_valid(self, form):    
        self.object=form.save(commit=False) #сохраняем, но не отправляем
        self.object.author = self.request.user
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_context_data( self,  **kwargs, ):
        context = super().get_context_data()

        return context       



class PostUpdate(UpdateView, LoginRequiredMixin,):
    """обновление поста"""
    form_class = PostCreateForm
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')
    # success_url = reverse_lazy('post', kwargs={'pk':self.get_object().id})
    # permission_required = ('news.change_post') доступ группы

class PostDelete(DeleteView, LoginRequiredMixin,):
    """удаляем пост"""
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class ResponseCreation():
    """создание отклика"""
    pass


class AuthorDetail(DetailView, LoginRequiredMixin):
    """профиль пользрвателя"""
    model = Author
    template_name = 'author_profile.html'
    context_object_name = 'author'
    
    
    # def get_context_data( self,  **kwargs, ):
    #     context = super().get_context_data()

    #     return context       



class AuthorUpdate(UpdateView, LoginRequiredMixin,):
    """обновление профиля"""
    form_class = AuthorForm
    model = Author
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_profile')

