from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'name', 'email', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'subject', 'name', 'email')
    search_fields = ('id', 'subject', 'name', 'email', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published', 'time_create')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'phone_number', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'email', 'name', 'surname', 'phone_number')
    search_fields = ('id', 'name', 'surname', 'email', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published', 'time_create')


class RulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_rule', 'title', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'number_rule', 'title',)
    search_fields = ('id', 'number_rule', 'title', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('number_rule', 'is_published', 'time_create')
    prepopulated_fields = {'slug': ('number_rule', 'title',)}


admin.site.register(ContactModel, ContactAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(FeedbackModel, FeedbackAdmin)
admin.site.register(RulesModel, RulesAdmin)
