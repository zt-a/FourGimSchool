from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class CustomUserRegistrationForm(UserCreationForm):
    birthdate = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'single-input',
            'placeholder': 'Введите дату рождения',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "НДата рождения"'
        }),
        label='Дата рождения'
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите номер телефона',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Номер телефона"'
        }),
        label='Номер телефона'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите ваш Email',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Email"'
        }),
        label='Email'
    )
    profile_image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'type': 'file',
            'class': 'single-input form-control',
            'placeholder': 'Выберите файл',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Фото профиля"'
        }),
        label='Фото профиля'
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите ваше имя пользователя',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Имя пользователя"'
        }),
        label='Имя пользователя'
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите ваше имя',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Имя"'
        }),
        label='Имя'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите ваше фамилию',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Фамилия"'
        }),
        label='Фамилия'
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите пароль',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Пароль"'
        }),
        label='Пароль'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите пароль',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Подтвердите пароль"'
        }),
        label='Подтвердите пароль'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'birthdate', 'phone_number',
                  'profile_image', 'password1', 'password2']
        widgets = {
            "phone_number": forms.CharField(max_length=15, required=False, label='Номер телефона'),
            "profile_image": forms.ImageField(required=False, label='Изображение профиля'),

        }

    def __init__(self, *args, **kwargs):
        super(CustomUserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.layout = Layout(
            Submit('submit', 'Зарегистрироваться', css_class='genric-btn success')
        )

    def clean(self):
        cleaned_data = super(CustomUserRegistrationForm, self).clean()

        for field_name, field_errors in self.errors.items():
            for error in field_errors:
                self.fields[field_name].widget.attrs['class'] = 'form-control is-invalid text-danger'
                break

        return cleaned_data


class CustomUserAuthenticationForm(AuthenticationForm):
    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя пользователя'}),
    #     label='Имя пользователя'
    # )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите ваше имя пользователя',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Имя пользователя"'
        }),
        label='Имя пользователя'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'single-input',
            'placeholder': 'Введите пароль',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Пароль"'
        }),
        label='Пароль'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'single-input',
                'placeholder': 'Введите ваше имя пользователя',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Имя пользователя"'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'single-input',
                'placeholder': 'Введите пароль',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Пароль"'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.layout = Layout(
            Submit('submit', 'Войти', css_class='generic-btn success')
        )

    def clean(self):
        cleaned_data = super(CustomUserAuthenticationForm, self).clean()

        for field_name, field_errors in self.errors.items():
            for error in field_errors:
                self.fields[field_name].widget.attrs['class'] = 'form-control is-invalid text-danger'
                break

        return cleaned_data
