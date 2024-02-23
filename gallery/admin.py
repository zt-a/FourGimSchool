from django.contrib import admin
from .models import Gallery
from modeltranslation.admin import TranslationAdmin

admin.site.register(Gallery, TranslationAdmin)