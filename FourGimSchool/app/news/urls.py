from django.urls import path
from .views import *


app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('<slug:slug>/add_comment/', add_comment, name='add_comment'),
]
