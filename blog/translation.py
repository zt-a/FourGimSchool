from modeltranslation.translator import translator, TranslationOptions
from .models import *


class CategoryBlogTranslationOptions(TranslationOptions):
    fields = ('name',)


class CommentBlogTranslationOptions(TranslationOptions):
    fields = ('post', 'content',)


class PostBlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(Category, CategoryBlogTranslationOptions)
translator.register(Comment, CommentBlogTranslationOptions)
translator.register(Post, PostBlogTranslationOptions)
