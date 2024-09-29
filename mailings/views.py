from django.urls import reverse_lazy
from django.views.generic import CreateView

from mailings.forms import MessageForm
from mailings.models import Message


# CRUD для MESSAGE
class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_create')
