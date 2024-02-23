from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class PostAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'author', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'title', 'author', )
    search_fields = ('id', 'title', 'author', 'time_create', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published',)


class CommentAdmin(TranslationAdmin):
    list_display = ('id', 'post', 'author', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'post', 'author')
    search_fields = ('id', 'post', 'author', 'time_create', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('id', 'is_published', 'post')


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Like)

