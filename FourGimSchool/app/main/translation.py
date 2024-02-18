from modeltranslation.translator import translator, TranslationOptions
from .models import *


class RulesTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class FeedbackTranslationOptions(TranslationOptions):
    fields = ('message',)


translator.register(RulesModel, RulesTranslationOptions)
translator.register(CategoryModel, CategoryTranslationOptions)
