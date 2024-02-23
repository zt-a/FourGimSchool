from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactNewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contact_news"
    verbose_name = _("Новостная рассылка")
    verbose_name_plural = _("Новостные рассылки")
