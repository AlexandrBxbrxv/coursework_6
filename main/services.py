from django.core.cache import cache

from blog.models import Blog
from config.settings import CACHE_ENABLED
from mailings.models import Mailing, Client


def send_mailing():
    from pytz import timezone
    import datetime
    from smtplib import SMTPException
    from django.core.mail import BadHeaderError
    from config import settings
    from django.core.mail import send_mail
    from config.settings import EMAIL_HOST_USER
    from mailings.models import Mailing
    from mailings.models import MailingTry

    zone = timezone(settings.TIME_ZONE)
    current_datetime = datetime.datetime.now(zone).replace(microsecond=0)
    mailings = Mailing.objects.exclude(status='off').filter(next_sending__lte=current_datetime)
    for mailing in mailings:
        subject = mailing.message.topic
        message = mailing.message.body
        from_email = EMAIL_HOST_USER
        recipient_list = [client.email for client in mailing.clients.all()]

        mailing_try = MailingTry(
            try_status=False,
            mailing=mailing,
            owner=mailing.owner,
            email_response=''
        )

        if subject and message and from_email:
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                mailing_try.try_status = True
                mailing_try.save()

            except BadHeaderError as e:
                e_msg = f'Обнаружен неверный заголовок. Ошибка: {e}'
                mailing_try.email_response = e_msg
                mailing_try.save()

            except SMTPException as e:
                e_msg = f'Произошла ошибка при отправке письма. Ошибка: {e}'
                mailing_try.email_response = e_msg
                mailing_try.save()

        else:
            e_msg = 'Отсутствует сообщение'
            mailing_try.email_response = e_msg
            mailing_try.save()

        mailing.status = 'send_waiting'
        mailing.last_sending = current_datetime
        mailing.save()

        if mailing.interval == 'day':
            mailing.next_sending = mailing.last_sending + datetime.timedelta(days=1)
            mailing.save()
        if mailing.interval == 'week':
            mailing.next_sending = mailing.last_sending + datetime.timedelta(weeks=1)
            mailing.save()
        if mailing.interval == 'month':
            mailing.next_sending = mailing.last_sending + datetime.timedelta(days=30)
            mailing.save()


def get_all_mailings_len_from_cache():
    """Возвращает из кеша количество рассылок, если кеш пуст записывает это количество в кеш"""
    if not CACHE_ENABLED:
        return len(Mailing.objects.all())
    key = 'all_mailings_len'
    all_mailings_len = cache.get(key)
    if all_mailings_len is not None:
        return all_mailings_len
    cache.set(key, len(Mailing.objects.all()))
    return len(Mailing.objects.all())


def get_active_mailings_len_from_cache():
    """Возвращает из кеша количество активных рассылок, если кеш пуст записывает это количество в кеш"""
    if not CACHE_ENABLED:
        return len(Mailing.objects.exclude(status='off'))
    key = 'active_mailings_len'
    active_mailings_len = cache.get(key)
    if active_mailings_len is not None:
        return active_mailings_len
    cache.set(key, len(Mailing.objects.exclude(status='off')))
    return len(Mailing.objects.exclude(status='off'))


def get_all_clients_len_from_cache():
    """Возвращает из кеша количество клиентов, если кеш пуст записывает это количество в кеш"""
    if not CACHE_ENABLED:
        return len(Client.objects.all())
    key = 'all_clients_len'
    all_clients_len = cache.get(key)
    if all_clients_len is not None:
        return all_clients_len
    cache.set(key, len(Client.objects.all()))
    return len(Client.objects.all())


def get_popular_blogs_from_cache():
    """Возвращает из кеша 3 популярных по просмотрам блога, если кеш пуст записывает эти объекты в кеш"""
    if not CACHE_ENABLED:
        return Blog.objects.order_by('-views_count')[:3]
    key = 'popular_blogs'
    popular_blogs = cache.get(key)
    if popular_blogs is not None:
        return popular_blogs
    cache.set(key, Blog.objects.order_by('-views_count')[:3])
    return Blog.objects.order_by('-views_count')[:3]
