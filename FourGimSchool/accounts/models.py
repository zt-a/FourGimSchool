from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('Номер телефона'))
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True,
                                      verbose_name=_('Изображение профиля'))
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    birthdate = models.DateField(null=True, blank=True, verbose_name=_('Дата рождения'))

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    bio = models.TextField(blank=True, null=True, verbose_name=_('Биография'))
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Адрес'))

    # Другие поля профиля

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
