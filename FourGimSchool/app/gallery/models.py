from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=50, verbose_name='Описание', default='Your default description')
    image = models.ImageField(upload_to='gallery/images/', verbose_name='Изображение', default='')

    time_create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True, null=True)
    time_update = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерей'
        ordering = ['-time_create', 'is_published']
