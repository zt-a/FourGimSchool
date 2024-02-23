from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_news_comments_count(sender, instance, **kwargs):
    # Обновление comments_count при создании или удалении комментариев
    news = instance.news
    news.comments_count = Comment.objects.filter(news=news, is_published=True).count()
    news.save()