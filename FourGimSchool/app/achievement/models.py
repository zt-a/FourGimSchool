from django.db import models
from personal.models import ClassModel, SubjectModel, PersonalModel


class BestStudents(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    class_student = models.ForeignKey(ClassModel, on_delete=models.CASCADE, verbose_name='Класс ученика',
                                      related_name='best_students')
    image_student = models.ImageField(upload_to='image_best_student/', verbose_name='Фото ученика')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Лучший ученик'
        verbose_name_plural = 'Лучшие ученики'


class AchievementStudents(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(verbose_name='Описание достижение')
    image_student = models.ImageField(upload_to='image_students/', verbose_name='Фото ученика')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Достижение ученика'
        verbose_name_plural = 'Достижении учеников'


class AchievementPersonal(models.Model):
    personal = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, verbose_name='Учитель')
    description = models.TextField(verbose_name='Описание достижение')

    image_personal = models.ImageField(upload_to='image_best_personal/', verbose_name='Фото ученика')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.personal.__str__()

    class Meta:
        verbose_name = 'Достижение учителя'
        verbose_name_plural = 'Достижении учителей'


class CompetitiveAchievement(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(verbose_name='Описание достижение')

    image_student = models.ImageField(upload_to='image_best_student/', verbose_name='Фото ученика')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Соревновательные Достижение'
        verbose_name_plural = 'Соревновательные Достижении'
