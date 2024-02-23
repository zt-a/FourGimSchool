from modeltranslation.translator import translator, TranslationOptions
from .models import *


class CategoryForumTranslationOptions(TranslationOptions):
    fields = ('name', )


class CommentForumTranslationOptions(TranslationOptions):
    fields = ('post', 'content', )


class PostForumTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'categories')


translator.register(Category, CategoryForumTranslationOptions)
translator.register(Comment, CommentForumTranslationOptions)
translator.register(Post, PostForumTranslationOptions)