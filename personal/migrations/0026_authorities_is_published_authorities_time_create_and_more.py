# Generated by Django 5.0.1 on 2024-02-02 17:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0025_authorities_parliament_retiredteachers_teachers"),
    ]

    operations = [
        migrations.AddField(
            model_name="authorities",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="authorities",
            name="time_create",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="authorities",
            name="time_update",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
        migrations.AddField(
            model_name="parliament",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="parliament",
            name="time_create",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="parliament",
            name="time_update",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
        migrations.AddField(
            model_name="retiredteachers",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="retiredteachers",
            name="time_create",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="retiredteachers",
            name="time_update",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
        migrations.AddField(
            model_name="teachers",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="teachers",
            name="time_create",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teachers",
            name="time_update",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата последнего обновления"
            ),
        ),
    ]
