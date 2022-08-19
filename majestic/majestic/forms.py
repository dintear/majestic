from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fullname', 'user_phone', 'user_email', 'message', 'checked']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'message-form-info__field',
                                                'placeholder': 'Полное имя'}),
            'user_phone': forms.TextInput(attrs={'class': 'message-form-info__field',
                                                'type': 'tel',
                                                'placeholder': 'Номер телефона'}),
            'user_email': forms.TextInput(attrs={'class': 'message-form-info__field',
                                                'type': 'email',
                                                'placeholder': 'Адрес почты'}),
            'message': forms.Textarea(attrs={'class': 'message-form-text__textarea',
                                                'placeholder': 'Ваше сообщение или вопрос...',
                                                'cols': '', 'rows': ''}),
        }