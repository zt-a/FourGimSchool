from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.views.generic import CreateView


class ContactViews(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_news/tags/form.html'
    success_url = '/'

