from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email',)
        labels = {
            'email': False,
        }
        widgets = {
            'email': forms.TextInput(attrs={
                'type': 'email',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Введите ваш email',
                'required': True
            })
        }


class ContactFormPlus(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email',)
        labels = {
            'email': False,
        }
        widgets = {
            'email': forms.TextInput(attrs={
                'type': 'email',
                'name': 'email',
                'id': 'email',
                'class': 'form-control',
                'onfocus': '"this.placeholder = ''"',
                'onblur': '"this.placeholder=\'Введите email\'"',
                'placeholder': 'Введите email',
                'required': True
            })
        }
