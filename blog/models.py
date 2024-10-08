from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/image', **NULLABLE, verbose_name='изображение')
    views_count = models.PositiveIntegerField(default=0, verbose_name='счетчик просмотров')
    publish_date = models.DateField(auto_now=True, verbose_name='дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_owner', verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
