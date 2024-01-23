from django.apps import AppConfig


class ArchiveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "archive"
    verbose_name = 'Документ'
    verbose_name_plural = 'Архив документов'
