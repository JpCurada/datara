from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('application/', views.ApplicationPageView.as_view(), name='application'),
    path('partner-organization/', views.PartnerOrganizationPageView.as_view(), name='partner_organization'),
    path('faq/', views.FAQPageView.as_view(), name='faq'),
]

