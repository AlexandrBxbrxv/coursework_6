from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    topic = models.CharField(max_length=100, verbose_name='тема')
    body = models.TextField(verbose_name='содержимое')

    owner = models.ForeignKey(User, related_name='message_owner', on_delete=models.CASCADE,
                              **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='фио')
    comment = models.TextField(**NULLABLE)

    owner = models.ForeignKey(User, related_name='client_owner', on_delete=models.CASCADE,
                              **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):

    INTERVALS = [
        ('day', 'Раз в день'),
        ('week', 'Раз в неделю'),
        ('month', 'Раз в месяц')
    ]
    STATUSES = [
        ('off', 'Отключена'),
        ('waiting_first', 'Запущена, Ожидает первой отправки'),
        ('send_waiting', 'Отправлена, ожидает следующей отправки')
    ]

    name = models.CharField(max_length=100, **NULLABLE, verbose_name='название')
    next_sending = models.DateTimeField(**NULLABLE, help_text='ГГГГ-ММ-ДД ЧЧ:ММ:СС',
                                        verbose_name='дата и время отправки')
    last_sending = models.DateTimeField(**NULLABLE, verbose_name='крайняя отправка')
    interval = models.CharField(max_length=15, choices=INTERVALS, default='month', verbose_name='периодичность')
    status = models.CharField(max_length=15, choices=STATUSES, default='off', verbose_name='статус')

    message = models.ForeignKey(Message, **NULLABLE, on_delete=models.SET_NULL, related_name='mailing_message',
                                verbose_name='сообщение рассылки')

    clients = models.ManyToManyField(Client, related_name='mailing_clients', verbose_name='клиенты рассылки')

    owner = models.ForeignKey(User, related_name='mailing_owner', on_delete=models.CASCADE,
                              **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.name

    class Meta:

        permissions = [
            ('change_status', 'Can change status of mailing'),
        ]

        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('next_sending',)


class MailingTry(models.Model):
    last_try = models.DateTimeField(auto_now=True, help_text='дата и время последней попытки',
                                    verbose_name='последняя попытка')
    try_status = models.BooleanField(default=False, verbose_name='статус попытки')
    email_response = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера')

    mailing = models.ForeignKey(Mailing, **NULLABLE, on_delete=models.CASCADE,
                                related_name='tries_mailing', verbose_name='рассылка попытки')

    owner = models.ForeignKey(User, related_name='mailingtry_owner', on_delete=models.CASCADE,
                              **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
        ordering = ('last_try',)
