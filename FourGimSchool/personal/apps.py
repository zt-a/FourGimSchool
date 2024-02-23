from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PersonalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "personal"
    verbose_name = _('Персонал')
    verbose_name_plural = _('Персоналы')
