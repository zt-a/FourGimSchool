from modeltranslation.translator import translator, TranslationOptions
from .models import *


class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content',)


translator.register(History, HistoryTranslationOptions)
