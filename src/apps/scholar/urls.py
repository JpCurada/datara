from django.urls import path
from . import views

app_name = 'scholar'

urlpatterns = [
    path('', views.ScholarDashboardView.as_view(), name='dashboard'),
    path('profile/', views.ScholarProfileView.as_view(), name='profile'),
]
