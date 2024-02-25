# Generated by Django 5.0.1 on 2024-01-21 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0010_remove_personalmodel_class_teacher_of"),
    ]

    operations = [
        migrations.AddField(
            model_name="classmodel",
            name="class_schedule",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="personal.classmodel",
                verbose_name="Расписание",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="classmodel",
            name="class_name",
            field=models.CharField(
                max_length=3, unique=True, verbose_name="Название класса"
            ),
        ),
        migrations.AlterField(
            model_name="schedulesmodel",
            name="class_name",
            field=models.CharField(max_length=3, verbose_name="Название класса"),
        ),
    ]