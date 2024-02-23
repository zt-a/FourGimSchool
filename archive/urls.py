from django.urls import path
from .views import *


app_name = 'archive'
urlpatterns = [
    path('', DocumentListView.as_view(), name='documents'),
    path('download/<int:document_id>/', DownloadDocumentView.as_view(), name='download_document'),
]