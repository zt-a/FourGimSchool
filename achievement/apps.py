from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AchievementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "achievement"
    verbose_name = _('Достижение')
    verbose_name_plural = _('Достижении')
