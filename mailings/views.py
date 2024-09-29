from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from mailings.forms import MessageForm
from mailings.models import Message


# CRUD для MESSAGE
class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_create')


class MessageList(ListView):
    model = Message

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Сообщения'
        return context_data
