from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


class SubjectModel(models.Model):
    subject_name = models.CharField(max_length=255, verbose_name=_('Название предмета'))

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = _('Предмет')
        verbose_name_plural = _('Предметы')


class PersonalModel(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=255, verbose_name=_('Фамилия'))
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Отчество"))
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    subjects_taught = models.ManyToManyField('SubjectModel', verbose_name=_('Преподаваемые предметы или должность'))
    address = models.TextField(verbose_name=_('Адрес'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Номер телефона'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))
    work_experience = models.TextField(verbose_name=_('Опыт работы'))
    birthday = models.DateField(verbose_name=_('Дата рождения'))
    age = models.IntegerField(verbose_name=_('Возраст'))

    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True,
                                        verbose_name=_('Фото профиля'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Персонал')
        verbose_name_plural = _('Персоналы')
        ordering = ['-work_experience', '-age', '-time_create', 'id']


class SchedulesModel(models.Model):
    class_name = models.CharField(max_length=10, verbose_name=_('Название класса'))
    slug = AutoSlugField(populate_from='class_name', max_length=10, unique=True, db_index=True, verbose_name=_('URL'))

    day1example1 = models.CharField(max_length=30, verbose_name=_('День 1 урок 1'))
    day1example2 = models.CharField(max_length=30, verbose_name=_('День 1 урок 2'))
    day1example3 = models.CharField(max_length=30, verbose_name=_('День 1 урок 3'))
    day1example4 = models.CharField(max_length=30, verbose_name=_('День 1 урок 4'))
    day1example5 = models.CharField(max_length=30, verbose_name=_('День 1 урок 5'))
    day1example6 = models.CharField(max_length=30, verbose_name=_('День 1 урок 6'))

    day2example1 = models.CharField(max_length=30, verbose_name=_('День 2 урок 1'))
    day2example2 = models.CharField(max_length=30, verbose_name=_('День 2 урок 2'))
    day2example3 = models.CharField(max_length=30, verbose_name=_('День 2 урок 3'))
    day2example4 = models.CharField(max_length=30, verbose_name=_('День 2 урок 4'))
    day2example5 = models.CharField(max_length=30, verbose_name=_('День 2 урок 5'))
    day2example6 = models.CharField(max_length=30, verbose_name=_('День 2 урок 6'))

    day3example1 = models.CharField(max_length=30, verbose_name=_('День 3 урок 1'))
    day3example2 = models.CharField(max_length=30, verbose_name=_('День 3 урок 2'))
    day3example3 = models.CharField(max_length=30, verbose_name=_('День 3 урок 3'))
    day3example4 = models.CharField(max_length=30, verbose_name=_('День 3 урок 4'))
    day3example5 = models.CharField(max_length=30, verbose_name=_('День 3 урок 5'))
    day3example6 = models.CharField(max_length=30, verbose_name=_('День 3 урок 6'))

    day4example1 = models.CharField(max_length=30, verbose_name=_('День 4 урок 1'))
    day4example2 = models.CharField(max_length=30, verbose_name=_('День 4 урок 2'))
    day4example3 = models.CharField(max_length=30, verbose_name=_('День 4 урок 3'))
    day4example4 = models.CharField(max_length=30, verbose_name=_('День 4 урок 4'))
    day4example5 = models.CharField(max_length=30, verbose_name=_('День 4 урок 5'))
    day4example6 = models.CharField(max_length=30, verbose_name=_('День 4 урок 6'))

    day5example1 = models.CharField(max_length=30, verbose_name=_('День 5 урок 1'))
    day5example2 = models.CharField(max_length=30, verbose_name=_('День 5 урок 2'))
    day5example3 = models.CharField(max_length=30, verbose_name=_('День 5 урок 3'))
    day5example4 = models.CharField(max_length=30, verbose_name=_('День 5 урок 4'))
    day5example5 = models.CharField(max_length=30, verbose_name=_('День 5 урок 5'))
    day5example6 = models.CharField(max_length=30, verbose_name=_('День 5 урок 6'))

    time_create = models.DateTimeField(verbose_name=_('Время создания'), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_('Время обновления'), auto_now=True)
    is_published = models.BooleanField(verbose_name=_('Публикация'), default=True)

    def __str__(self):
        return f'{self.class_name} {self.slug}'

    def get_absolute_url(self):
        return reverse('schedule', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.class_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')
        ordering = ['class_name', '-time_create', 'id']


class ClassModel(models.Model):
    class_name = models.CharField(max_length=3, verbose_name=_('Название класса'), unique=True)
    class_teacher = models.OneToOneField('PersonalModel', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name=_('Классный руководитель'))
    class_schedule = models.ForeignKey('SchedulesModel', on_delete=models.CASCADE, verbose_name=_('Расписание'),
                                       null=True,
                                       blank=True)
    classroom_number = models.CharField(max_length=10, verbose_name=_('Номер кабинета'), null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    # Добавляем поле slug
    slug = AutoSlugField(populate_from='class_name', unique=True, editable=True,
                         verbose_name=_('Slug'))

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.class_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = _('Класс')
        verbose_name_plural = _('Классы')
        ordering = ['class_name', '-time_create', 'id']


class StudentModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=100, verbose_name=_("Фамилия"))
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Отчество"))
    date_of_birth = models.DateField(verbose_name=_("Дата рождения"))
    passport_number = models.CharField(max_length=9, unique=True, verbose_name=_("Номер паспорта (ID1234567)"))
    inn = models.CharField(max_length=14, unique=True, verbose_name=_("Персональный номер (ИНН)"))
    citizenship = models.CharField(max_length=50, verbose_name=_("Гражданство"))
    address = models.TextField(verbose_name=_("Адрес проживания"))
    school_class = models.ForeignKey('ClassModel', on_delete=models.SET_NULL, null=True, verbose_name=_("Класс"))

    gender_choices = [
        ('M', _('Мужской')),
        ('F', _('Женский')),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, verbose_name=_("Пол"))

    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

    class Meta:
        verbose_name = _('Ученик')
        verbose_name_plural = _('Ученики')
        ordering = ['id', 'date_of_birth']


class GradesStudents(models.Model):
    student = models.ForeignKey('StudentModel', on_delete=models.CASCADE, verbose_name=_('Ученик'),
                                related_name='StudentGrade')
    grade_choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    grade = models.IntegerField(choices=grade_choices, verbose_name=_('Оценка ученика'))

    quarter_choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ]
    quarter = models.IntegerField(choices=quarter_choices, verbose_name=_('Четверть'))
    subject = models.ForeignKey('SubjectModel', on_delete=models.SET_NULL, related_name='SubjectGrade',
                                verbose_name=_('Предмет'), null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.student.__str__()

    class Meta:
        verbose_name = _('Оценка')
        verbose_name_plural = _('Оценки')
        ordering = ['quarter', 'grade', 'subject', 'id', '-time_create']


class Authorities(models.Model):
    person = models.ForeignKey('PersonalModel', on_delete=models.CASCADE, related_name='authorities_person')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = _('Начальство')
        verbose_name_plural = _('Начальство')
        ordering = ['id']


class Teachers(models.Model):
    person = models.ForeignKey('PersonalModel', on_delete=models.CASCADE, related_name='teachers_person')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = _('Учитель')
        verbose_name_plural = _('Учителя')
        ordering = ['id']


class Parliament(models.Model):
    person = models.ForeignKey('StudentModel', on_delete=models.CASCADE, related_name='parliaments_person')

    profile_picture = models.ImageField(upload_to='parliaments_person_pictures/', verbose_name=_('Фото профиля'))

    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = _('Парламент')
        verbose_name_plural = _('Парламенты')
        ordering = ['id']


class RetiredTeachers(models.Model):
    person = models.ForeignKey('PersonalModel', on_delete=models.CASCADE, related_name='RetiredTeachers_person')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = _('Учитель в отставке')
        verbose_name_plural = _('Учителя в отставке')
        ordering = ['id']
