import secrets

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def send_email_verification_message(self, user):
    user.is_active = False
    token = secrets.token_hex(16)
    user.token = token
    user.save()

    host = self.request.get_host()
    link = f"http://{host}/users/email-confirm/{token}/"
    msg = (f'Здравствуйте, для подтверждения почты и регистрации на сайте перейдите по ссылке ниже.\n'
           f'{link}\n'
           f'Если вы не регистрировались на сайте, не переходите по ссылке.')

    send_mail(
        subject='Подтверждение почты для регистрации на сайте управления рассылками',
        message=msg,
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email],

    )
