from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книги'
        return context


class DownloadBookView(View):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug, is_published=True)

        response = HttpResponse(book.pdf_book, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{book.book_name}.pdf"'

        return response
