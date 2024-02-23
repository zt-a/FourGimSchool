from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file', 'time_create', 'is_published')


admin.site.register(Document, DocumentAdmin)