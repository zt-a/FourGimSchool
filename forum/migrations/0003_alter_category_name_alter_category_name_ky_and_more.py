# Generated by Django 5.0.1 on 2024-02-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0002_category_name_ky_category_name_ru_comment_content_ky_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_ky",
            field=models.CharField(max_length=100, null=True, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_ru",
            field=models.CharField(max_length=100, null=True, verbose_name="Название"),
        ),
    ]
