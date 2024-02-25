# Generated by Django 5.0.1 on 2024-01-31 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0020_alter_personalmodel_subjects_taught_studentmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="GradesStudents",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "grade",
                    models.IntegerField(
                        choices=[("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)],
                        verbose_name="Оценка ученика",
                    ),
                ),
                (
                    "quarter",
                    models.IntegerField(
                        choices=[("1", 1), ("2", 2), ("3", 3), ("4", 4)],
                        verbose_name="Четверть",
                    ),
                ),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего обновления"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="StudentGrade",
                        to="personal.schedulesmodel",
                        verbose_name="Ученик",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="SubjectGrade",
                        to="personal.schedulesmodel",
                        verbose_name="Предмет",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оценка",
                "verbose_name_plural": "Оценки",
                "ordering": ["quarter", "grade", "subject", "id", "-time_create"],
            },
        ),
    ]
