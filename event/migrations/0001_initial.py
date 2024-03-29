# Generated by Django 5.0.1 on 2024-01-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                ("slug", models.SlugField(null=True, unique=True, verbose_name="URL")),
                ("content", models.TextField(verbose_name="Контент")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="event/images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Время обновления"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
            ],
            options={
                "verbose_name": "Событие",
                "verbose_name_plural": "Событии",
                "ordering": ["-time_create", "is_published"],
            },
        ),
    ]
