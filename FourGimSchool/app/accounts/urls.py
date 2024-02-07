from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    # path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('register/', CustomUserRegistrationView.as_view(), name='register'),

    path('profile/', profile, name='profile'),
    path('profile/change/', AccountEditView.as_view(), name='profile_change'),


    path('password-change/', UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="accounts/password_change_form_done.html"), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(
            template_name='accounts/password_reset_form.html',
            email_template_name='accounts/password_reset_email.html',
            success_url=reverse_lazy("accounts:password_reset_done"),
        ),
         name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name="password_reset_done"),

    path('password_reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html',
             success_url=reverse_lazy("accounts:password_reset_complete"),

         ),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('account/delete/', AccountDeleteView.as_view(), name='account_delete'),

]
