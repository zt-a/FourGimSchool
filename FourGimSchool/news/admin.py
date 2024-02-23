from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class NewsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'likes', 'comments_count', 'time_create', 'time_update', 'is_published',)
    list_display_links = ('id', 'title', 'slug', 'author')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    # exclude = ('slug',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'author', 'content', 'time_create', 'is_published')
    list_display_links = ('id', 'news', 'author', 'content')
    list_filter = ('is_published',)
    list_editable = ('is_published',)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
