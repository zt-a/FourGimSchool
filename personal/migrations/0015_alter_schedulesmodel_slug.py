# Generated by Django 5.0.1 on 2024-01-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0014_alter_schedulesmodel_class_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedulesmodel",
            name="slug",
            field=models.SlugField(max_length=10, unique=True, verbose_name="URL"),
        ),
    ]
