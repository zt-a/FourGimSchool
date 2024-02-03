from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Gallery
from .forms import GalleryForm


class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GalleryForm()  # Замените на имя вашей формы
        return context

    def get_queryset(self):
        return Gallery.objects.filter(is_published=True)


class GalleryCreateView(UserPassesTestMixin, CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'gallery/create_gallery.html'
    success_url = reverse_lazy('gallery:gallery_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
