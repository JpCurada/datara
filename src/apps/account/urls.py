# File: src/apps/account/urls.py (Create this new file)
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('admin/login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('scholar/login/', views.ScholarLoginView.as_view(), name='scholar_login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password/reset/', views.PasswordResetView.as_view(), name='password_reset'),
]