# Generated by Django 5.0.1 on 2024-01-24 16:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="history",
            options={"verbose_name": "История", "verbose_name_plural": "Истории"},
        ),
    ]
