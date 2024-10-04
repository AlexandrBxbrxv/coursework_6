from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.views import LoginView

from users.forms import UserCreateForm, UserLoginForm, UserProfileForm, UserProfileManagerForm
from users.models import User
from users.services import send_email_verification_message


class UserLogin(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'
        return context_data


# Create, Read, Update для User #####################################
class UserRegister(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        user = form.save()
        send_email_verification_message(self, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'
        return context_data


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect('users:login')


class UserList(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context


class UserProfile(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('main:index')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.pk:
            return UserProfileForm
        if user.has_perm('users.change_is_active'):
            return UserProfileManagerForm
        else:
            raise PermissionDenied

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        return context
