# Generated by Django 5.0.1 on 2024-02-20 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_category_name_ky_category_name_ru_comment_content_ky_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(to="blog.category", verbose_name="Категория"),
        ),
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                related_name="post_likes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Лайк",
            ),
        ),
    ]
