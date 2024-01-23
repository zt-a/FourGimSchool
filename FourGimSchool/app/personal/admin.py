from django.contrib import admin
from .models import *


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'time_create', 'work_experience', 'age', 'birthday', 'is_published')
    list_display_links = ('id', 'first_name', 'last_name', 'email',)
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'work_experience', 'birthday', 'subject_taught', )
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'class_teacher', 'class_schedule', 'classroom_number', 'time_create', 'is_published')
    list_display_links = ('id', 'class_name', 'class_teacher')
    search_fields = ('id', 'class_name', 'class_teacher', 'classroom_number', 'time_create', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'slug', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'class_name', 'slug', 'time_create', 'time_update',)
    search_fields = ('id', 'class_name', 'slug', 'time_create')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')


admin.site.register(PersonalModel, PersonalAdmin)
admin.site.register(ClassModel, ClassAdmin)
admin.site.register(SubjectModel)
admin.site.register(SchedulesModel, SchedulesAdmin)