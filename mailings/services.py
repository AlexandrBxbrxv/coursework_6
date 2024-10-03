from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_mailing(mailing):
    send_mail(
        subject=mailing.message.topic,
        message=mailing.message.body,
        from_email=EMAIL_HOST_USER,
        recipient_list=[client.email for client in mailing.clients],
    )
