from django.db import models
from django.utils.text import slugify


class History(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    date = models.DateTimeField(verbose_name='Дата и время')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(upload_to='history_images/', verbose_name='Изображение')
    files = models.ManyToManyField('MediaFiles', related_name='histories', verbose_name='видео или файлы')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'


class MediaFiles(models.Model):
    file = models.FileField(upload_to='history_media_files/')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return str(self.file)
