from modeltranslation.translator import translator, TranslationOptions
from .models import *


class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(Gallery, GalleryTranslationOptions)