# Generated by Django 5.0.1 on 2024-02-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0003_alter_gallery_options_alter_gallery_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallery",
            name="description_ky",
            field=models.CharField(
                default="Your default description",
                max_length=50,
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AddField(
            model_name="gallery",
            name="description_ru",
            field=models.CharField(
                default="Your default description",
                max_length=50,
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AddField(
            model_name="gallery",
            name="title_ky",
            field=models.CharField(max_length=255, null=True, verbose_name="Заголовок"),
        ),
        migrations.AddField(
            model_name="gallery",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Заголовок"),
        ),
    ]
