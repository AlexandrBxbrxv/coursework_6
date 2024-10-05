from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailings.forms import MessageForm, ClientForm, MailingForm, MailingManagerForm
from mailings.models import Message, Client, Mailing, MailingTry


# CRUD для Message ##################################################
class MessageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    permission_required = 'mailings.add_message'
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание сообщения'
        return context_data


class MessageList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Message
    permission_required = 'mailings.view_message'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Сообщения'
        user = self.request.user
        if user.is_superuser:
            return context_data
        users_items = []
        for item in context_data.get('object_list'):
            if user == item.owner:
                users_items.append(item)
        context_data['object_list'] = users_items
        return context_data


class MessageDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Message
    permission_required = 'mailings.view_message'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности сообщения'
        return context_data


class MessageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'mailings.change_message'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_success_url(self):
        return reverse('mailings:message_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование сообщения'
        return context_data


class MessageDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Message
    permission_required = 'mailings.delete_message'
    success_url = reverse_lazy('mailings:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление сообщения'
        return context_data


# CRUD для Client ###################################################
class ClientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailings.add_client'
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание клиента'
        return context_data


class ClientList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    permission_required = 'mailings.view_client'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Клиенты'
        user = self.request.user
        if user.is_superuser:
            return context_data
        users_items = []
        for item in context_data.get('object_list'):
            if user == item.owner:
                users_items.append(item)
        context_data['object_list'] = users_items
        return context_data


class ClientDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    permission_required = 'mailings.view_client'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности клиента'
        return context_data


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailings.change_client'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_success_url(self):
        return reverse('mailings:client_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование клиента'
        return context_data


class ClientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'mailings.delete_client'
    success_url = reverse_lazy('mailings:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление клиента'
        return context_data


# CRUD для Mailing ##################################################
class MailingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailings.add_mailing'
    success_url = reverse_lazy('mailings:mailing_create')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание рассылки'
        return context_data


class MailingList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    permission_required = 'mailings.view_mailing'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Рассылки'
        user = self.request.user
        if user.is_superuser or user.has_perm('mailings.change_status'):
            return context_data
        users_items = []
        for item in context_data.get('object_list'):
            if user == item.owner:
                users_items.append(item)
        context_data['object_list'] = users_items
        return context_data


class MailingDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    permission_required = 'mailings.view_mailing'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.has_perm('mailings.change_status'):
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности рассылки'
        return context_data


class MailingUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    permission_required = 'mailings.change_mailing'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.has_perm('mailings.change_status'):
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingForm
        if user.has_perm('mailings.change_status'):
            return MailingManagerForm
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('mailings:mailing_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование рассылки'
        return context_data


class MailingDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'mailings.delete_mailing'
    success_url = reverse_lazy('mailings:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление рассылки'
        return context_data


# Read для MailingTry ###############################################
class MailingTryList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MailingTry
    permission_required = 'mailings.view_mailingtry'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Попытки рассылок'
        user = self.request.user
        if user.is_superuser:
            return context_data
        users_items = []
        for item in context_data.get('object_list'):
            if user == item.owner:
                users_items.append(item)
        context_data['object_list'] = users_items
        return context_data


class MailingTryDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = MailingTry
    permission_required = 'mailing.view_mailingtry'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Подробности попытки'
        return context_data
