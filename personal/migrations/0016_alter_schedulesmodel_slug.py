# Generated by Django 5.0.1 on 2024-01-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0015_alter_schedulesmodel_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedulesmodel",
            name="slug",
            field=models.SlugField(max_length=10, verbose_name="URL"),
        ),
    ]
