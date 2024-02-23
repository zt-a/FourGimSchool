from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class AchievementPersonalAdmin(TranslationAdmin):
    list_display = ('id', 'personal', 'description', 'time_create', 'time_update', 'is_published', 'image_personal',)
    list_display_links = ('id', 'personal',)
    search_fields = ('id', 'personal', 'time_create', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published',)


class AchievementStudentsAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'description', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'full_name',)
    search_fields = ('id', 'full_name', 'time_create', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published',)


class BestStudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'class_student', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'full_name',)
    search_fields = ('id', 'full_name', 'class_student', 'time_create', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published', 'class_student')


class CompetitiveAchievementAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'description', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'full_name',)
    search_fields = ('id', 'full_name', 'time_create', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published',)


admin.site.register(AchievementPersonal, AchievementPersonalAdmin)
admin.site.register(AchievementStudents, AchievementStudentsAdmin)
admin.site.register(BestStudents, BestStudentsAdmin)
admin.site.register(CompetitiveAchievement, CompetitiveAchievementAdmin)
