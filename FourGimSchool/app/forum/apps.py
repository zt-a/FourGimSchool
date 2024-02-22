from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ForumConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "forum"
    verbose_name = _('Форум')
    verbose_name_plural = _('Форумы')
