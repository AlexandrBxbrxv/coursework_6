import os
import sys

from django.apps import AppConfig

from main.scheduler import run_scheduler


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        if 'runserver' in sys.argv and os.environ.get('RUN_MAIN') == 'true':
            run_scheduler()
