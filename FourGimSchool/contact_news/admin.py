from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactNewsAdmin(admin.ModelAdmin):
    list_display = ('email', 'time_create')
