from django.urls import path
from .views import *

app_name = 'history'
urlpatterns = [
    path('', HistoryListView.as_view(), name='histories'),
    path('<int:history_id>/', HistoryDetailView.as_view(), name='detail_history'),
]