from datetime import datetime

from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
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

            subject = mailing.message.topic
            message = mailing.message.body
            from_email = EMAIL_HOST_USER
            recipient_list = [client.email for client in mailing.clients.all()]

            mail_2 = (f'---------------------------------------\n'
                      f'{subject}\n'
                      f'{message}\n'
                      f'{from_email}\n'
                      f'{recipient_list}\n'
                      f'---------------------------------------')
            print(mail_2)

            if subject and message and from_email:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
            else:
                print('error')
