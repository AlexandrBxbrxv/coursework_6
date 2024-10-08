from django.urls import path
from mailings.apps import MailingsConfig

from mailings.views import MessageCreate, MessageList, MessageDetail, MessageUpdate, MessageDelete, ClientCreate, \
    ClientList, ClientDetail, ClientUpdate, ClientDelete, MailingCreate, MailingList, MailingDetail, MailingUpdate, \
    MailingDelete, MailingTryList, MailingTryDetail

app_name = MailingsConfig.name


urlpatterns = [
    path('message/create/', MessageCreate.as_view(), name='message_create'),
    path('message/list/', MessageList.as_view(), name='message_list'),
    path('message/detail/<int:pk>/', MessageDetail.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdate.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDelete.as_view(), name='message_delete'),

    path('client/create/', ClientCreate.as_view(), name='client_create'),
    path('client/list/', ClientList.as_view(), name='client_list'),
    path('client/detail/<int:pk>/', ClientDetail.as_view(), name='client_detail'),
    path('client/update/<int:pk>/', ClientUpdate.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDelete.as_view(), name='client_delete'),

    path('mailing/create/', MailingCreate.as_view(), name='mailing_create'),
    path('mailing/list/', MailingList.as_view(), name='mailing_list'),
    path('mailing/detail/<int:pk>/', MailingDetail.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>/', MailingUpdate.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>/', MailingDelete.as_view(), name='mailing_delete'),

    path('mailingtry/list/', MailingTryList.as_view(), name='mailingtry_list'),
    path('mailingtry/detail/<int:pk>/', MailingTryDetail.as_view(), name='mailingtry_detail'),
]
