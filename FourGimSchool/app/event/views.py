from django.shortcuts import render
from .models import *
from django.views.generic import ListView


# Create your views here.
class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Event.objects.filter(is_published=True)
