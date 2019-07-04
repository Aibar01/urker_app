from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy


# class UserLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     success_url = reverse_lazy('user_profile')


def logout_view(request):
    logout(request)
    return redirect('employees')