from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailings.forms import MessageForm, ClientForm
from mailings.models import Message, Client


# CRUD для Message ##################################################
class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_create')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание сообщения'
        return context_data


class MessageList(ListView):
    model = Message

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Сообщения'
        return context_data


class MessageDetail(DetailView):
    model = Message

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности сообщения'
        return context_data


class MessageUpdate(UpdateView):
    model = Message
    form_class = MessageForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование сообщения'
        return context_data

    def get_success_url(self):
        return reverse('mailings:message_detail', args=[self.kwargs.get('pk')])


class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление сообщения'
        return context_data


# CRUD для Client ###################################################
class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_create')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание клиента'
        return context_data


class ClientList(ListView):
    model = Client

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Клиенты'
        return context_data


class ClientDetail(DetailView):
    model = Client

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности клиента'
        return context_data


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailings:client_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование клиента'
        return context_data


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление клиента'
        return context_data
