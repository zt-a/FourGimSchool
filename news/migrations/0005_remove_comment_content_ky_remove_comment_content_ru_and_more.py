# Generated by Django 5.0.1 on 2024-02-23 16:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_comment_content_ky_comment_content_ru_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="content_ky",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="content_ru",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="news_ky",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="news_ru",
        ),
    ]
