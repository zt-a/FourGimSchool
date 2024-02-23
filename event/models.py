from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    slug = models.SlugField(unique=True, verbose_name='URL')
    content = models.TextField(verbose_name=_('Контент'))
    image = models.ImageField(upload_to='event/images/', verbose_name=_('Изображение'), null=True, blank=True)
    time_create = models.DateTimeField(verbose_name=_('Время создания'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновления'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event:event_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Событие')
        verbose_name_plural = _('Событии')
        ordering = ['-time_create', 'is_published']


