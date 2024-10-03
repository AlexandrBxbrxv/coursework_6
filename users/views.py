from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserCreateForm
from users.models import User


class UserRegister(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'
        return context_data
