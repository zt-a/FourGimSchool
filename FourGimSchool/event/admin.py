from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.
admin.site.register(Event, TranslationAdmin)