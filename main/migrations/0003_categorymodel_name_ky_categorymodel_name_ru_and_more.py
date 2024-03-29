# Generated by Django 5.0.1 on 2024-02-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_feedbackmodel_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="categorymodel",
            name="name_ky",
            field=models.CharField(max_length=100, null=True, verbose_name="Название"),
        ),
        migrations.AddField(
            model_name="categorymodel",
            name="name_ru",
            field=models.CharField(max_length=100, null=True, verbose_name="Название"),
        ),
        migrations.AddField(
            model_name="rulesmodel",
            name="description_ky",
            field=models.TextField(null=True, verbose_name="Описание правило"),
        ),
        migrations.AddField(
            model_name="rulesmodel",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Описание правило"),
        ),
        migrations.AddField(
            model_name="rulesmodel",
            name="title_ky",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Название правило"
            ),
        ),
        migrations.AddField(
            model_name="rulesmodel",
            name="title_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Название правило"
            ),
        ),
    ]
