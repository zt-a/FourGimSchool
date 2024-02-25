# Generated by Django 5.0.1 on 2024-01-30 17:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Категория блогов",
                "verbose_name_plural": "Категории блогов",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Контент")),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создание"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновление"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forum_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("categories", models.ManyToManyField(to="forum.category")),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="forum_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "ordering": ["-time_create", "id"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="Текст комментария")),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создание"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновление"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forum_post_comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор комментария",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="forum.post",
                        verbose_name="Пост",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forum_post_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forum_post_likes",
                        to="forum.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лайк",
                "verbose_name_plural": "Лайки",
                "unique_together": {("post", "user")},
            },
        ),
    ]
