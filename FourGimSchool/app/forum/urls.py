from django.urls import path
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryPostsView.as_view(), name='category_posts'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('post/<int:pk>/like/', LikeCreateView.as_view(), name='like_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
