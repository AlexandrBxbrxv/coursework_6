from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegister

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserRegister.as_view(), name='register')
]
