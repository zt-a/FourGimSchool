from django.db import models
from personal.models import ClassModel, SubjectModel, PersonalModel
from django.utils.translation import gettext_lazy as _


class BestStudents(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    class_student = models.ForeignKey(ClassModel, on_delete=models.CASCADE, verbose_name=_('Класс ученика'),
                                      related_name='best_students')
    image_student = models.ImageField(upload_to='image_best_student/', verbose_name=_('Фото ученика'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Лучший ученик')
        verbose_name_plural = _('Лучшие ученики')


class AchievementStudents(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(verbose_name=_('Описание достижение'))
    image_student = models.ImageField(upload_to='image_students/', verbose_name=_('Фото ученика'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Достижение ученика')
        verbose_name_plural = _('Достижении учеников')


class AchievementPersonal(models.Model):
    personal = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, verbose_name=_('Учитель'))
    description = models.TextField(verbose_name=_('Описание достижение'))

    image_personal = models.ImageField(upload_to='image_best_personal/', verbose_name=_('Фото ученика'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.personal.__str__()

    class Meta:
        verbose_name = _('Достижение учителя')
        verbose_name_plural = _('Достижении учителей')


class CompetitiveAchievement(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(verbose_name=_('Описание достижение'))

    image_student = models.ImageField(upload_to='image_best_student/', verbose_name=_('Фото ученика'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Соревновательные Достижение')
        verbose_name_plural = _('Соревновательные Достижении')
