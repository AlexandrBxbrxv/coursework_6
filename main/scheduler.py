import logging
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from apscheduler.triggers.cron import CronTrigger


logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)


def send_mailing():
    import pytz
    from django.core.mail import send_mail
    from config.settings import EMAIL_HOST_USER
    from mailings.models import Mailing

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Mailing.objects.filter(first_sending__lte=current_datetime).filter(
        status__in=['waiting_first', 'send_waiting'])

    for mailing in mailings:
        print(mailing.name)
        send_mail(
            subject=mailing.message.topic,
            message=mailing.message.body,
            from_email=EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.clients.all()],
        )


def run_scheduler():
    from django_apscheduler.jobstores import DjangoJobStore

    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        send_mailing,
        trigger=CronTrigger(minute="*"),
        id="my_job",
        max_instances=1,
        replace_existing=True,
    )

    scheduler.start()
    print('Запущен django apscheduler')
