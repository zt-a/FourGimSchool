from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class History(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    date = models.DateTimeField(verbose_name=_('Дата и время'))
    description = models.TextField(verbose_name=_('Описание'), null=True, blank=True)
    content = models.TextField(verbose_name=_('Контент'))
    image = models.ImageField(upload_to='history_images/', verbose_name=_('Изображение'))
    files = models.ManyToManyField('MediaFiles', related_name='histories', verbose_name=_('видео или файлы'))

    time_create = models.DateTimeField(verbose_name=_('Время создание'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновление'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('История')
        verbose_name_plural = _('Истории')


class MediaFiles(models.Model):
    file = models.FileField(upload_to='history_media_files/')

    time_create = models.DateTimeField(verbose_name=_('Время создание'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновление'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return str(self.file)
