# Generated by Django 5.0.1 on 2024-01-21 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClassModel",
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
                    "class_name",
                    models.CharField(max_length=10, verbose_name="Название класса"),
                ),
                ("schedule", models.TextField(verbose_name="Расписание класса")),
                (
                    "classroom_number",
                    models.CharField(max_length=10, verbose_name="Номер кабинета"),
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
            ],
        ),
        migrations.CreateModel(
            name="SubjectModel",
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
                    "subject_name",
                    models.CharField(max_length=255, verbose_name="Название предмета"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JournalModel",
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
                ("date", models.DateField(verbose_name="Дата оценки")),
                (
                    "grade",
                    models.PositiveIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "quarter",
                    models.CharField(
                        choices=[
                            ("1", "Первая четверть"),
                            ("2", "Вторая четверть"),
                            ("3", "Третья четверть"),
                            ("4", "Четвёртая четверть"),
                        ],
                        max_length=1,
                        verbose_name="Четверть",
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
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
                    "student_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="class_journals",
                        to="personal.classmodel",
                        verbose_name="Класс",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="classmodel",
            name="class_journal",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="personal.journalmodel",
                verbose_name="Журнал класса",
            ),
        ),
        migrations.CreateModel(
            name="PersonalModel",
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
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=255, verbose_name="Фамилия")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                ("address", models.TextField(verbose_name="Адрес")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Номер телефона"),
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
                ("work_experience", models.TextField(verbose_name="Опыт работы")),
                ("birthday", models.DateField(verbose_name="Дата рождения")),
                ("age", models.IntegerField(verbose_name="Возраст")),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pictures/",
                        verbose_name="Фото профиля",
                    ),
                ),
                (
                    "class_teacher_of",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="class_teacher_personal",
                        to="personal.classmodel",
                        verbose_name="Учитель класса",
                    ),
                ),
                (
                    "subjects_taught",
                    models.ManyToManyField(
                        to="personal.subjectmodel",
                        verbose_name="Преподаваемые предметы",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="classmodel",
            name="class_teacher",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="personal.personalmodel",
                verbose_name="Классный руководитель",
            ),
        ),
        migrations.CreateModel(
            name="StudentsModel",
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
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=255, verbose_name="Фамилия")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                ("address", models.TextField(verbose_name="Адрес")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Номер телефона"),
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
                ("birthday", models.DateField(verbose_name="Дата рождения")),
                ("age", models.IntegerField(verbose_name="Возраст")),
                (
                    "student_class",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="students",
                        to="personal.classmodel",
                        verbose_name="Класс",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="journalmodel",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="personal.studentsmodel",
                verbose_name="Ученик",
            ),
        ),
        migrations.AddField(
            model_name="journalmodel",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="personal.subjectmodel",
                verbose_name="Предмет",
            ),
        ),
    ]
