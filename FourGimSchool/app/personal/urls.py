from django.urls import path
from .views import *

app_name = 'personal'
urlpatterns = [
    path('', personal, name='personal'),
    path('all_personal', all_personal, name='all_personal'),
    path('classes', classes, name='classes'),
    path('classes/<slug:slug>/', class_detail, name='class_detail')
]