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


# Выборы для настройки РАССЫЛКИ
INTERVALS = [
    ('minute', 'Раз в минуту'),
    ('day', 'Раз в день'),
    ('week', 'Раз в неделю'),
    ('month', 'Раз в месяц')
]
STATUSES = [
    ('off', 'Отключена'),
    ('waiting_first', 'Запущена, Ожидает первой отправки'),
    ('send_waiting', 'Отправлена, ожидает следующей отправки')
]


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    first_sending = models.DateField(help_text='дата и время первой отправки рассылки', verbose_name='первая отправка')
    interval = models.CharField(max_length=15, choices=INTERVALS, default='month', verbose_name='периодичность')
    status = models.CharField(max_length=15, choices=STATUSES, default='off', verbose_name='статус')

    message = models.ForeignKey(Message, **NULLABLE, on_delete=models.SET_NULL, related_name='mailing_message',
                                verbose_name='сообщение рассылки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='фио')
    comment = models.TextField(**NULLABLE)

    mailing = models.ManyToManyField(Mailing, related_name='client_mailings', verbose_name='рассылки клиента')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

