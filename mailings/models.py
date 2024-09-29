from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    topic = models.CharField(max_length=100, verbose_name='тема')
    body = models.TextField(verbose_name='содержимое')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='фио')
    comment = models.TextField(**NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
