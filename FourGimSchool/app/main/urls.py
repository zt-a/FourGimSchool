from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('feedback/', feedback_list, name='feedback'),
    path('add_feedback/', add_feedback, name='add_feedback'),
    path('rules/', rules, name='rules'),
    path('rules/<slug:slug>/', detail_rules, name='detail_rules'),
    # path('search/', search, name='search'),
]