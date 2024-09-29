from django.contrib import admin

from mailings.models import Message, Mailing, Client


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('topic', 'body',)
    search_fields = ('topic',)


@admin.register(Mailing)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_sending', 'interval', 'status', 'message',)
    list_filter = ('message',)
    search_fields = ('name',)


@admin.register(Client)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name',)
    search_fields = ('full_name',)
