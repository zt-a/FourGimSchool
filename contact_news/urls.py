from django.urls import path
from .views import ContactViews

app_name = 'contact_news'
urlpatterns = [
    path('', ContactViews.as_view(), name='contact_email')
]