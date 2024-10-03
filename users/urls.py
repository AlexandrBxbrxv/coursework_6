from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig

from users.views import UserRegister, email_verification, UserLogin

app_name = UsersConfig.name


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
]
