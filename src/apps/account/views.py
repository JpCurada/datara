from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic import TemplateView

class AdminLoginView(LoginView):
    template_name = 'account/admin_login.html'
    redirect_authenticated_user = True

class ScholarLoginView(LoginView):
    template_name = "account/scholar_login.html"
    redirect_authenticated_user = True

# class LogoutView(LogoutView):
#     next_page = 'home'
