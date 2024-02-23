from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ArchiveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "archive"
    verbose_name = _('Документ')
    verbose_name_plural = _('Архив документов')
