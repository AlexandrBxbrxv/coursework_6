from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    token = models.CharField(max_length=50, **NULLABLE, verbose_name='token')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        permissions = [
            ('change_is_active', 'Can change is_active of user'),
        ]

        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
