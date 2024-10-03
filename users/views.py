from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from users.forms import UserCreateForm, UserLoginForm, UserProfileForm
from users.models import User
from users.services import send_email_verification_message


class UserLogin(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'
        return context_data


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


class UserProfile(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('main:index')
