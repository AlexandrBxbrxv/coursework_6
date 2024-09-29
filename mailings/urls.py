from django.urls import path
from mailings.apps import MailingsConfig

from mailings.views import MessageCreate, MessageList

app_name = MailingsConfig.name


urlpatterns = [
    path('message/create/', MessageCreate.as_view(), name='message_create'),
    path('message/list/', MessageList.as_view(), name='message_list'),
]
