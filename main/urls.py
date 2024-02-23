from django.urls import path
from .views import *
from django.views.i18n import set_language


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('set-language/', set_language, name='set_language'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('feedback/', feedback_list, name='feedback'),
    path('add_feedback/', add_feedback, name='add_feedback'),
    path('rules/', rules, name='rules'),
    path('rules/<slug:slug>/', detail_rules, name='detail_rules'),
    path('switch-language/<str:language_code>/', switch_language, name='switch_language'),
]


