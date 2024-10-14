from django.core.cache import cache

from blog.models import Blog
from config.settings import CACHE_ENABLED


def get_blog_list_from_cache():
    """Возвращает из кеша список Blog, если кеш пуст записывает этот список в кеш"""
    if not CACHE_ENABLED:
        return Blog.objects.all()
    key = 'blog_list'
    blog_list = cache.get(key)
    if blog_list is not None:
        return blog_list
    cache.set(key, Blog.objects.all())
    return Blog.objects.all()
