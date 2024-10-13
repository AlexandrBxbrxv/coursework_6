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

