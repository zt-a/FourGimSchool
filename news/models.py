from django.core.mail import send_mail
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.conf import settings

from contact_news.models import Contact
from django.utils.translation import gettext_lazy as _

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    content = models.TextField(verbose_name=_('Контент'))
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(verbose_name=_('Фотография'), upload_to='photos/news/%Y/%m/%d/')
    video = models.FileField(verbose_name=_('Видео'), upload_to='videos/news/%Y/%m/%d/', null=True, blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'avi', 'flm', 'ogg'])])
    audio = models.FileField(verbose_name=_('Аудио'), upload_to='musics/news/%Y/%m/%d/', null=True, blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MP3', 'mp3', 'ogg', 'wav', 'tac', 'adx', 'flac', 'wma', 'aac',
                                                     'opus', 'm4a', 'ape', 'pac', 'flac'])])
    file = models.FileField(verbose_name='Файл', upload_to='files/news/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Автор новости"))
    likes = models.IntegerField(default=0, verbose_name=_("Количество лайков"))
    comments_count = models.IntegerField(default=0, verbose_name=_("Количество комментариев"))
    time_create = models.DateTimeField(verbose_name=_('Время создание'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновление'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:news_post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        ordering = ['-time_create', 'id']
        unique_together = ('slug', 'author')


@receiver(post_save, sender=News)
def send_newsletter_on_new_news(sender, instance, created, **kwargs):
    global url
    if settings.DEBUG:
        url = '127.0.0.1:8000' + reverse('news:news_detail', args=[str(instance.slug)])
    else:
        settings.MAIN_HOSTS + reverse('news:news_detail', args=[str(instance.slug)])
    if created:  # Отправлять рассылку только при создании новой новости, а не при обновлении
        subject = _('Новая новость: {}'.format(instance.title))
        message = _('У нас есть новая новость! "{}" \n\n{}\n\n{}'.format(
            instance.title,
            instance.content,
            url
        ))
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = list(Contact.objects.values_list('email', flat=True))

        send_mail(subject, message, from_email, recipient_list)




class Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='likes_set', verbose_name=_("Новость"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь"))

    def __str__(self):
        return _(f"{self.user.username} поставил лайк новости: {self.news.title}")

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = _("Лайки")
        unique_together = ('news', 'user')


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name=_("Новость"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Автор комментария"),
                               related_name='news_comments')
    content = models.TextField(verbose_name=_("Текст комментария"))
    time_create = models.DateTimeField(verbose_name=_('Время создание'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновление'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return _(f"Комментарий от: {self.author.username} на {self.news.title}")

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
