import logging

from apscheduler.schedulers.background import BackgroundScheduler
from config import settings
from apscheduler.triggers.cron import CronTrigger


logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)


def run_scheduler():
    from django_apscheduler.jobstores import DjangoJobStore
    from main.services import send_mailing

    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        send_mailing,
        trigger=CronTrigger(second="*/10"),
        id="my_job",
        max_instances=1,
        replace_existing=True,
    )

    scheduler.start()
    print('Запущен django apscheduler')
