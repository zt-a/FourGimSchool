from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import CustomUserRegistrationForm, UserPasswordChangeForm, CustomUserChangeForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import CustomUserAuthenticationForm


class CustomUserRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomUserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class CustomUserLoginView(LoginView):
    form_class = CustomUserAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


def custom_logout(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile(request):
    # user_profile = get_object_or_404(UserProfile, user=request.user)
    if not request.user.is_authenticated:
        redirect('accounts:login')
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile, 'title': 'Профиль'})


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("accounts:password_change_done")
    template_name = "accounts/password_change_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля'
        return context


class AccountEditView(UpdateView):
    template_name = 'accounts/profile_change_form.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        return context


class AccountDeleteView(DeleteView):
    template_name = 'accounts/account_delete.html'
    success_url = reverse_lazy('accounts:login')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление аккаунта'
        return context
