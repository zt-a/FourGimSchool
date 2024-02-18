from modeltranslation.translator import translator, TranslationOptions
from .models import *


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )


translator.register(Event, EventTranslationOptions)