from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from mailings.forms import StyleFormMixin
from users.models import User


class UserCreateForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    pass


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
