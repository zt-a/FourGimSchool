# Generated by Django 5.0.1 on 2024-01-21 13:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "personal",
            "0002_remove_classmodel_schedule_alter_journalmodel_grade_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="classmodel",
            name="slug",
            field=models.SlugField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name="Slug"
            ),
        ),
    ]