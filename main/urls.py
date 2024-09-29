from django.urls import path

from main.apps import MainConfig
from main.views import IndexTemplate

app_name = MainConfig.name

urlpatterns = [
    path('', IndexTemplate.as_view(), name='index'),
]
