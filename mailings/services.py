from django.core.cache import cache

from config.settings import CACHE_ENABLED
from mailings.models import Message, Client, Mailing


def get_message_list_from_cache():
    """Возвращает из кеша список Message, если кеш пуст записывает этот список в кеш"""
    if not CACHE_ENABLED:
        return Message.objects.all()
    key = 'message_list'
    message_list = cache.get(key)
    if message_list is not None:
        return message_list
    cache.set(key, Message.objects.all())
    return Message.objects.all()


def get_client_list_from_cache():
    """Возвращает из кеша список Client, если кеш пуст записывает этот список в кеш"""
    if not CACHE_ENABLED:
        return Client.objects.all()
    key = 'client_list'
    client_list = cache.get(key)
    if client_list is not None:
        return client_list
    cache.set(key, Client.objects.all())
    return Client.objects.all()


def get_mailing_list_from_cache():
    """Возвращает из кеша список Mailing, если кеш пуст записывает этот список в кеш"""
    if not CACHE_ENABLED:
        return Mailing.objects.all()
    key = 'mailing_list'
    mailing_list = cache.get(key)
    if mailing_list is not None:
        return mailing_list
    cache.set(key, Mailing.objects.all())
    return Mailing.objects.all()
