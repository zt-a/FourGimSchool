from modeltranslation.translator import translator, TranslationOptions
from .models import *


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


class CommentTranslationOptions(TranslationOptions):
    fields = ('news', 'content',)


translator.register(News, NewsTranslationOptions)
translator.register(Comment, CommentTranslationOptions)
