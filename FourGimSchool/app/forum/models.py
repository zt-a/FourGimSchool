from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блогов'
        verbose_name_plural = 'Категории блогов'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forum_post_comments',
                               verbose_name=_("Автор комментария"))
    content = models.TextField(verbose_name=_("Текст комментария"))
    time_create = models.DateTimeField(verbose_name=_('Время создание'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновление'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return _(f"Комментарий от: {self.author.username} на {self.blog.title}")

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='forum_post_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forum_post_likes')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        unique_together = ('post', 'user')


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forum_posts')
    categories = models.ManyToManyField(Category)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='forum_likes', blank=True)
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'id']
