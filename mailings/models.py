from django.db import models


class Message(models.Model):
    topic = models.CharField(max_length=100, verbose_name='тема')
    body = models.TextField(verbose_name='содержимое')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
