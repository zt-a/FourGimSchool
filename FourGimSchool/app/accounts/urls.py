from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('register/', CustomUserRegistrationView.as_view(), name='register'),
    path('logout/', custom_logout, name='logout'),
    # path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]