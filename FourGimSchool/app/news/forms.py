from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Введите сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control w100',
        'placeholder': 'Введите комментарий',
        'name': 'message',
        'id': 'message',
        'cols': '30',
        'rows': '9',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Введите сообщение'"
    }))

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control w100',
                'placeholder': 'Введите комментарий',
                'name': 'message',
                'id': 'message',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите сообщение'"
            }),
        }
