from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.forms import BlogForm
from blog.models import Blog


# CRUD для Blog #####################################################
class BlogCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:blog_create')

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание блога'
        return context_data


class BlogList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Blog
    permission_required = 'blog.view_blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Блоги'
        return context_data


class BlogDetail(DetailView):
    model = Blog
    permission_required = 'blog.view_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности блога'
        return context_data
