from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog
from blog.services import get_blog_list_from_cache


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
        context_data['object_list'] = get_blog_list_from_cache()
        return context_data


class BlogDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Blog
    permission_required = 'blog.view_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности блога'
        return context_data


class BlogUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    permission_required = 'blog.change_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование блога'
        return context_data


class BlogDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    permission_required = 'blog.delete_blog'
    success_url = reverse_lazy('blog:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление блога'
        return context_data
