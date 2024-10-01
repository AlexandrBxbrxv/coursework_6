from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailings.forms import MessageForm, ClientForm, MailingForm
from mailings.models import Message, Client, Mailing, MailingTry


# CRUD для Message ##################################################
class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')

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
    success_url = reverse_lazy('mailings:client_list')

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


# CRUD для Mailing ##################################################
class MailingCreate(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_create')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание рассылки'
        return context_data


class MailingList(ListView):
    model = Mailing

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Рассылки'
        return context_data


class MailingDetail(DetailView):
    model = Mailing

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности рассылки'
        return context_data


class MailingUpdate(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailings:mailing_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование рассылки'
        return context_data


class MailingDelete(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление рассылки'
        return context_data


# Read для MailingTry ###############################################
class MailingTryList(ListView):
    model = MailingTry

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Попытки рассылок'
        return context_data


class MailingTryDetail(DetailView):
    model = MailingTry

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности попытки'
        return context_data
