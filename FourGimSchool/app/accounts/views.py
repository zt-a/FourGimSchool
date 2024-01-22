from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import CustomUserRegistrationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.views import LoginView
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


class CustomUserLoginView(LoginView):
    form_class = CustomUserAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('main:index')


def custom_logout(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile(request):
    # user_profile = get_object_or_404(UserProfile, user=request.user)
    if not request.user.is_authenticated:
        redirect('accounts:login')
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})
