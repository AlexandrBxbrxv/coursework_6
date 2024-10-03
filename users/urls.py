from django.urls import path
from users.apps import UsersConfig

from users.views import UserRegister, email_verification

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
]
