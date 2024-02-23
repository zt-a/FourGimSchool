from django.db import models
from django.utils.translation import gettext_lazy as _


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    description = models.CharField(max_length=50, verbose_name=_('Описание'), default=_('Школа гимназии номер - 4'))
    image = models.ImageField(upload_to='gallery/images/', verbose_name=_('Изображение'))

    time_create = models.DateTimeField(verbose_name=_('Время создания'), auto_now_add=True, null=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновления'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Галерея')
        verbose_name_plural = _('Галерей')
        ordering = ['-time_create', 'is_published']
