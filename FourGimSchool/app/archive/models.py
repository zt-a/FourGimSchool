from django.db import models
from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    pdf_file = models.FileField(upload_to='documents/', verbose_name='Документ (PDF)')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создание'))
    is_published = models.BooleanField(default=True, verbose_name=_('Публикация'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Документ')
        verbose_name_plural = _('Документы')
