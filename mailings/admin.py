from django.contrib import admin

from mailings.models import Message, Mailing, Client, MailingTry


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'body', 'owner',)
    list_filter = ('owner',)
    search_fields = ('topic',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first_sending', 'interval', 'status', 'message', 'owner',)
    filter_horizontal = ('clients',)
    list_filter = ('message', 'owner',)
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'owner',)
    list_filter = ('owner',)
    search_fields = ('full_name',)


@admin.register(MailingTry)
class MailingTryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_try', 'try_status', 'mailing', 'owner',)
    list_filter = ('try_status', 'mailing', 'owner',)
    search_fields = ('name',)
