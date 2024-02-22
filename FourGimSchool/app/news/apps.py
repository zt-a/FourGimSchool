from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"
    verbose_name = _('Новость')
    verbose_name_plural = _('Новости')

    def ready(self):
        import news.signals