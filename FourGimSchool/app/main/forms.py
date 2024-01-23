from django import forms
from .models import *


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Поиск на сайте'}))


class ContactForm(forms.ModelForm):
    subject = forms.CharField(label='Введите тему', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите тему',
        'name': 'subject',
        'id': 'subject',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Введите тему'"
    }))
    name = forms.CharField(label='Введите ваше имя', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control valid',
        'placeholder': 'Введите ваше имя',
        'name': 'name',
        'id': 'name',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Введите ваше имя'"
    }))
    email = forms.EmailField(label='Электронная почта', max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control valid',
        'placeholder': 'Электронная почта',
        'name': 'email',
        'id': 'email',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Электронная почта'"
    }))
    message = forms.CharField(label='Введите сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control w100',
        'placeholder': 'Введите сообщение',
        'name': 'message',
        'id': 'message',
        'cols': '30',
        'rows': '9',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Введите сообщение'"
    }))

    class Meta:
        model = ContactModel
        fields = ['message', 'name', 'email', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Введите ваше имя',
                'name': 'name',
                'id': 'name',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите ваше имя'"
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Электронная почта',
                'name': 'email',
                'id': 'email',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Электронная почта'"
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control w100',
                'placeholder': 'Введите сообщение',
                'name': 'message',
                'id': 'message',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите сообщение'"
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тему',
                'name': 'subject',
                'id': 'subject',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите тему'"
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Имя",
                           widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=100, label="Фамилия",
                              widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Фамилия'}))
    phone_number = forms.CharField(max_length=20, label='Номер телефона',
                                   widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Номер телефона'}))
    email = forms.CharField(max_length=100, label="E-mail",
                            widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Адресс электронный почты'}))
    feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(
        attrs={'type': 'text', 'placeholder': 'Оставьте отзыв', 'rows': '10', 'cols': '30'}))

    class Meta:
        model = FeedbackModel
        fields = ['name', 'surname', 'phone_number', 'email', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Имя'}),
            'surname': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Фамилия'}),
            'phone_number': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Номер телефона'}),
            'email': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Адресс электронный почты'}),
            'feedback': forms.Textarea(
                attrs={'type': 'text', 'placeholder': 'Оставьте отзыв', 'rows': '10', 'cols': '30'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
