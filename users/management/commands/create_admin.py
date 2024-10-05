import os

from django.contrib.auth.models import Group
from dotenv import load_dotenv
from django.core.management import BaseCommand
from config.settings import BASE_DIR
from users.models import User

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
        )
        user.set_password(os.getenv('ADMIN_PASSWORD'))

        user_group = Group.objects.get(name='admin')
        user_group.user_set.add(user)

        user.save()
