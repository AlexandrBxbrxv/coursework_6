from django.forms import ModelForm

from mailings.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
