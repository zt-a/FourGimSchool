from django.apps import AppConfig


class EventConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "event"
    verbose_name = 'Событии'
    verbose_name_plural = 'Событии'
