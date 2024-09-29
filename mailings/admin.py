from django.contrib import admin

from mailings.models import Message, Mailing, Client, MailingTry


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('topic', 'body',)
    search_fields = ('topic',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_sending', 'interval', 'status', 'message',)
    list_filter = ('message',)
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name',)
    search_fields = ('full_name',)


@admin.register(MailingTry)
class MailingTryAdmin(admin.ModelAdmin):
    list_display = ('try_number', 'last_try', 'try_status', 'try_count',)
    list_filter = ('try_status',)
    search_fields = ('try_number',)
