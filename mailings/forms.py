from django.forms import ModelForm, BooleanField

from mailings.models import Message, Client, Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner', 'last_sending',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        # Устанавливаем queryset для поля clients, чтобы показывались только клиенты текущего пользователя
        self.fields['clients'].queryset = Client.objects.filter(owner=user)


class MailingManagerForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('status',)
