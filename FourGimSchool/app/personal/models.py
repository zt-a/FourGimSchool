from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid
from autoslug import AutoSlugField


class SubjectModel(models.Model):
    subject_name = models.CharField(max_length=255, verbose_name='Название предмета')

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class PersonalModel(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(unique=True, verbose_name='Email')
    subjects_taught = models.ManyToManyField(SubjectModel, verbose_name='Преподаваемые предметы или должность')
    address = models.TextField(verbose_name='Адрес')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    work_experience = models.TextField(verbose_name='Опыт работы')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст')

    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True,
                                        verbose_name='Фото профиля')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персоналы'
        ordering = ['-work_experience', '-age', '-time_create', 'id']


class SchedulesModel(models.Model):
    class_name = models.CharField(max_length=10, verbose_name='Название класса')
    slug = AutoSlugField(populate_from='class_name', max_length=10, unique=True, db_index=True, verbose_name='URL')

    day1example1 = models.CharField(max_length=30, verbose_name='День 1 урок 1')
    day1example2 = models.CharField(max_length=30, verbose_name='День 1 урок 2')
    day1example3 = models.CharField(max_length=30, verbose_name='День 1 урок 3')
    day1example4 = models.CharField(max_length=30, verbose_name='День 1 урок 4')
    day1example5 = models.CharField(max_length=30, verbose_name='День 1 урок 5')
    day1example6 = models.CharField(max_length=30, verbose_name='День 1 урок 6')

    day2example1 = models.CharField(max_length=30, verbose_name='День 2 урок 1')
    day2example2 = models.CharField(max_length=30, verbose_name='День 2 урок 2')
    day2example3 = models.CharField(max_length=30, verbose_name='День 2 урок 3')
    day2example4 = models.CharField(max_length=30, verbose_name='День 2 урок 4')
    day2example5 = models.CharField(max_length=30, verbose_name='День 2 урок 5')
    day2example6 = models.CharField(max_length=30, verbose_name='День 2 урок 6')

    day3example1 = models.CharField(max_length=30, verbose_name='День 3 урок 1')
    day3example2 = models.CharField(max_length=30, verbose_name='День 3 урок 2')
    day3example3 = models.CharField(max_length=30, verbose_name='День 3 урок 3')
    day3example4 = models.CharField(max_length=30, verbose_name='День 3 урок 4')
    day3example5 = models.CharField(max_length=30, verbose_name='День 3 урок 5')
    day3example6 = models.CharField(max_length=30, verbose_name='День 3 урок 6')

    day4example1 = models.CharField(max_length=30, verbose_name='День 4 урок 1')
    day4example2 = models.CharField(max_length=30, verbose_name='День 4 урок 2')
    day4example3 = models.CharField(max_length=30, verbose_name='День 4 урок 3')
    day4example4 = models.CharField(max_length=30, verbose_name='День 4 урок 4')
    day4example5 = models.CharField(max_length=30, verbose_name='День 4 урок 5')
    day4example6 = models.CharField(max_length=30, verbose_name='День 4 урок 6')

    day5example1 = models.CharField(max_length=30, verbose_name='День 5 урок 1')
    day5example2 = models.CharField(max_length=30, verbose_name='День 5 урок 2')
    day5example3 = models.CharField(max_length=30, verbose_name='День 5 урок 3')
    day5example4 = models.CharField(max_length=30, verbose_name='День 5 урок 4')
    day5example5 = models.CharField(max_length=30, verbose_name='День 5 урок 5')
    day5example6 = models.CharField(max_length=30, verbose_name='День 5 урок 6')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return f'{self.class_name} {self.slug}'

    def get_absolute_url(self):
        return reverse('schedule', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.class_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Расписания'
        verbose_name_plural = 'Расписании'
        ordering = ['class_name', '-time_create', 'id']


class ClassModel(models.Model):
    class_name = models.CharField(max_length=3, verbose_name='Название класса', unique=True)
    class_teacher = models.OneToOneField(PersonalModel, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='Классный руководитель')
    class_schedule = models.ForeignKey(SchedulesModel, on_delete=models.CASCADE, verbose_name='Расписание', null=True,
                                       blank=True)
    classroom_number = models.CharField(max_length=10, verbose_name='Номер кабинета', null=True, blank=True, )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    # Добавляем поле slug
    slug = AutoSlugField(populate_from='class_name', unique=True, default=uuid.uuid4, editable=True,
                         verbose_name='Slug')

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.class_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['class_name', '-time_create', 'id']


class StudentModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    passport_number = models.CharField(max_length=9, unique=True, verbose_name="Номер паспорта (ID1234567)")
    inn = models.CharField(max_length=14, unique=True, verbose_name="Персональный номер (ИНН)")
    citizenship = models.CharField(max_length=50, verbose_name="Гражданство")
    address = models.TextField(verbose_name="Адрес проживания")
    school_class = models.ForeignKey(ClassModel, on_delete=models.SET_NULL, null=True)

    gender_choices = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, verbose_name="Пол")

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['id', 'date_of_birth']


class GradesStudents(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, verbose_name='Ученик',
                                related_name='StudentGrade')
    grade_choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    grade = models.IntegerField(choices=grade_choices, verbose_name='Оценка ученика')

    quarter_choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ]
    quarter = models.IntegerField(choices=quarter_choices, verbose_name='Четверть')
    subject = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, related_name='SubjectGrade',
                                verbose_name='Предмет', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.student.__str__()

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['quarter', 'grade', 'subject', 'id', '-time_create']


class Authorities(models.Model):
    person = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name='authorities_person')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = 'Начальство'
        verbose_name_plural = 'Начальство'
        ordering = ['id']


class Teachers(models.Model):
    person = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name='teachers_person')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = 'Учителя '
        verbose_name_plural = 'Учителя'
        ordering = ['id']


class Parliament(models.Model):
    person = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='parliaments_person')

    profile_picture = models.ImageField(upload_to='parliaments_person_pictures/', verbose_name='Фото профиля')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = 'Парламент '
        verbose_name_plural = 'Парламенты'
        ordering = ['id']


class RetiredTeachers(models.Model):
    person = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name='RetiredTeachers_person')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = 'Учителя в отставке '
        verbose_name_plural = 'Учителя в отставке'
        ordering = ['id']
