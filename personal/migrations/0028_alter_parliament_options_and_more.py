# Generated by Django 5.0.1 on 2024-02-20 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0027_alter_classmodel_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="parliament",
            options={
                "ordering": ["id"],
                "verbose_name": "Парламент",
                "verbose_name_plural": "Парламенты",
            },
        ),
        migrations.AlterModelOptions(
            name="retiredteachers",
            options={
                "ordering": ["id"],
                "verbose_name": "Учитель в отставке",
                "verbose_name_plural": "Учителя в отставке",
            },
        ),
        migrations.AlterModelOptions(
            name="schedulesmodel",
            options={
                "ordering": ["class_name", "-time_create", "id"],
                "verbose_name": "Расписание",
                "verbose_name_plural": "Расписания",
            },
        ),
        migrations.AlterModelOptions(
            name="teachers",
            options={
                "ordering": ["id"],
                "verbose_name": "Учитель",
                "verbose_name_plural": "Учителя",
            },
        ),
        migrations.AlterField(
            model_name="schedulesmodel",
            name="time_create",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Время создания"
            ),
        ),
        migrations.AlterField(
            model_name="schedulesmodel",
            name="time_update",
            field=models.DateTimeField(auto_now=True, verbose_name="Время обновления"),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="school_class",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="personal.classmodel",
                verbose_name="Класс",
            ),
        ),
    ]
