from django.urls import path
from .views import GalleryListView, GalleryCreateView


app_name='gallery'
urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery_list'),
    path('create_gallery/', GalleryCreateView.as_view(), name='create_gallery'),
]
