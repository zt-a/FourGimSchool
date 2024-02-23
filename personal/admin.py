from django.contrib import admin
from .models import *


class PersonalAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'first_name', 'last_name', 'email', 'phone_number', 'time_create', 'work_experience', 'age', 'birthday',
    'is_published')
    list_display_links = ('id', 'first_name', 'last_name', 'email',)
    search_fields = (
    'id', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'work_experience', 'birthday', 'subject_taught',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class StudentAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'school_class', 'citizenship', 'address', 'gender',
    'citizenship', 'passport_number', 'inn', 'is_published')
    list_display_links = ('id', 'first_name', 'last_name', 'patronymic',)
    search_fields = (
    'id', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'school_class', 'citizenship', 'address', 'gender',
    'citizenship', 'passport_number', 'inn' 'is_published')
    list_filter = ('is_published', 'date_of_birth', 'time_create')
    list_editable = ('is_published',)


class ClassAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'class_name', 'class_teacher', 'class_schedule', 'classroom_number', 'time_create', 'is_published')
    list_display_links = ('id', 'class_name', 'class_teacher')
    search_fields = ('id', 'class_name', 'class_teacher', 'classroom_number', 'time_create', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('class_name', )}


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'slug', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'class_name', 'slug', 'time_create', 'time_update',)
    search_fields = ('id', 'class_name', 'slug', 'time_create')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(PersonalModel, PersonalAdmin)
admin.site.register(StudentModel, StudentAdmin)
admin.site.register(ClassModel, ClassAdmin)
admin.site.register(SubjectModel)
admin.site.register(SchedulesModel, SchedulesAdmin)
admin.site.register(GradesStudents)
admin.site.register(Authorities)
admin.site.register(Teachers)
admin.site.register(Parliament)
admin.site.register(RetiredTeachers)
