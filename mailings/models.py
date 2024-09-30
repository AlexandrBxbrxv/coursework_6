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


class MailingTry(models.Model):
    try_count = models.PositiveIntegerField(default=0, verbose_name='попыток рассылки')
    last_try = models.DateField(help_text='дата и время последней попытки', verbose_name='последняя попытка')
    try_status = models.BooleanField(default=False, verbose_name='статус попытки')
    email_response = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера')
    try_number = models.CharField(max_length=100, verbose_name='номер попытки')

    def __str__(self):
        return self.try_number

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
        ordering = ('try_number',)


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='фио')
    comment = models.TextField(**NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):

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

    name = models.CharField(max_length=100, verbose_name='название')
    first_sending = models.DateField(help_text='дата и время первой отправки рассылки', verbose_name='первая отправка')
    interval = models.CharField(max_length=15, choices=INTERVALS, default='month', verbose_name='периодичность')
    status = models.CharField(max_length=15, choices=STATUSES, default='off', verbose_name='статус')

    message = models.ForeignKey(Message, **NULLABLE, on_delete=models.SET_NULL, related_name='mailing_message',
                                verbose_name='сообщение рассылки')

    clients = models.ManyToManyField(Client, related_name='mailing_clients', verbose_name='клиенты рассылки')

    mailing_try = models.ForeignKey(MailingTry, **NULLABLE, on_delete=models.SET_NULL,
                                    related_name='mailing_tries', verbose_name='попытки рассылки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
