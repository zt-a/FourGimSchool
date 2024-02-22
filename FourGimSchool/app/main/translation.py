from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(RulesModel)
class RulesTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(FeedbackModel)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('message',)


@register(ContactModel)
class ContactModelTranslationOptions(TranslationOptions):
    fields = ('message', )
