from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from app.settings import MAIN_HOSTS
from .models import Document


class DocumentListView(ListView):
    model = Document
    template_name = 'archive/documents.html'
    context_object_name = 'documents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_host'] = MAIN_HOSTS
        return context


class DownloadDocumentView(View):
    def get(self, request, document_id):
        document = get_object_or_404(Document, pk=document_id)

        response = HttpResponse(document.pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{document.title}.pdf"'

        return response


